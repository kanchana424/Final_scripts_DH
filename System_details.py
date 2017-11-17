# -*- coding: utf-8 -*-
import sys
import Telnet_Login
import time

my_list=[]
my_dic={}
k =""
v = ""  

def show_system():
    tm=Telnet_Login.login_A()
    tm.write(b" set cli-parameters pager off \n")
    tm.write(b" show system \n")
    tm.write(b" exit \n")
    data=tm.read_all().decode('ascii','ignore') #Generally we decode to string using UTF-8 but decode to ascii ie., bytes and keep ignore to all foreign characters or non ascii characters
    time.sleep(10)
    file = open("C:\python3.6\Final scripts\Logs\show_system.txt", "w+").write(data)
    file = open("C:\python3.6\Final scripts\Logs\show_system.txt", "r+")
    content = file.readlines()
    #print(content)
    ind = content.index('------------------\n')+1 #add 1 To iterate from next index. #This is to check the index of '---------' in the list and then take the values in indexs next to that
    for ind in content[ind:-3]:
        my_list.append(ind[:-1]) #:-1 to remove new line chracter
    #print(my_list)
    for i in range(len(my_list)-12): #-12 is to remove all values after pfu status till "success: message" from list
       if ":" in my_list[i]: # To check every line has : in it for key and value
           k,v= my_list[i].split(":",1) #split : and 1 , 1 is to split after 1 item when : appears
           my_dic[k]=v
    #print(my_dic)
    #print(my_dic.items())
    #print(my_dic.keys())
    #print(my_dic.values())
    Vendor_Name = my_dic["Vendor Name"].strip() # Strip is to remove whitespaces before and after string
    Product_ID = my_dic["Product ID"].strip()
    Health = my_dic["Health"].strip()
    return(Vendor_Name,Product_ID,Health) # Need to return dic or list instead of multiple values

#Vendor_Name,Product_ID,Health=show_system()
#print(Vendor_Name)
#print(Product_ID)
#print(Health)

