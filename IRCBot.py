import socket
       
server = "irc.freenode.net" # Server
channel = "#lug-nitk" # Channel
botnickname = "PNPBot" # Your bots nick


def ping(): 
  sock.send("PONG :pingis\n")  

def sendmsg(chan , msg):
  sock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def join_channel(chan): 
  sock.send("JOIN "+ chan +"\n")

def initialhello(): 
  sock.send("PRIVMSG "+ chan +" :Hello!\n")
                  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, 6667)) # Here we connect to the server using the port 6667
sock.send("USER "+ botnickname +" "+ botnickname +" "+ botnickname+"This is pnpninja\'s bot\n") # user authentication
sock.send("NICK "+ botnickname +"\n") # here we actually assign the nick to the bot

join_channel(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
   msg = ircsock.recv(2048) # receive data from the server
   msg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
   print(ircmsg) # Here we print what's coming from the server
   if msg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
      sock.send("PRIVMSG "+ channel +" :Hello! I am PNPNinja's Bot\n")
   if msg.find("PING :") != -1: # if the server pings us then we've got to respond!
      sock.send("PONG :pingis\n") 