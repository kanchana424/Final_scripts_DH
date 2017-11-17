import time
from pprint import pprint
import ftplib
import Telnet_Login
import sys
import Versions_details
import Read_JSON

i =0
def create_snap_snaps():
        tm=Telnet_Login.login()	
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        tm.write(b" create vdisk  \n")
		tm.write(b" create volume  \n")
		tm.write(b" create snapshot  \n")
		if i <128:
			tm.write(b" create snapshot  \n")
        time.sleep(3)
        tm.write(b" exit \n")
        data=tm.read_all().decode('UTF-8')
        time.sleep(5)
        file = open("C:\python3.6\Final scripts\Logs\TC15-Snap_of_snaps.txt", "a+").write(data)
        
        
        tm.close()
                
