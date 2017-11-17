import Telnet_Login
import time
from pprint import pprint
import sys
import FTP_Download_Logs
import Read_JSON



def create_delete_user():
    tm1=Telnet_Login.login_A()
    tm.write(b" set cli-parameters pager off \n")
    tm.write(b" set cli-parameters api \n")
    tm.write(b" create user interfaces cli,wbi roles manage user1 password User@12345 \n")
    tm.write(b" delete user user1 \n")
    tm.write(b" create user interfaces snmpuser password User@12345 authentication-type SHA privacy-type AES privacy-password User@12345 User_Snmp \n")
    tm.write(b" delete user User_Snmp \n")
    tm.write(b" exit \n")
    time.sleep(3)                 	        
    data=tm.read_all().decode('UTF-8')
    file = open("C:\python3.6\Final scripts\Logs\TC12-create_delete_User.txt", "a+")
    file.write("Created a manage and snmp v3 user and deleted the users \n")
    file.write(data)
    tm.close()
               
create_delete_user()
FTP_Download_Logs.FTP_Logs("TC12") 

	
