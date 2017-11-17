#This program will first list all vdisks in the system, collect vdisk names and delete all vdisks
#Prompt here is hardcoded.


import Telnet_Login
import time
from pprint import pprint
import sys
import FTP_Download_Logs
import Read_JSON

#This program is depended on the create_vdisk funcrtion
def delete_vdisk():
  tm=Telnet_Login.login_A()
  tm.write(b" set cli-parameters pager off \n")
  tm.write(b" show vdisks \n")
  tm.write(b" set cli-parameters api \n")
  vdisks = []
  values = []
  tm.write(b" exit \n") # Need to check how to proceed without existing from telnet
  time.sleep(10)      
  data = tm.read_all().decode('UTF-8')
  file = open("C:\python3.6\Final scripts\Logs\pvdisks.txt", "w+").write(data) # What if there are 2 outputs of show vdisks in text file how it will be handled
  file = open("C:\python3.6\Sanity_Testcases\Logs\pvdisks.txt", "r")
  #Need column wise data collection code here 










	
