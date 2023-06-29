import connection
import proxmark3
import datetime
curr_time = datetime.datetime.now().time()

# Connecting and saving pm3 file
connection.receive_file()

# # Running the simulation command on the proxmark3.
print("pre simulation" + str(curr_time.hour), curr_time.minute, curr_time.second)
proxmark3.run_sim_cmd()

