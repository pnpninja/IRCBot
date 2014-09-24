#To do - 
#1 - Handle Private chats and Channel Chats
#2 - More text processing of message to give a personal touch to messages

import socket

server = "irc.freenode.net" #server name
channel = "#lug-nitk" #channel name
botnick = "PNPBot" #nickname

def join_channel(chan):
  sock.send("JOIN "+ chan +"\n")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
sock.connect((server, 6667)) #connect to the IRC server
sock.send("USER "+ botnick +" "+ botnick +" "+ botnick+"This is pnpninja\'s bot\n") #set user details
sock.send("NICK "+ botnick +"\n") #set nickname

join_channel(channel)

while 1:
   msg = sock.recv(2048)
   msg = msg.strip('\n\r')
   print(msg)
   if msg.find(":Hello "+ botnick) != -1:
      sock.send("PRIVMSG "+ channel +" :Hello!\n")
   if msg.find("PING :") != -1:
      sock.send("PONG :pingis\n") 