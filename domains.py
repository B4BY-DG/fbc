#!/usr/bin/env python2
try:
    import os
    import re
    import time
    import sys
    import bs4
except IOError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("pip2 install requests bs4")
    os.system("python2 domains.py")

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
    os.system("xdg-open https://facebook.com/Techabm")
    time.sleep(0.05)
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
    os.sytem("clear")
    banner()
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
    os.sytem("clear")
    banner()
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
