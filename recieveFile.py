import socket

def receive_file(save_path):
    # Create a Bluetooth socket
    server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    # Bind the server socket to any available port
    server_socket.bind(("", 1))

    # Listen for incoming connections
    server_socket.listen(1)

    # Accept the connection from the sender device
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from", client_address)

    # Receive the file contents and save it
    with open(save_path, "wb") as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    # Close the sockets
    client_socket.close()
    server_socket.close()
    print("File received successfully.")

# Specify the save path for the received file
save_path = "received_file.txt"

# Call the receive_file function
receive_file(save_path)