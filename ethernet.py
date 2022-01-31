from time import sleep
from prettytable import PrettyTable
import os

def getArpTable():
    unavailable = "<incomplete>"
    devices = os.popen('arp -a').read().split("\n")
    ipMAC = {}
    for x in range(len(devices)-1):
        y = devices[x].split(" ")
        if y[3] != unavailable:
            ip = y[1][1:-1]
            ipMAC[ip] = y[3]
    return ipMAC

def printArpTable():
    ipMAC = getArpTable()
    print("ARP Table ")
    tab = []
    for IP,MAC in ipMAC.items():
        tab.append([IP, MAC])
    ARP_TABLE = PrettyTable(['IP Address', 'Mac Address'])
    for row in tab:
        ARP_TABLE.add_row(row)
    sleep(2)
    print(ARP_TABLE)



