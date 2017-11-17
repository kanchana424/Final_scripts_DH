import Telnet_Login
import time
from pprint import pprint
import sys
import FTP_Download_Logs
import Read_JSON

my_list=[]
my_dic={}
k =""
v = ""  

def show_protocols():
    tm=Telnet_Login.login_A()
    tm.write(b" set cli-parameters pager off \n")
    tm.write(b" show protocols \n")
    tm.write(b" exit \n")
    data=tm.read_all().decode('ascii')
    time.sleep(10)
    file = open("C:\python3.6\Final scripts\Logs\show_protocols.txt", "w+").write(data)
    file = open("C:\python3.6\Final scripts\Logs\show_protocols.txt", "r+")
    content = file.readlines()
    #print(content)
    ind = content.index('------------------------------\n')+1 
    for ind in content[ind:-3]:
        my_list.append(ind[:-1]) #:-1 to remove new line chracter
    #print(my_list)
    for i in range(len(my_list)-6): #-6 is to remove all values after v2/v3 status till "success: message" from list
        if ":" in my_list[i]: # To check every line has : in it for key and value
           k,v= my_list[i].split(":",1) #split : and 1 , 1 is to split after 1 item when : appears
           my_dic[k]=v
    print(my_dic) # Here take only HTTP like that
    #print(my_dic.items())
    #print(my_dic.keys())
    #print(my_dic.values())
    #HTTP = my_dic["Web Browser Interface (HTTP)"].strip() # Strip is to remove whitespaces before and after string
    #SNMP = my_dic["Simple Network Management Protocol (SNMP)"].strip()
    #Vendor_Name,Product_ID,Health=show_system()
    #return(HTTP,SNMP) # Need to return a list instead of individual values
    
#HTTP,SNMP=show_protocols()
#print(HTTP)
#print(SNMP)
