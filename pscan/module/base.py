# -*- coding: utf-8 -*-
class Base:
    def __init__(self, scan_target = "", scan_ports = "80", scan_thread = 200):
        self.scan_target = self.split_ip(scan_target)
        self.scan_ports = self.split_port(scan_ports)
        self.scan_thread = scan_thread

    def split_ip(self, ip): #判断是一个IP还是一个IP段
        ips = len(ip.split('-'))
        iplist= []
        if ips == 1:
            iplist.append(ip)
            return iplist
        else:
            ipfinal = ip.split('-')[0][:-len(ip.split('-')[0].split('.')[-1])]
            start = int(ip.split('-')[0].split('.')[-1])
            end = int(ip.split('-')[1]) + 1
            for i in range(start, end):
                if len(ip.split(".")) == 4:
                    iplist.append(ipfinal + str(i))
                elif len(ip.split(".")) == 3:
                    for j in range(1,255):
                        iplist.append(ipfinal + str(i) + "." + str(j))
            return iplist

    def split_port(self, port):
        portlist = []
        if "," in port:
            portlist =[int(s) for s in port.split(",")] 
        elif len(port.split("-")) == 1:
            portlist.append(int(port))
        else:
            start, end = int(port.split("-")[0]), int(port.split("-")[1])
            for i in range(start, end+1):
                portlist.append(i)
        return portlist