#This program will login to telnet and execute few commands and write the output to a file. 
#Login details host, username and password are read from a json file. 
#If there is any change in login details, the json file can be changed instead of changing in code.
#While executing the program, give the json file here it is "python telnet_login_details_through_json.py Login_details.json" from command prompt.
#The file is given as an argument to function.
#to use the values in json file the syntax is cmds["FTP LOGIN"]["host"] , here cmds is the variable where we loaded json file.
#TO access the values in json file we have to give cmds [whatever function name we gave in json file][parameter name in the function]

import time
from pprint import pprint
import ftplib
import Telnet_Login
import sys
import Versions_details
import Read_JSON

i =0
def set_pfu_disable():
        tm=Telnet_Login.login_A()	
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        tm.write(b" set advanced-settings partner-firmware-upgrade disabled  \n")
        time.sleep(3)#Need to add code to verify whether PFU is disabled or not, check xml	
        tm.write(b" exit \n")
        data=tm.read_all().decode('UTF-8')
        time.sleep(15)
        file = open("C:\python3.6\Final scripts\Logs\TC10-FTP_Upgrade_Downgrade.txt", "a+")
        file.write("*************PFU DISABLED for "+str(i)+" time *************\n")
        file.write(data)
        #System_CntrlA,System_CntrlB = Versions_details.show_versions()
        ftp = ftplib.FTP(Read_JSON.get_controller_A_IP(),Read_JSON.getUserName(),Read_JSON.getPassword())
        ftp.storbinary('STOR flash', open('C:\python3.6\Sanity_Testcases\Firmware\GL220P008-06-HP.bin', 'rb'))#Need to find alternate way to give path
        time.sleep(200)
        ftp = ftplib.FTP(Read_JSON.get_controller_B_IP(),Read_JSON.getUserName(),Read_JSON.getPassword())
        ftp.storbinary('STOR flash', open('C:\python3.6\Sanity_Testcases\Firmware\GL220P008-06-HP.bin', 'rb'))
        time.sleep(200)
        tm.close()
        #return (System_CntrlA,System_CntrlB)
                
def set_pfu_enable():
        tm=Telnet_Login.login_A()
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b"set cli-parameters api \n")
        tm.write(b" set advanced-settings partner-firmware-upgrade enabled \n")
        #Need to add code to verify whether PFU is enabled or not, check xml	
        time.sleep(3)	
        tm.write((" exit \n").encode('ascii'))
        data=tm.read_all().decode('UTF-8')
        time.sleep(15)
        file = open("C:\python3.6\Final scripts\Logs\TC10-FTP_Upgrade_Downgrade.txt", "a+")
        file.write("*************PFU ENABLED for "+str(i)+" time *************\n")
        file.write(data)
        ftp = ftplib.FTP(Read_JSON.get_controller_A_IP(),Read_JSON.getUserName(),Read_JSON.getPassword())
        ftp.storbinary('STOR flash', open('C:\python3.6\Sanity_Testcases\Firmware\GL220P009-15-HP.bin', 'rb')) #Need to find alternate way to give path
        time.sleep(200)
        tm.close()
	
count = Read_JSON.getFW_up_down_count()
User_Upver = Read_JSON.getUpgradeVer()
User_Downver = Read_JSON.getDowngradeVer()
#System_CntrlA,System_CntrlB = Versions_details.show_versions()

#print(count)
#print(User_Upver)
#print(User_Downver)
#print(System_CntrlA)
#print(System_CntrlB)


while (i<=int(count)):
        System_CntrlA,System_CntrlB = Versions_details.show_versions()
        if ((System_CntrlA == User_Upver) and (System_CntrlB == User_Upver)):
                set_pfu_disable()
                #Here need to check whether SC,MC,CPLD are loaded successfully or not
                print("pfu disabled \n" )
                break
        elif ((System_CntrlA == User_Downver) and (System_CntrlB == User_Downver)):        
                set_pfu_enable()
                #Here need to check whether SC,MC,CPLD are loaded successfully or not
                time.sleep(300)
                print("pfu enabled \n")
                break
        else:
                set_pfu_enable()
                #Here need to check whether SC,MC,CPLD are loaded successfully or not
                time.sleep(300)
                print("pfu enabled \n")
                break
        i = i+1


