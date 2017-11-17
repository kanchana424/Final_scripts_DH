info =[]

file = open("C:\python3.6\Final scripts\Firmware\README-GL220P009-15.txt","r+") #This file name/path should come from json
content = file.readlines()
#print(content)
for item in content:
    if "Storage Controller:" in item:
        item =item.strip()
        info.append(item)
    if "Management Controller:" in item:
        item =item.strip()
        info.append(item)
    if "CPLD(348):" in item:
        item =item.strip()
        info.append(item)
#print(info)
#for i in range(len(info)):
SC =info[0].split(":")
SC =SC[1].strip()
SC = SC.split(" ")
print(SC[0])

MC =info[1].split(":")
MC =MC[1].strip()
MC = MC.split(" ")
print(MC[0])


CPLD =info[2].split(":")
CPLD =CPLD[1].strip()
CPLD = CPLD.split(" ")
print(CPLD[0])


'''
SC_ver = SC[1].strip()
#SC_ver = SC_ver[1].split(" ")
#SC_ver = SC_ver[0].strip()
print(SC_ver)
#if ":" in SC:
   

for i in range(len(info)): #-12 is to remove all values after pfu status till "success: message" from list
       if ":" in info[i]: # To check every line has : in it for key and value
           k,v= info[i].split(":") #split : and 1 , 1 is to split after 1 item when : appears
           my_dic[k]=v
#print(my_dic)
#my_dic =my_dic.values()
#print(my_dic)


#print(my_dic.items().strip())
#print(my_dic.keys())
#print(my_dic.values())
#SC = my_dic["Storage Controller"].strip() # Strip is to remove whitespaces before and after string
#print(SC)

    Product_ID = my_dic["Product ID"].strip()
    Health = my_dic["Health"].strip()
    return(Vendor_Name,Product_ID,Health) # Need to return dic or list instead of multiple values

#Vendor_Name,Product_ID,Health=show_system()
#print(Vendor_Name)
#print(Product_ID)
#print(Health)

'''
