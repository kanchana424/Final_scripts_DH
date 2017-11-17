import json
import ipaddress

data = open('C:\python3.6\Final scripts\Login_details.json','r').read()
#FTP_LOGIN = json.loads(data)
My_dic =json.loads(data)

first_index = 0

def get_controller_A_IP():
    hostA = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'controller_A_IP')][first_index]    
    return hostA

def get_controller_B_IP():
    hostB = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'controller_B_IP')][first_index]    
    return hostB

def getUserName():
    username = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'username')][first_index]    
    return username

def getPassword():
    password = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'password')][first_index]    
    return password

def getIterations():
    iter_count = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'iter')][first_index]    
    return iter_count

def getUpgradeVer():
    upver = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'Upgrade_Version')][first_index]    
    return upver

def getDowngradeVer():
    downver = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'Downgrade_Version')][first_index]    
    return downver

def getFW_up_down_count():
    pfu_count = [My_dic.get(var1).get(key) for var1 in My_dic for key in My_dic.get(var1) if(key == 'PFU_count')][first_index]    
    return pfu_count


'''
def get_upVER():
    up_ver = [My_dic.get(var1).get(key) for var1 in My_dic if(var1=='Firmware_Upgrade') for key in My_dic.get(var1) if(key == 'Upgrade_Version')][first_index]    
    return up_ver

def get_downVER():
   down_ver = [My_dic.get(var1).get(key) for var1 in My_dic if(var1=='Firmware_Downgrade') for key in My_dic.get(var1) if(key == 'Downgrade_Version')][first_index]    
   return down_ver


def get_controller_A_IP():
    controller_A_IP = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'controller_A_IP')]    
    return controller_A_IP[first_index]

def get_controller_B_IP():
    hostB_list = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'controller_B_IP')]    
    return hostB_list

def getUserName():
    username = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'username')]    
    return username[first_index]
    
def getPassword():
    password = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'password')]    
    return password[first_index]

def getIterations():
   iter_count = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'iter')]    
   return iter_count[first_index]

def getFW_up_down_count():
    PFU_count = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'PFU_count')]    
    return PFU_count[first_index]

def getDowngradeVer():
   Down_ver = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'Upgrade_Version')]    
   return Down_ver[first_index]

def getUpgradeVer():
   Up_ver = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'Downgrade_Version')]    
   return Up_ver[first_index]


def get_controller_A_IP():
    controller_A_IP = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'controller_A_IP')]
    IP_A = controller_A_IP[first_index]
    #print(type(IP_A))
    while True:
        try:
            IP_A=ipaddress.ip_address(IP_A)
            #print(IP_A)
            break
        except ValueError:
            IP_A=input("Enter a valid IP address: \n")
               
    return str(IP_A)

'''
