#This program will create a folder with current time stamp in the location from where the program is running .
#FTP logs will be downloaded to the folder with current time stamp.
#To run this script continously for every 15min or 30min or 1hr, create a jenkins job.

#This program will create a folder with current time stamp in the location from where the program is running .
#FTP logs will be downloaded to the folder with current time stamp.
#To run this script continously for every 15min or 30min or 1hr, create a jenkins job.

import ftplib
import time
import os
import datetime
import sys
import Read_JSON

def FTP_Logs(TC_no):
    date = datetime.datetime.now()
    strdate = date.strftime('%Y-%m-%d_%H-%M-%S')
    filename = TC_no + "_" + strdate
    os.chdir('Logs')
    os.mkdir(filename)
    os.chdir(filename)
    ftp = ftplib.FTP(Read_JSON.get_controller_A_IP(),Read_JSON.getUserName(),Read_JSON.getPassword())
    ftp.retrbinary('RETR logs', open(filename + "_" +'CntrlA.zip', 'wb').write)




    

