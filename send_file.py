import socket

target_address = "e4:70:b8:0c:f2:a5"  # Bluetooth address of the receiver device
port = 3  # Port number for the Bluetooth connection
pm3file = "graph.pm3"

# Create a Bluetooth socket
socket_obj = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Connect to the receiver device
socket_obj.connect((target_address, port))

# Read and send the file data
with open(pm3file, "rb") as file:
    chunk = file.read(1024)
    while chunk:
        socket_obj.send(chunk)
        chunk = file.read(1024)

# Close the connection
socket_obj.close()
