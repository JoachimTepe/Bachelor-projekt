import serial

filename = "graph.pm3"
baud_rate = 115200


def send_file():
    # Open the serial port
    serial_port = "COM3"
    ser = serial.Serial(serial_port, baud_rate)

    # Read the file
    with open(filename, 'rb') as file:
        data = file.read()

    # Send the file data
    ser.write(data)

    # Close the serial port
    ser.close()


def receive_file():
    # Open the serial port
    serial_port = "COM3"
    ser = serial.Serial(serial_port, baud_rate)

    # Receive the file data
    data = ser.read_all()

    # Write the received data to a file
    with open(filename, 'wb') as file:
        file.write(data)

    # Close the serial port
    ser.close()

