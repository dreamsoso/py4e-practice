import socket
import re

target_url = input("Enter URL:")
#HOST = re.findall('(^http[s+]://)',target_url)
HOST = re.findall("http[s]?://(.+)",target_url)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((HOST[0], 80))
    mysock.close()
except:
    print("socket connect fail!\n")
