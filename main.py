import os
import subprocess

#from send_file import send_file

# This Bluetooth device - 2c:8d:b1:ed:68:80
# This UUID - 7DC1ABC9-CE4B-11EB-80F0-902E163640B3
# Target Bluetooth device - e4:70:b8:0c:f2:a5
# Target UUID - 118C694C-2830-11B2-A85C-F40E8F872426

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
run_command(cmd)
#send_file()


