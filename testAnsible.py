
import subprocess
output = subprocess.run("/usr/bin/ansible localhost -m ping", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
print(output)