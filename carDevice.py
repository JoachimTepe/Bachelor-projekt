import LAN_connection
import USB_connection
import proxmark3

wireless_conn = False

# Setting up LAN connection before sniffing
if wireless_conn:
    LAN_conn = LAN_connection.setup()

# Running the sniffing command on the proxmark3.
proxmark3.run_sniff_cmd()

# Sending the saved pm3 file to the other device
if wireless_conn:
    LAN_connection.send_file(LAN_conn)
else:
    USB_connection.send_file()
