# -*- coding: utf-8 -*-
import threading, socket, sys, cmd, os, Queue
import time
import re
import requests

from base import *
lock = threading.Lock()
class Port(Base):
    def get_tagget_queue(self, hosts ,ports):
        IpQueue = Queue.Queue()
        for host in hosts:
            for port in ports:
                IpQueue.put((host, port))
        return IpQueue

    def run(self):
        ThreadList = []
        IpQueue = self.get_tagget_queue(self.scan_target, self.scan_ports)
        resultqurere = Queue.Queue()
        
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
        self.web_title = ''
        self.web_server = ''
        self.web_status = ''

    def scan_target(self, host, port):
        global lock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        address = (host, port)
        socks_banners = ''
        try:          
            sock.connect(address)
        except:
            sock.close()
            return False
        try:
            sock.send('HELLO\r\n')
            socks_banners = sock.recv(1024).split('\r\n')[0].strip('\r\n')
        except:
            pass
        sock.close()
        self.get_info(host, port)
        if lock.acquire():
            print "[*] %15s : open port %5s  %40s ||  %20s  %5s  %s" %(host, port, socks_banners, self.web_server, self.web_status, self.web_title )
            lock.release()
        return True
    
    def get_info(self, host, port):
        url = "http://%s:%d" % (host ,port)
        try:
            s = requests.Session()
            s.keep_live = False
            infos = s.get(url=url, timeout=0.2)
            self.web_status = int(infos.status_code)
            try:
                self.web_server = infos.headers['server']
            except:
                pass
            try:
                self.web_title = re.findall(r'<title>(.*)</title>', infos.text)[0]
            except:
                pass
        except:
           pass
    def run(self):
        while not self.InQueure.empty():
            host, port = self.InQueure.get()
            self.scan_target(host, port)