#This program will load license through ftp.
# Here "put <filename.txt> license" is copying the file "filename.txt" as "license" in ftp. ("put sourcefile destfile"  is the syntax)
#'STOR license', license is the destinationfile and in Dothill ftp it is license 
#opening the license file using open function

import ftplib
import time
import os
import datetime
import sys
import Read_JSON
import Telnet_Login

ftp = ftplib.FTP(Read_JSON.get_controller_A_IP(),Read_JSON.getUserName(),Read_JSON.getPassword())
ftp.storbinary('STOR license', open('C:\Users\kanchana\Desktop\certificate.txt', 'rb')) # Give file path from json
 tm=Telnet_Login.login_A()	
        tm.write(b" set cli-parameters pager off \n")


