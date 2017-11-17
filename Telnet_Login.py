import sys
import telnetlib
import time
from pprint import pprint
import Read_JSON

def login_A():
	#tm=telnetlib.Telnet(Read_JSON.get_controller_A_IP(),23,10)
        ip_str = Read_JSON.get_controller_A_IP()
        #print(type(ip_str))
        tm=telnetlib.Telnet(ip_str,23,10)
        tm.read_until(b"login: ")
        tm.write(Read_JSON.getUserName().encode('UTF-8') + b"\n")
	#if cmds["FTP_LOGIN"]["password"]:
        tm.read_until(b"Password: ")
        tm.write(Read_JSON.getPassword().encode('UTF-8') + b"\n")
        return(tm)

def login_B():
	tm=telnetlib.Telnet(Read_JSON.get_controller_B_IP(),23,10)
	tm.read_until(b"login: ")
	tm.write(Read_JSON.getUserName().encode('UTF-8') + b"\n")
	#if cmds["FTP_LOGIN"]["password"]:
	tm.read_until(b"Password: ")
	tm.write(Read_JSON.getPassword().encode('UTF-8') + b"\n")
	return(tm)

