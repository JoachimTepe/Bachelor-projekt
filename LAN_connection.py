import socket
# Adding a transfer speed that ensures the whole file can be sent in a single TCP packet
transfer_speed = 32768

port = 8080
s = socket.socket()
host = "LAPTOP-MEGPB18A"
filename = "graph.pm3"


def receive_file():
    s.connect((host, port))
    print("Connected...")
    file = open(filename, 'wb')
    file_data = s.recv(transfer_speed)
    file.write(file_data)
    file.close()
    print("File has been received successfully.")


def setup():
    s.bind((host, port))
    s.listen(1)
    print("Waiting for any incoming connections ...")
    connection, address = s.accept()
    print(address, "Has connected to this laptop")
    return connection


def send_file(connection):
    file = open(filename, 'rb')
    file_data = file.read(transfer_speed)
    connection.send(file_data)
    print("File has been transmitted successfully.")
