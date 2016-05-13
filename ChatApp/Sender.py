# Main program

from socket import *
import Utils as Util
import time

host = "192.168.0.18"
port = 6666
buf = 1024
addr = (host, port)
# End Socket Parameters Dynamically
# Create socket and bind to address
UDPSock = socket(AF_INET, SOCK_DGRAM)

remote_host = "192.168.0.27"
remote_port = 6666

remote_addr = (remote_host, remote_port)

# SessionKey = Util.sessionKeyControl("77F04F43B", UDPSock, remote_addr)

# if SessionKey != None:
print("Ready to Chat! Type #HELP for manual.")
print("#To send file => #FILE <path> ")
print ("#To send text message, enter the desired text directly.")

while 1:
    # Send Message
    user_input = input('>> ')
    if "#HELP" in user_input:
        Util.Help()
        continue
    elif "#FILE" in user_input:
        Util.Send_File(UDPSock, remote_addr, user_input[5:].strip())
    elif "#AUTH" in user_input:
        Util.Send_AuthMessage(UDPSock,remote_addr)
    elif "#ROUT" in user_input:
        Util.Send_RoutingTable(UDPSock,remote_addr)
    elif user_input:
        Util.SendMessage(UDPSock, user_input, remote_addr)
        # else:
        # print "Session has not been established!"
