"""
Author: @new92
Program for Scanning the device for open ports
Not for illegal use !
The author has no responsibility for any illegal activities carried out using this tool
"""

#Imports
try:
    import nmap
    import sniffer
    import socket
    import time 
    import os 
    import sys
    import requests
    import geocoder
    import crypto 
    import cryptography
    import getpass
    import pyfiglet
    import logging
except ImportError as imp:
    print("Error ! Please make sure you have installed all the modules !")
    time.sleep(1)
    print("Please enter the command: pip3 install -r OPSrequirements.txt")
    time.sleep(1)
    print("And execute again the program")
    time.sleep(1)
    print(imp)
#End of Imports

#Logo
OPS=pyfiglet.figlet_format("OPS")
print(OPS)

#Main program

print("[+]Tool for Scanning for open ports")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[01] Scan for Open Ports")
print("[02] Exit")
option=input("Choose an option: ")
while option != "01" and option != "02" and option != "1" and option != "2":
    print("Invalid option !")
    option=input("Please enter again: ")
if option == "01" or option == "1":
    hostname=socket.gethostname()
    DevIP=socket.gethostbyname(hostname)

    print("Initiating System Scan for Open Ports")
    time.sleep(10)
    OpenPorts=os.system("nmap --open "+str(DevIP))
    print(OpenPorts)

else: 
    print("Exiting...")
    time.sleep(2)
    quit(0)
#End of the program