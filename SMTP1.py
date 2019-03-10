from socket import * 

msg = "\r\n My name is Ray(Yanrui) Li. My student number is 52591120. I love computer networks!" 
endmsg = "\r\n.\r\n" 
 
# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = "esva.mail-relay.ubc.ca", 25
 
# Create socket called clientSocket and establish a TCP connection with mailserver 
# Fill in start     
clientSocket= socket(AF_INET, SOCK_STREAM) 
clientSocket.connect(mailserver)
#sentence = raw_input('Input lowercase sentence: ') 
# Fill in end 
recv = clientSocket.recv(1024).decode() 
print(recv) 
if recv[:3] != '220':  
    print('220 reply not received from server.') 
 
# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode()) 
recv1 = clientSocket.recv(1024).decode() 
print('Received from server:' + recv1) 
if recv1[:3] != '250':     
    print('250 reply not received from server.') 
    
# Send MAIL FROM command and print server response. 
# Fill in start
clientSocket.send('MAIL FROM: <yanrayli@gmail.com>\r\n'.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print ('From:' + recv2)
if recv2[:3] != '250': #if the data is not received
	print ('250 reply not received from server.')
# Fill in end 
 
# Send RCPT TO command and print server response.  
# Fill in start 
clientSocket.send('RCPT TO: yanruii@alumni.ubc.ca> \r\n'.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print ('To:' + recv3)
if recv3[:3] != '250':
	print ('250 reply not received from server.')
# Fill in end 
 
# Send DATA command and print server response.  
# Fill in start  
clientSocket.send('DATA\r\n'.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print (recv4)
if recv4[:3] != '354':
	print ('250 reply not received from server.')
# Fill in end 
 
# Send message data. 
# Fill in start 
clientSocket.send(msg.encode()) 
# Fill in end 

# Message ends with a single period. 
# Fill in start 
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print ("Response after sending message body:"+recv_msg.decode())
if recv_msg[:3] != '250':
	print ('250 reply not received from server.')
# Fill in end 
 
# Send QUIT command and get server response. 
# Fill in start 
clientSocket.send('QUIT\r\n')
clientSocket.close()
# Fill in end 