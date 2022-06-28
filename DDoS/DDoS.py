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
#End of the Program