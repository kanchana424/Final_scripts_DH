#This function defines telnet login by taking input from login.json file.

import sys
import Telnet_Login
import time

def show_versions():
    tm=Telnet_Login.login_A()
    tm.write(b" set cli-parameters pager off \n")
    tm.write(b" show versions \n")
    tm.write(b" exit \n")
    time.sleep(30)                 	        
    data=tm.read_all().decode('UTF-8')	        
    file = open("C:\python3.6\Final scripts\Logs\show_versions", "w+").write(data)
    file = open("C:\python3.6\Final scripts\Logs\show_versions", "r+")
    content = file.readlines()
    ind_A= content.index("Controller A Versions\n")+4 #4 is to remove ---and Build version information from list
    ind_B= content.index("Controller B Versions\n")+4
    FW_A = content[ind_A].split(":")
    FW_B = content[ind_B].split(":")
    cntrlA_ver =FW_A[1].strip() #Take the index 1 from the list
    cntrlB_ver =FW_B[1].strip() #Strip is to remove white spaces on both sides of a string
    return (cntrlA_ver,cntrlB_ver)

'''
i=1

while i <= 50:
    cntrlA_ver,cntrlB_ver = show_versions()
    print(cntrlA_ver)
    print(cntrlB_ver)
    print("iteration : ",i)
    i = i +1
    '''
