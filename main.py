import sys
import time
import Telnet_Login
import FTP_Download_Logs
import System_details
import Versions_details

#Calling system information from "System_details" file
Vendor_Name,Product_ID,Health=System_details.show_system()
print("Vendor_Name: ",Vendor_Name)
print("Product_ID: ",Product_ID)
print("Health: ",Health)
#Calling Version details from "Versions_details" file
cntrlA_ver,cntrlB_ver = show_versions()
print(cntrlA_ver)
print(cntrlB_ver)




