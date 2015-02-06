#import socket module
import socket                                 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Prepare a sever socket

#usr = socket.gethostbyname(socket.gethostname())

serverSocket.bind(('localhost',1234))


while True:
    #Establish the connection

	print 'Ready to serve...'
	serverSocket.listen(2)
	connectionSocket, addr = serverSocket.accept()         
	try:
		message = connectionSocket.recv(2048)        		
		filename = message.split()[1]
		filename = filename.lstrip("/")		
		print filename                 
		f = open(filename)                        
		outputdata = f.readlines()
		f.close()
		
		                  
       
       #Send one HTTP header line into socket
		connectionSocket.send("HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n") 
      

               
        #Send the content of the requested file to the client
		for i in range(0, len(outputdata)):           
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
		
	except IOError:
  
#Send response message for file not found
		
		          
			connectionSocket.send("ERROR YOU BROKE IT !")
			connectionSocket.close()
			serverSocket.close()
			exit()
        #Close client socket
	connectionSocket.close()
	serverSocket.close()
	exit()
	
