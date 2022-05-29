"""
Author: @new92
Anubis: Tool for Information Gathering for Tik Tok accounts 
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
    import locale 
    import platform
    import random 
    import time
    import pyfiglet
    import requests
    import scapy
    import subprocess
    import TikTokApi
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
    print("Modules used: sys, os, TikTokApi, socket, pyfiglet, subprocess, locale, platform, random, time, requests, scapy, geocoder, json, getpass, cryptography, sniffer, nmap, from geopy.geocoders imports Nominatim")
    print(imp)
#End of Imports

#Main program
print("""
          d8888                   888      d8b
         d88888                   888      Y8P
        d88P888                   888
       d88P 888 88888b.  888  888 88888b.  888 .d8888b
      d88P  888 888 "88b 888  888 888 "88b 888 88K
     d88P   888 888  888 888  888 888  888 888 "Y8888b.
    d8888888888 888  888 Y88b 888 888 d88P 888      X88
   d88P     888 888  888  "Y88888 88888P"  888  88888P'
""")
api = TikTokApi 
def UserVideos(username):
    uvideos = 100
    username = usernameused
    user_videos = api.byUsername(username, uvideos)
    return user_videos
def UserLikes(username):
    n_videos = 10
    username = usernameused
    liked_videos = api.userLikedbyUsername(username, count=n_videos)
    liked_videos = [simple_dict(v) for v in liked_videos]
    liked_videos_df = pd.DataFrame(liked_videos)
    liked_videos_df.to_csv('{}_liked_videos.csv'.format(username), index=False)
    return 
time.sleep(1)
user=input("Please enter the username of the victim: ")
usernameused=user.lower()
time.sleep(1)

#Information Gathering 
AllUserInfo = TikTokApi.user(username = usernameused).info_full()
Videos = UserVideos(usernameused)
Likes = UserLikes(usernameused)
UserID = api.user(username = usernameused).user_id

#End of Information Gathering


#Displaying the information which have been gathered
"""
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
print("This is the profile Anubis formed with the information: ")
time.sleep(4)
"""
print("|----------------PROFILE--------------|                 ")
print("                                                        ")
time.sleep(2)
print("      Username: "+str(usernameused)+"                       ")
time.sleep(2)
print("      All Information: "+str(AllUserInfo)+"                 ")
time.sleep(2)
print("      User Videos: "+str(Videos)+"                      ")
time.sleep(2)
print("      User Likes: "+str(Likes)+"                        ")
time.sleep(2)
print("      User's ID: "+str(UserID)+"                        ")
time.sleep(2)
print("                                                        ")
print("|---------------------------------------|               ")
#End of the program