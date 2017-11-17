#This function defines login and logout of telnet for 10 times


import Telnet_Login
import time
from pprint import pprint
import sys
import FTP_Download_Logs
import Read_JSON

i =1
def Login_Logout():
    tm1=Telnet_Login.login_A()
    tm1.write(b" show vdisks \n")
    tm1.write(b" exit \n")
    time.sleep(3)                 	        
    data=tm1.read_all().decode('UTF-8')
    file = open("C:\python3.6\Final scripts\Logs\TC1-login_logout.txt", "a+")
    file.write("*************Login_Logout function is executing for "+str(i)+" time *************\n")
    file.write(data)
    tm1.close()
               
    
count =Read_JSON.getIterations()

while (i<=int(count)):
	Login_Logout()
	print("logging to controller for count:%d" %i)
	i=i+1

FTP_Download_Logs.FTP_Logs("TC1") 

	
