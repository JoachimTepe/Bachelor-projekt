import socket

# Adding a transfer speed that ensures the whole file can be sent in a single TCP packet
transfer_speed = 32768

# Using tcp port
port = 8080
# Create a socket object
s = socket.socket()
# Define the host (target device) and file name
host = "LAPTOP-MEGPB18A"
file_name = "graph.pm3"


def receive_file():
    # Connect to the host and port
    s.connect((host, port))
    print("Connected...")

    # Open the file in write-binary mode
    file = open(file_name, 'wb')

    # Receive data from the socket
    file_data = s.recv(transfer_speed)

    # Write the received data to the file
    file.write(file_data)
    file.close()
    print("File has been received successfully.")


def setup():
    # Bind the socket to the host and port
    s.bind((host, port))

    # Listen for incoming connections with a maximum queue size of 1
    s.listen(1)
    print("Waiting for any incoming connections ...")

    # Accepts any connection
    connection, address = s.accept()
    print(address, "Has connected to this laptop")
    return connection


def send_file(connection):
    # Open the file in read-binary mode
    file = open(file_name, 'rb')

    # Read the data from the file
    file_data = file.read(transfer_speed)

    # Send the data through the connection
    connection.send(file_data)
    print("File has been transmitted successfully.")

