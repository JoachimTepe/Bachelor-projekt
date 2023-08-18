import LAN_connection
import proxmark3

# Setting up LAN connection before sniffing
LAN_conn = LAN_connection.setup()

# Running the sniffing command on the proxmark3.
proxmark3.run_sniff_cmd()

# Sending the saved pm3 file to the other device
LAN_connection.send_file(LAN_conn)

# Deleting the file containing the pm3 sniff on Host A
proxmark3.delete_file()

