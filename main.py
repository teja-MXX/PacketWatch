#! /usr/bin/env python
import netifaces as ni
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
        print("Online")
        online[host] = {}
    else:
        print("Unreachable")

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
print("* Pinging 25 IP addresses in the above detected Network \n")
for x in range(1,26,1):
    IP = NetworkAddress+str(x)
    print("  Pinging "+IP+" -- ",end=" ")
    pings(IP)

