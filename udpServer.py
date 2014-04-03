from socket import *
serverName = 'localhost'
serverPort = 12000
#Udp socket olustur
serverSocket = socket(AF_INET, SOCK_DGRAM)
#socketi localhost a bagla
serverSocket.bind((serverName,serverPort))

print "The server is ready to receive"

while 1:
	#Client adres bilgisi ve Port numarasini mesajla birlikte al
	mesaj, clientAddress = serverSocket.recvfrom(2048)
	print mesaj
	#Buyuk harfe cevir ve geri gonder
	modifiedMessage = mesaj.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)