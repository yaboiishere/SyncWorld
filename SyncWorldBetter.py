from requests import get
from git import Repo
import os
import socket
import subprocess

PATH_OF_GIT_REPO = os.getcwd()
COMMIT_MESSAGE = 'updated state'

def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

repo = Repo(PATH_OF_GIT_REPO)
state = ""
repo.remote().origin.repo.git.checkout("origin/master", "mcServerState")
with open("mcServerState.txt", "r") as file:
    state = file.readline()
    if state == True
        print("Server is working")
        exit()
    file.close()
    file.open("mcServerState.txt", "w")
    file.write("True")
    file.close()

repo.remotes.origin.pull()
os.chdir("McServer")
#Here is where the server starts
for output_line in run_command('java -Xmx1024M -Xms1024M -jar server.jar nogui'):
    print(output_line)
os.chdir("../")
print("done")
