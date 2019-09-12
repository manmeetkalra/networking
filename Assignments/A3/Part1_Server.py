#! /usr/bin/python

#Importing a socket library
import socket

#Using winter as our host and reserving a port for the connection
host = 'april'
port = 24925

#Creating a socket object
s = socket.socket()

#Bind Socket to the port and have empty string for the ip address making server
#listen to incoming connection from other computers
s.bind(('', port))

#The socket is listening and 5 her means that teh max number of pending connections for the socket
s.listen(5)

while 1:
	#Establishing connection with the client
	conn, addr = s.accept()
	print 'Client ' + addr[0] + ' connected!' #Printing the message that client is connected
	print 'MESSAGE: ' + conn.recv(512) #Print the message received from client
	conn.send('You are connected to server ' + host + '.') #Send a message to client
	conn.close() #close connection
