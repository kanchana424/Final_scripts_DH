

import time
import ftplib
import sys
import telnetlib
import Versions_details
import Read_JSON

hostA = "10.1.25.107"
hostB = "10.1.25.108"
user = "manage"
password = "!manage"

def set_pfu_disable():
        tm=telnetlib.Telnet(hostA,23,10)
        tm.read_until(b"login: ")
        tm.write(user.encode('UTF-8') + b"\n")
        tm.read_until(b"Password: ")
        tm.write(password.encode('UTF-8') + b"\n")
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        tm.write(b" set advanced-settings partner-firmware-upgrade disabled  \n")
        time.sleep(3)#Need to add code to verify whether PFU is disabled or not, check xml	
        tm.write(b" exit \n")
        #data=tm.read_all().decode('UTF-8')
        time.sleep(15)
        #file = open("C:\python3.6\Final scripts\Logs\TC10-FTP_Upgrade_Downgrade.txt", "a+")
        #file.write("*************PFU DISABLED for "+str(i)+" time *************\n")
        #file.write(data)
        ftp = ftplib.FTP(hostA,user,password)
        ftp.storbinary('STOR flash', open('C:\python3.6\Sanity_Testcases\Firmware\GL220P008-06-HP.bin', 'rb'))#Need to find alternate way to give path
        time.sleep(500)
        ftp = ftplib.FTP(hostB,user,password)
        ftp.storbinary('STOR flash', open('C:\python3.6\Sanity_Testcases\Firmware\GL220P008-06-HP.bin', 'rb'))
        time.sleep(500)
        tm.close()
                
def set_pfu_enable():
        tm=telnetlib.Telnet(hostA,23,10)
        tm.read_until(b"login: ")
        tm.write(user.encode('UTF-8') + b"\n")
        tm.read_until(b"Password: ")
        tm.write(password.encode('UTF-8') + b"\n")
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        tm.write(b" set advanced-settings partner-firmware-upgrade enabled \n")
        time.sleep(3)#Need to add code to verify whether PFU is disabled or not, check xml	
        tm.write(b" exit \n")
        #data=tm.read_all().decode('UTF-8')
        time.sleep(15)
        #file = open("C:\python3.6\Final scripts\Logs\TC10-FTP_Upgrade_Downgrade.txt", "a+")
        #file.write("*************PFU DISABLED for "+str(i)+" time *************\n")
        #file.write(data)
        ftp = ftplib.FTP(hostA,user,password)
        ftp.storbinary('STOR flash', open('C:\python3.6\Sanity_Testcases\Firmware\GL220P009-15-HP.bin', 'rb')) #Need to find alternate way to give path
        time.sleep(200)
        tm.close()
	

count =2
while (count>=0):
        print("********************************************\n")
        print(count)
        System_CntrlA,System_CntrlB = Versions_details.show_versions()
        print(System_CntrlA,System_CntrlB)
        print("Started pfu disabled \n")
        set_pfu_disable()
        time.sleep(800)
        print("pfu disabled ended \n")
        System_CntrlA,System_CntrlB = Versions_details.show_versions()
        print(System_CntrlA,System_CntrlB)
        print("Started pfu enabled \n")
        set_pfu_enable()    
        time.sleep(800)
        print("pfu enabled ended \n" )
        count =  count -1
        


