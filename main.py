import os
import subprocess

from send_file import send_file

proxmark3_path = "C:\\working\\ProxSpace\\pm3\\proxmark3-4.16191\\client"

os.environ['PATH'] += os.pathsep + r"C:\working\ProxSpace\msys2\mingw64\bin"

def run_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output)

    print(error)

    if process.returncode != 0:
        print(f'Error occurred: {error.decode().strip()}')
    else:
        print(f'Output: {output.decode().strip()}')


cmd = f'{proxmark3_path}\\proxmark3 COM4 -c "lf sniff; data save -f graph.pm3"'

print(cmd)
# run_command(cmd)
send_file("abc","abc")

