# -*- coding: utf-8 -*-
# author: p0desta

import argparse
import  time

from module.portscan import *
from module.sensscan import *
describe = '''
______                    
| ___ \                   
| |_/ /__  ___ __ _ _ __  
|  __/ __|/ __/ _` | '_ \ 
| |  \__ \ (_| (_| | | | |
\_|  |___/\___\__,_|_| |_|                 author: p0desta\n
'''
print describe

parser = argparse.ArgumentParser(description='Pscan')
parser.add_argument("-m", "--mode", help='''****************Choose an scan mode****************
        ***************port:   port scan ***************
        ****sens:   sensitive information scanning *****''', required=True)
parser.add_argument("--host", help="please input host, example: 192.168.1.1 or 192.168.1.1-254", required=True)
parser.add_argument("--port", help="please input your port,example:80  or  80,8080 or 80-100", default="80")
parser.add_argument("--thread", help="please input your thread", default=50, type=int)


args = parser.parse_args()
if args.mode == "port":
    exp = Port(args.host, args.port, args.thread)
    exp.run()
elif args.mode == "sens":
    exp = Sens(args.host, args.port, args.thread)
    exp.run()

