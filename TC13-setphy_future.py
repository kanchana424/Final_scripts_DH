import time
from pprint import pprint
import ftplib
import Telnet_Login
import sys
import Versions_details
import Read_JSON

i =0
def set_phy(): # Create vdisk, vol, map, disable a drive, add spare, wait till recons, Io should not stop, No crash
        tm=Telnet_Login.login()	
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        tm.write(b" delete vdisks all \n") # Check 
		tm.write(b" create vdisk level r5 disks {} vd0001  \n")
		#create volume map and run IO
		tm.write(b" set phy   \n") # To disable a drive from telnet
		#add a spare, wait till vdisk completes reconstruction
		time.sleep(3)
        tm.write(b" exit \n")
        data=tm.read_all().decode('UTF-8')
        time.sleep(5)
        file = open("C:\python3.6\Final scripts\Logs\TC13_setphy.txt", "a+").write(data)
        
        tm.close()
                
