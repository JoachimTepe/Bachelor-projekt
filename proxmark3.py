import os
import subprocess
import datetime

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
    proxmark3_path = "C:\\working\\ProxSpace\\pm3\\proxmark3-4.16191\\client"
    cmd = f'{proxmark3_path}\\proxmark3 COM4 -c "lf config -t 20; lf sniff; data save -f graph.pm3"'
    curr_time = datetime.datetime.now().time()
    print("Pre sniffing " + str(curr_time.hour), curr_time.minute, curr_time.second, curr_time.microsecond)
    run_command(cmd)
    curr_time = datetime.datetime.now().time()
    print("post sniffing " + str(curr_time.hour), curr_time.minute, curr_time.second, curr_time.microsecond)


def run_sim_cmd():
    proxmark3_path = "C:\\working\\ProxSpace\\pm3\\proxmark3\\client"
    cmd = f'{proxmark3_path}\\proxmark3 COM4 -c "data load -f graph.pm3; lf sim"'
    curr_time = datetime.datetime.now().time()
    print("pre simulation " + str(curr_time.hour), curr_time.minute, curr_time.second, curr_time.microsecond)
    run_command(cmd)

