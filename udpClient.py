from socket import *

serverName = 'localhost'
serverPort = 12000
#udp soket olustur
clientSocket = socket(AF_INET,SOCK_DGRAM)
while 1:
	#klavyeden veri al
	message = raw_input("Input lowercase sentence:")
	#sunucu ismi ve port numarisi ekle gonder
	clientSocket.sendto(message,(serverName,serverPort))
	#soketten cevap mesajini oku
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	#mesaji ekrana bas ve soketi kapat
	print modifiedMessage

clientSocket.close()
