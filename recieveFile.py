import socket
s = socket.socket()
host = "LAPTOP-MEGPB18A"
port = 8080
s.connect((host,port))
print("Connected...")
filename = "graph.pm3"
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")
