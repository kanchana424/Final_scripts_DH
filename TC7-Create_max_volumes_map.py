import time
from pprint import pprint
import ftplib
import Telnet_Login
import sys
import Versions_details
import Read_JSON

def set_pfu_disable():
        tm=Telnet_Login.login()	
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        tm.write(b" set advanced-settings partner-firmware-upgrade disabled  \n")
        time.sleep(3)#Need to add code to verify whether PFU is disabled or not, check xml	
        tm.write(b" exit \n")
        data=tm.read_all().decode('UTF-8')
        time.sleep(5)
        file = open("C:\python3.6\Final scripts\Logs\TC10-FTP_Upgrade_Downgrade.txt", "a+")
        file.write("*************PFU DISABLED for "+str(i)+" time *************\n")
        file.write(data)
