#!/usr/bin/env python2
import re,os,requests
import time
from os import system
from platform import platform
from time import sleep
import sys
sys.platform
'wind32', 'wind64', 'linux', '32bit', '64bit', 'android'
import os
xoo = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if xoo == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    abm = 'cls'
    dr = '\\'
else:
    abm = 'clear'
    dr = '/'

os.system(abm)
time.sleep(1)
print("loading modules...")
time.sleep(0.05)
os.system(abm)
print("lOading modules...")
time.sleep(0.05)
os.system(abm)
print("loAding modules...")
time.sleep(0.1)
os.system(abm)
print("loaDing modules...")
time.sleep(0.1)
os.system(abm)
print("loadIng modules...")
time.sleep(0.1)
os.system(abm)
print("loadiNg modules...")
time.sleep(0.1)
os.system(abm)
print("loadinG modules...")
time.sleep(0.1)
os.system(abm)
print("loading modules...")
time.sleep(0.1)
os.system(abm)
print("loading mOdules...")
time.sleep(0.1)
os.system(abm)
print("loading moDules...")
time.sleep(0.1)
os.system(abm)
print("loading modUles...")
time.sleep(0.1)
os.system(abm)
print("loading moduLes...")
time.sleep(0.1)
os.system(abm)
print("loading modulEs...")
time.sleep(0.1)
os.system(abm)
print("loading moduleS...")
time.sleep(0.1)
os.system(abm)
print("loading modules...")
time.sleep(0.1)
os.system(abm)
print("Loading modules...")
time.sleep(0.1)
os.system(abm)
print("lOading modules...")
time.sleep(0.1)
os.system(abm)
print("loAding modules...")
time.sleep(0.1)
os.system(abm)
print("loaDing modules...")
time.sleep(0.1)
os.system(abm)
print("loadIng modules...")
time.sleep(0.1)
os.system(abm)
print("loadiNg modules...")
time.sleep(0.1)
os.system(abm)
print("loadinG modules...")
time.sleep(0.1)
os.system(abm)
print("loading Modules...")
time.sleep(0.1)
os.system(abm)
print("loading mOdules...")
time.sleep(0.1)
os.system(abm)
print("loading moDules...")
time.sleep(0.1)
os.system(abm)
print("loading modUles...")
time.sleep(0.1)
os.system(abm)
print("loading moduLes...")
time.sleep(0.1)
os.system(abm)
print("loading modulEs...")
time.sleep(0.1)
os.system(abm)
print("loading moduleS...")
time.sleep(0.1)
os.system(abm)
print("loading modules...")
time.sleep(0.1)
os.system(abm)

def banner():
    print("""
         88888888b  888888ba   a88888b. 
         88         88    `8b d8'   `88 
        a88aaaa    a88aaaa8P' 88        
         88         88   `8b. 88        
         88         88    .88 Y8.   .88 
         dP         88888888P  Y88888P'                               
------------------------------------------------- 
(~) Author  : Tech Abm
(~) Github  : https://github.com/Tech-abm
(~) Fb Page : https://facebook.com/Techabm
-------------------------------------------------   
""")

def main():
    os.system("clear")
    banner()
    print("[1] Install Fbc Tool 64bit Version (Simple)");time.sleep(0.05)
    print("[2] Install Fbc Tool 64bit Version   (Vip)");time.sleep(0.05)
    print("[3] Tool Exit");time.sleep(0.05)
    print("-------------------------------------------------");time.sleep(0.05)
    m()
def m():
    user_option = raw_input("\n[!] Select an valid option : ")
    if user_option =="1":
        fbc_01()
    if user_option =="2":
        fbc_02()
    if user_option =="3":
        print("")
        print("Tool Logout Successfull").center(50)
        time.sleep(1)
        os.system("exit")
    else:
        print("")
        print("Please select an correct option").center(50)
        print("")
        time.sleep(1)
        main()

def fbc_01():
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("")
    os.system("uname -om")
    print("")
    print("This tool is works only 64bit version").center(50)
    print("If your termux is 64bit - you can use this tool").center(50)
    ask_user = raw_input("\tYour termux is 64bit version (yes/no) ")
    if ask_user =="yes":
        os.system("cd old_main && python2 main.py")
    if ask_user =="no":
        print("")
        print("Unknow Device Aarch, Please try again").center(50)
        time.sleep(1)
        main()
    else:
        print("")
        print("Please select an valid option").center(50)
        print("")
        time.sleep(1)
        main()

def fbc_02():
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("")
    os.system("uname -om")
    print("")
    print("This tool is works only 64bit version").center(50)
    print("If your termux is 64bit - you can use this tool").center(50)
    ask_user = raw_input("\tYour termux is 64bit version (yes/no) ")
    if ask_user =="yes":
        os.system("cd fbc_main && python2 install.py")
    if ask_user =="no":
        print("")
        print("Unknow Device Aarch, Please try again").center(50)
        time.sleep(1)
        main()
    else:
        print("")
        print("Please select an valid option").center(50)
        print("")
        time.sleep(1)
        main()

if __name__ == '__main__':
    main()
