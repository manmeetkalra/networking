#Client side

#! /usr/bin/python

#Importing a socket module
import socket
import time

#Using winter as our host and reserving a port for the connection
host = 'april'
port = 24925

#creating a socket object
s = socket.socket()

#Connecting to the specified host and port as mentioned above
s.connect((host, port))

#Send (write) data to the connection
s.send('Hello server ' + host + '!' + ' I am client ' + socket.gethostname() + '.')

#Printing the message received from the server
print 'MESSAGE: ' + s.recv(512)
time.sleep(1)

#Closing connection
s.close()
