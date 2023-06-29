import connection
import proxmark3

# Setting up connection before sniffing
conn = connection.setup()

# Running the sniffing command on the proxmark3.
proxmark3.run_sniff_cmd()

# Sending "graph.pm3" to the other device
connection.send_file(conn)
