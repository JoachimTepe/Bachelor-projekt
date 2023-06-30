import connection
import proxmark3

# Connecting and saving pm3 file
connection.receive_file()

# # Running the simulation command on the proxmark3.
proxmark3.run_sim_cmd()

