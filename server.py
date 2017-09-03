import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
   conn, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   try:
      with open('received_file.png', 'wb') as f:
         print 'file opened'
         while True:
            print('receiving data...')
            data = conn.recv(40960000)
            # print('data=%s', (data))
            if not data:
               break
            # write data to a file
            f.write(data)

      f.close()
      print('Successfully get the file')
   except:
      conn.close()
      print('connection closed')
      continue
