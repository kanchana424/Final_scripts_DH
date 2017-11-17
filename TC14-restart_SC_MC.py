import time
from pprint import pprint
import ftplib
import Telnet_Login
import sys
import Read_JSON


def shutdown_restart_SC():
        tm=Telnet_Login.login_A()	
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        print("Shutdown \n")
        tm.write(b" shutdown \n")
        time.sleep(20)
        print("restart \n")
        tm.write(b" restart sc \n")
        time.sleep(20)
        #data = tm.read_very_eager()
        #print(data)
        #file = open("C:\python3.6\Final scripts\Logs\TC14-restart_SC_MC.txt", "a+").write(data)
        time.sleep(20)
        tm=Telnet_Login.login_B()
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        print("Shutdown \n")
        tm.write(b" shutdown \n")
        time.sleep(20)
        print("restart \n")
        tm.write(b" restart sc \n")
        #data = tm.read_very_eager()
        #file = open("C:\python3.6\Final scripts\Logs\TC14-restart_SC_MC.txt", "a+").write(data)
        
      		
def restart_MC():
        tm=Telnet_Login.login_A()	
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        print("restart \n")
        tm.write(b" restart mc \n")
        time.sleep(20)
        #data = tm.read_very_eager()
        #file = open("C:\python3.6\Final scripts\Logs\TC14-restart_SC_MC.txt", "a+").write(data)
        time.sleep(20)
        tm=Telnet_Login.login_B()
        tm.write(b" set cli-parameters pager off \n")
        tm.write(b" set cli-parameters api \n")
        print("restart \n")
        tm.write(b" restart mc \n")
        time.sleep(20)
        #data = tm.read_very_eager()
        #file = open("C:\python3.6\Final scripts\Logs\TC14-restart_SC_MC.txt", "a+").write(data)

shutdown_restart_SC()
restart_MC()

