import os
import subprocess


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
    cmd = f'{proxmark3_path}\\proxmark3 COM4 -c "lf sniff; data save -f graph.pm3"'
    run_command(cmd)


def run_sim_cmd():
    proxmark3_path = "C:\\working\\ProxSpace\\pm3\\proxmark3\\client"
    cmd = f'{proxmark3_path}\\proxmark3 COM4 -c "data load -f graph.pm3; lf sim"'
    run_command(cmd)

