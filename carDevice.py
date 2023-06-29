import connection
import proxmark3
import datetime

curr_time = datetime.datetime.now().time()


print(curr_time.hour, curr_time.minute, curr_time.second)

# Setting up connection before sniffing
conn = connection.setup()

print("Pre sniffing" + str(curr_time.hour), curr_time.minute, curr_time.second)

# Running the sniffing command on the proxmark3.
proxmark3.run_sniff_cmd()

print("post sniffing" + str(curr_time.hour), curr_time.minute, curr_time.second)

# Sending the saved pm3 file to the other device
connection.send_file(conn)
