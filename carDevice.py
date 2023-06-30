import connection
import proxmark3
import datetime

curr_time = datetime.datetime.now().time()

# Setting up connection before sniffing
conn = connection.setup()

# Running the sniffing command on the proxmark3.
proxmark3.run_sniff_cmd()

# Sending the saved pm3 file to the other device
connection.send_file(conn)
