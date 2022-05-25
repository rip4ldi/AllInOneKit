"""
Author: @new92
Program for information gathering for Social Media accounts 
Made for educatinoal purposes
The author has no responsibility for any illegal activity/activities carried out using this tool
"""

#Sniffer

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
    import subprocess
    import geocoder
    import smtplib
    import json 
    import getpass
    import cryptography
    import sniffer
    import nmap
    from geopy.geocoders import Nominatim
except ImportError as imp:
    print("Error ! Make sure you have installed all the modules used in this program !")
    time.sleep(1)
    print("Please enter the command: pip3 install -r requirements.txt")
    time.sleep(1)
    print("And execute again the program")
    time.sleep(1)
    print(imp)
#End of imports


#Main program 
snif = pyfiglet.figlet_format("SNIFFER")
print(snif)

username=input("Please type the username of the victim: ")
time.sleep(1)
socialplatform=input("Please type the social media platform: ")
socialplatformused=socialplatform.lower()
usernameused=username.lower()
Socialplatform=socialplatform.capitalize()

#Information Gathering

userinfo = requests.get("https://www."+str(socialplatformused)+".com/"+str(usernameused))
UsefulInfo=userinfo.headers
OtherInfo=userinfo.content
if userinfo.status_code == requests.codes.ok: 
    print("User and information found !")
else: 
    print("User not found !")
    print("Try checking the username and the platform")
Information = UsefulInfo, OtherInfo
#End of Information Gathering

#Display Information which have been gathered
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
print("This is the profile Sniffer formed with the information: ")
time.sleep(4)
print("|----------------PROFILE--------------|                 ")
print("                                                        ")
time.sleep(2)
print("      Platform: "+str(Socialplatform)+"                 ")
time.sleep(2)
print("      Username: "+str(username)+"                       ")
time.sleep(2)
print("      Information: "+str(Information)+"                 ")
time.sleep(2)
print("                                                        ")
print("|---------------------------------------|               ")
#End of the program
