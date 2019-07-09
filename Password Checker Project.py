# -*- coding: utf-8 -*-

import re
import time

pwd = input("Enter a password: ")

patterns = [r'^.{8,32}$', r'[A-Za-z0-9#@!*$&\-.+]', r'^.*[A-Z].*$', r'^.*[a-z].*$', r'^.*[0-9].*$', 
            r'^.*[#@!*$&\-.+].*$', r'^.*(.)\1{2,}.*$']
error_msgs = ["Length of password is not between 8 to 32 characters", "Password contains 1 or more invalid character(s)", 
              "Password must contain atleast 1 upper case letter", "Password must contain atleast 1 lower case letter", 
              "Password must contain atleast 1 digit from 0 to 9", "Password must contain atleast 1 special character", 
              "Password must not contain repetition of characters"]
chk_list = []

def pwd_chk_disp():
    print('\r'+'Checking the password, please wait.                \r', end='\r')
    time.sleep(0.5)
    print('\r'+'Checking the password, please wait..               \r', end='\r')
    time.sleep(0.5)
    print('\r'+'Checking the password, please wait...              \r', end='\r')
    time.sleep(0.5)
    print('\r'+'Checking the password, please wait....             \r', end='\r')
    time.sleep(0.5)
    print('\r'+'Checking the password, please wait.....            \r', end='\r')
    time.sleep(0.5)
    print('\n')

while True:
    if pwd != '':
        pwd_chk_disp()
        for i in range(0, 6):
            if not re.search(patterns[i], pwd):
                print(error_msgs[i])
                chk_list.append(False)
            else:
                chk_list.append(True)
            
        if re.search(patterns[6], pwd):
            print(error_msgs[6])
            chk_list.append(False)
        else:
            chk_list.append(True)
    
    else:
        print("You didn't enter any password")
        pwd = input("Enter a password: ")
        continue
        
    if False in chk_list: 
        pwd = input("Enter a password: ")
        chk_list = []
        
    else:
        print("Password verified")
        break
 
    
    
    
    
    
