#!/usr/bin/python2

import os
import re
import time

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

def fuck():
    os.system('clear')
    banner()
    print("[1] Extract Pakistan Number With uuid")
    time.sleep(0.05)
    print("[2] Extract Pakistan Number (fast)")
    time.sleep(0.05)
    print("[3] Get Phone Number Information With Country")
    time.sleep(0.05)
    print("[4] How To Create Fake Number Whatsapp")
    time.sleep(0.05)
    print("[0] Direct back")
    time.sleep(0.05)
    print("-------------------------------------------------")
    m()
def m():
    fuck = raw_input("\n[!] Please select a valid option : ")
    if fuck =="1":
        os.system("cd uuid && python2 uuid")
    if fuck =="2":
        os.system("dpkg -i num*.deb")
        os.system("num")
    if fuck =="3":
        os.system("cd info && python2 info.py")
    if fuck =="4":
        os.system("xdg-open https://www.facebook.com/113361253709847/posts/408663280846308/?app=fbl")
        time.sleep(1)
        fuck()
    if fuck =="0":
        os.system("cd - && pytho2 domains.py")
    else:
        print("")
        print("Please select a valid option").center(50)
        print("")
        time.sleep(2)
        fuck()
if __name__ == '__main__':
    fuck()
