import socket
import os

# host to listen on 
host = "192.168.1.2"

# create a raw socket and bind it to the public interface 
if os.name=="nt":
    socket_protocol=socket.IPPROTO_IP
else:
    socket_protocol=socket.IPPROTO_ICMP 

sniffer=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# we want the ip headers included in the capture 
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# if were using Windows, we need to send an IOCTL
# to set up permiscuous mode 
if os.name=="nt":
    sniffer.ioctl(socket.SIO_RCVLL, socket.RCVALL_ON)
print sniffer.recvfrom(65565)

if os.name =="nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
