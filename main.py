#! /usr/bin/env python
import netifaces as ni
import ethernet
import socket
from time import sleep
from colorama import init , Fore, Back
from ping3 import ping
import scapy.all as scapy
init()

online = {}

def pings(host):
    resp = ping(host)
    if resp:
        online[host] = {}

print(Fore.GREEN+"""\033[1m 
__________                  __             __         __      __          __           .__     
\______   \_____     ____  |  | __  ____ _/  |__     /  \    /  \_____  _/  |_   ____  |  |__  
 |     ___/\__  \  _/ ___\ |  |/ /_/ __ \\\   ___\    \   \/\/   /\__  \ \   __\_/ ___\ |  |  \ 
 |    |     / __ \_\  \___ |    < \  ___/ |  |        \        /  / __ \_|  |  \  \___ |   Y  \\
 |____|    (____  / \___  >|__|_ \ \___  >|__|         \__/\  /  (____  /|__|   \___  >|___|  /
                \/      \/      \/     \/                   \/        \/            \/      \/ 

\033[0m""")

print("* Looking for Interfaces")
sleep(3)
interfaces = scapy.get_if_list()
interfaceCount = len(interfaces)
print("* Found "+str(interfaceCount)+" interfaces")
sleep(3)

print("* Choose the network interface of your choice -")
for x in range(interfaceCount):
    print(f"     {x+1} . {interfaces[x]} ")
interfaceChoice = int(input("\n* Choice - "))-1
sleep(1.5)
interface = interfaces[interfaceChoice]

print("* Getting interface IP - ",end="")
sleep(0.5)
interfaceIP = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

print(interfaceIP)
Last_Octet = interfaceIP.rfind(".")
NetworkAddress = interfaceIP[:10]
print("* Network Address - ",NetworkAddress+"0")
sleep(1)
print("\n*** Pinging 20 IP addresses in the above detected Network ***")
y = 0
for x in range(1,21,1):
    
    IP = NetworkAddress+str(x)
    hashes = "#" * (3 * x)
    dots = "." * (60 - (3 * x))
    perc = int((x/20) * 100)
    print(f"[ {hashes}{dots} ] {perc}%",end="\r")
    pings(IP)

print("\n")
ethernet.printArpTable()