import shlex
from glob import glob
from subprocess import run, PIPE, CalledProcessError

command_str = "netstat -n"

filespec = 'DATA/*.zip'
file_list = glob(filespec)

command_words = shlex.split(command_str)  + file_list
print("command_words: {}".format(command_words))

# run(command_words)

process = run(command_words, stdout=PIPE)

print(process.returncode)
output = process.stdout.decode()
output_lines = output.splitlines()  # split on \n
# print(output_lines[:10])

for line in output_lines:
    if line.startswith('tcp4'):
        proto, recv, send, local, foreign, state = line.split()
        if state == 'ESTABLISHED':
            local_ip, local_port = local.rsplit('.', 1)
            foreign_ip, foreign_port = foreign.rsplit('.', 1)
            print(f"{local_ip:15s} {local_port:>5s}    {foreign_ip:15s} {foreign_port:>5s}")




