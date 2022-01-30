import platform
import subprocess
import socket
from colorama import init , Fore, Back
from ping3 import ping
init()

def icmp(host):
    resp = ping(host)
    if resp:
        print("Online")
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

NetworkAddress = socket.gethostbyname(socket.gethostname())
Last_Octet = NetworkAddress.rfind(".")
NetworkAddress = NetworkAddress[:10]
print("Network Address - ",NetworkAddress+"0")
print("Pinging 25 IP addresses in the above detected Network \n")
for x in range(1,26,1):
    IP = NetworkAddress+str(x)
    print("Pinging "+IP+" -- ",end=" ")
    icmp(IP)


