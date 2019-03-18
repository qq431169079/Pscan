# -*- coding: utf-8 -*-
import threading, socket, sys, cmd, os, Queue
import time
import re
import requests
from base import *
lock = threading.Lock()

class Sens(Base):
    def get_tagget_queue(self, hosts ,ports, paths):
        IpQueue = Queue.Queue()
        for host in hosts:
            for port in ports:
                for path in paths:
                    IpQueue.put((host, port, path))
        return IpQueue
    def run(self):
        ThreadList = []
        paths = open("src.txt").readlines()
        IpQueue = self.get_tagget_queue(self.scan_target, self.scan_ports, paths)        
        for i in range(self.scan_thread):
            t = Scan(IpQueue)
            t.start()
            ThreadList.append(t)
        for t in ThreadList:
            t.join(0.4)

class Scan(threading.Thread):
    def __init__(self, InQueure):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.InQueure = InQueure

    def scan_target(self, host, port, path):
        url = "http://%s:%s/%s" % (host, port, path.strip())

        s = requests.Session()
        s.keep_live = False
        res = s.get(url=url, timeout=0.2)
        if res.status_code != 200:
            return False        
        if lock.acquire():
            print "[*] %s" % url
            lock.release()
        return True
    
    def run(self):
        while not self.InQueure.empty():
            host, port, path = self.InQueure.get()
            self.scan_target(host, port, path)