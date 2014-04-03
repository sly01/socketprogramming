from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#klavyeden veri al
message = raw_input("Input lowercase sentence:")
clientSocket.send(message)
#soketten cevap mesajini oku
modifiedMessage = clientSocket.recvfrom(1024)
#mesaji ekrana bas ve soketi kapat
print 'From Server: ', modifiedMessage

clientSocket.close()
