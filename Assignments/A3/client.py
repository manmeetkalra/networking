#! /usr/bin/python

import socket
import time

host = 'winter'
port = 12345

s = socket.socket() #create socket (Default is TCP)

s.connect((host, port)) #connect to host on specified port

s.send('Hello ' + host + '!' + ' I am ' + socket.gethostname() + '.')
print 'MESSAGE: ' + s.recv(512) #print TCP msg received
time.sleep(1)

s.close() #close connection
