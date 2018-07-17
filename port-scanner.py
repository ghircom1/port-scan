import socket
import os
import sys
url=raw_input("enter the url: ")
ip=socket.gethostbyname(url)
print("-"*60)
print("scan ip",ip)
print("-"*60)
try:
    for port in range(1,100):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        nati=sock.connect_ex((ip,port))
        if nati==0:
            print("port {} :     open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("error")
    sys.exit(0)
except socket.gaierror:
    print("error")
    sys.exit(0)
except socket.error:
    print("error")
    sys.exit()
