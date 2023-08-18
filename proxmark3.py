import os
import subprocess

file_name = "graph.pm3" # Just a generic name for the file.
length_of_signal = 5000 # Regular length of a LF RFID signal from the car is 3500


def run_command(_cmd):
    # Adding binaries for the os environment
    os.environ['PATH'] += os.pathsep + r"C:\working\ProxSpace\msys2\mingw64\bin"
    print("Running command: " + _cmd)
    process = subprocess.Popen(_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output)
    print(error)

    if process.returncode != 0:
        print(f'Error occurred: {error.decode().strip()}')
    else:
        print(f'Output: {output.decode().strip()}')


def run_sniff_cmd():
    proxmark3_path = "C:\\working\\ProxSpace\\pm3\\proxmark3\\client"
    cmd = f'{proxmark3_path}\\proxmark3 COM4 -c "lf config -t 20; lf sniff; data save -f {file_name}"'
    run_command(cmd)


def run_sim_cmd():
    proxmark3_path = "C:\\working\\ProxSpace\\pm3\\proxmark3\\client"
    cmd = f'{proxmark3_path}\\proxmark3 COM4 -c "data load -f {file_name}; lf sim"'
    run_command(cmd)


def delete_file():
    if os.path.exists(file_name):
        os.remove(file_name)
