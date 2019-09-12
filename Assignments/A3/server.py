#! /usr/bin/python

# RUN THIS SCRIPT ON WINTER!

import socket

host = 'winter'
port = 12345

s = socket.socket() #create socket (Default is TCP)
s.bind(('', port)) #bind socket ('' refers to localhost)

s.listen(5) #TCP listener (5 is the max number of queued connections at a time)

print 'Keyboard Interrupt to Quit!'
print 'Server running on port ' + str(port) + '...'

while 1:
	conn, addr = s.accept() #accept new connection
	print 'Client ' + addr[0] + ' connected!'
	print 'MESSAGE: ' + conn.recv(512)
	conn.send('You are connected to ' + host + '.')
	conn.close() #close connection
