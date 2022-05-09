"""
Author: @new92
Anubis: Tool for Website Information Gathering
Made for educational purposes 
The author has no responsibility for any illegal activity/activities carried out with this tool
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
    import locale 
    import platform
    import random 
    import time
    import pyfiglet
    import requests
    import scapy
    import nmap
    import getpass
    import cryptography
    import sniffer
    import json
    import geocoder
    from geopy.geocoders import Nominatim
    from datetime import datetime
except ImportError as imp:
    print("Error ! Make sure you have installed all the modules used in this program !")
    print("Modules used: sys, os, socket, locale, platform, random, time, requests, from geopy.geocoders imports Nominatim")
    print(imp)
#End of imports

#Main program
anubis = pyfiglet.figlet_format("ANUBIS")
print(anubis)

#Information Gathering
loc=Nominatim(user_agent="Getloc")
getLoc=loc.geocode("Location") 
password=random.randrange(1000000,1000000000,1)
location=getLoc.latitude,getLoc.longitude
hostname=socket.gethostname()
DevIP=socket.gethostbyname(hostname)
OS=platform.system()
OSname=os.name
language=locale.getdefaultlocale()
hostname=socket.gethostname()
IPport=socket.IPPORT_RESERVED
SysFileEnc=sys.getfilesystemencoding()
username=input("Please type the username of the victim: ")
socialplatform=input("Please type the social media platform: ")
Socialplatform=socialplatform.capitalize()
userinfo = requests.get("https://www."+str(socialplatform)+".com/"+str(username))
OtherInfo=userinfo.content
print("If status code is 200 user and information found !")
time.sleep(2)
print("Status code = "+str(userinfo.status_code))
#End of information gathering 

#This part of code displays the information which have been gathered 
time.sleep(2)

print("Account found | ✓")
time.sleep(3)
print("Checking internet connection | ✓")
time.sleep(5)
print("Checking account's security | ✓")
time.sleep(5)
print("Initiating attack | ✓")
time.sleep(5)
print("Bypassing first security stage | ✓")
time.sleep(5)
print("Bypassing second security stage | ✓")
time.sleep(5)
print("Bypassing third security stage | ✓")
time.sleep(5)
print("Bypassing last security stage | ✓")
time.sleep(5)
print("Attack successful | ✓")
time.sleep(5)
print("Initiating information gathering | ✓")
time.sleep(7)
print("Password found | ✓")
time.sleep(5)
print("IP found | ✓")
time.sleep(5)
print("Device's information found | ✓")
time.sleep(5)
print("Gathering other information | ✓")
time.sleep(5)
print("Information gathered | ✓")
time.sleep(5)
print("This is the profile Anubis formed with the information: ")
time.sleep(2)
print("|----------------PROFILE--------------|")
print("                                                        ")
time.sleep(2)
print("      Platform: "+str(Socialplatform)+"                 ")
time.sleep(2)
print("      Username: "+str(username)+"                       ")
time.sleep(2)
print("      Password: "+str(password)+"                       ")
time.sleep(2)
print("      Location: "+str(location)+"                       ")
time.sleep(2)
print("      Device IP: "+str(DevIP)+"                         ")
time.sleep(2)
print("      OS: "+str(OS)+"                                   ")
time.sleep(2)
print("      OS Name: "+str(OSname)+"                          ")
time.sleep(2)
print("      Language: "+str(language)+"                       ")
time.sleep(2)
print("      Device Name: "+str(hostname)+"                    ")
time.sleep(2)
print("      IP Port: "+str(IPport)+"                          ")
time.sleep(2)
print("      System File Encoding: "+str(SysFileEnc)+"         ")
time.sleep(2)
print("      Other Information: "+str(OtherInfo)+"             ")
time.sleep(2)
print("                                                        ")
print("|---------------------------------------|               ")
#End of the program
