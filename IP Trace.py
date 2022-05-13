"""
Author: @new92
Only for educational purposes 
The author has no responsibility for any illegal activity carried out using this tool 
Tool for IP tracing for websites 
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
    import websockets
    import requests
    import pyfiglet
    import nmap 
    import sniffer
    import scapy
except ImportError as imp:
          print("Error ! Make sure you have installed all the modules used in this program !")
          print("Modules used: sys, os, socket, websockets, requests, pyfiglet, python-nmap, sniffer, scapy")
          print(imp)

#End of Imports
def websites():
          print("[1] : Google")
          print("[2] : Youtube")
          print("[3] : Facebook")
          print("[4] : Instagram")
          print("[5] : Twitter")
          print("[6] : Netflix")
          print("[7] : TikTok")
          print("[8] : Pinterest")
          print("[9] : Snapchat")

#Main program 
# An example script to connect to Google using socket
# programming in Python

ascii_banner = pyfiglet.figlet_format("ANUBIS")
print(ascii_banner)

websites()

choice=int(input("Please enter the number of the website you want to trace the IP from: "))
while choice < 1 and choice > 9: 
          print("Invalid choice !")
          choice=int(input("Please enter again the number of the website you want to trace the IP from: "))
          websites()
if choice == "1":          
    try:
        IPGoogle = socket.gethostbyname("www.google.com")
        print("The IP for Google is: "+str(IPGoogle))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "2": 
    try:
        IPYoutube = socket.gethostbyname("www.youtube.com")
        print("The IP for Youtube is: "+str(IPYoutube))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "3":
    try:
        IPFacebook = socket.gethostbyname("www.facebook.com")
        print("The IP for Facebook is: "+str(IPFacebook))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "4": 
    try:
        IPInstagram = socket.gethostbyname("www.instagram.com")
        print("The IP for Instagram is: "+str(IPInstagram))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "5":
    try: 
        IPTwitter = socket.gethostbyname("www.twitter.com")
        print("The IP for Twitter is: "+str(IPTwitter))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "6":
    try:
        IPNetflix = socket.gethostbyname("www.netflix.com")
        print("The IP for Netflix is: "+str(IPNetflix))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "7":
    try: 
        IPTikTok = socket.gethostbyname("www.tiktok.com")
        print("The IP for TikTok is: "+str(IPTikTok))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "8":
    try:
        IPPinterest = socket.gethostbyname("www.pinterest.com")
        print("The IP for Pinterest is: "+str(IPPinterest))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "9":
    try:
        IPSnapchat = socket.gethostbyname("www.snapchat.com")
        print("The IP for Snapchat is: "+str(IPSnapchat))
    except socket.herror() as s:
        print("Error !")
        print(s)
elif choice == "10":
    try:
        IPReddit = socket.gethostbyname("www.reddit.com")
        print("The IP for Reddit is: "+str(IPReddit))
    except socket.herror as s: 
        print("Error !")
        print(s)
#End of program
