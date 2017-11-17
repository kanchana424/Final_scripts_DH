import Telnet_Login
import time
from pprint import pprint
import sys
#import FTP_Download_Logs

def protocols_enabled_disabled():
    tm=Telnet_Login.login_A()
    tm.write(b" set cli-parameters pager off \n")
    tm.write(b" set cli-parameters api \n")
    tm.write(b" set protocols http enabled https enabled ssh enabled smis enabled usmis disabled ftp enabled snmp enabled debug enabled ses enabled activity enabled management-mode v2 \n")
    #Need to check return code from xml output continue if it is 0 , exit if other
    time.sleep(1)
    #tm.write(b" show protocols \n")
    #Need to check the values set to each parameter from xml, if it is different exit else continue
    tm.write(b"  set protocols http disabled https disabled ssh disabled smis disabled usmis enabled ftp disabled snmp disabled debug disabled ses disabled activity disabled management-mode v3 \n")
    #Need to check return code from xml output continue if it is 0 , exit if other
    time.sleep(1)
    #tm.write(b" show protocols \n")
    #Need to check the values set to each parameter from xml, if it is different exit else continue
    time.sleep(1)
    tm.write(b" set protocols http enabled https enabled ssh enabled smis enabled usmis disabled ftp enabled snmp enabled debug enabled ses enabled activity enabled management-mode v2 \n")
    tm.write((" exit \n").encode('ascii'))
    time.sleep(30)                 	        
    data=tm.read_all().decode('UTF-8')	        
    file = open("C:\python3.6\Final scripts\Logs\TC6-protocols.txt", "a").write(data)
    tm.close()

protocols_enabled_disabled()



#FTP_Download_Logs.FTP_Logs("TC6") 


