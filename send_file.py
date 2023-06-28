import bluetooth

def send_file(file_path, target_device_address):
    # Establish a Bluetooth socket connection
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    try:
        # Connect to the target Bluetooth device
        socket.connect((target_device_address, 1))
        print("Connected to the target device.")

        # Open the file for reading
        with open(file_path, 'rb') as file:
            # Read the file in chunks
            chunk = file.read(1024)

            # Send file data in chunks
            while chunk:
                socket.send(chunk)
                chunk = file.read(1024)

        print("File sent successfully.")

    except bluetooth.btcommon.BluetoothError as error:
        print(f"Bluetooth connection error: {error}")

    finally:
        # Close the Bluetooth socket
        socket.close()

# Usage example
file_path = "path/to/your/file.txt"  # Replace with the actual file path
target_device_address = "XX:XX:XX:XX:XX:XX"  # Replace with the target device's Bluetooth address

send_file(file_path, target_device_address)
