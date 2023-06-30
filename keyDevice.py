import LAN_connection
import USB_connection
import proxmark3

wireless_conn = False

# Connecting and saving pm3 file using a Local Area Network connection
if wireless_conn:
    LAN_connection.receive_file()
else:
    USB_connection.receive_file()

# # Running the simulation command on the proxmark3.
proxmark3.run_sim_cmd()

