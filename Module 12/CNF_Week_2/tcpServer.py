import socket
import threading
from _thread import *
import csv
def Main():
	host = '10.1.135.147'
	port = 2148
	s=socket.socket()
	s.bind((host, port))


if __name__ == '__main__':
	with open('data.csv','r') as csvFile:
		reader=csv.reader(csvFile)
		for row in reader:
			#print (row)
			a = row[0]
			b = row[1]
			c = row[2]
			#print (a)



