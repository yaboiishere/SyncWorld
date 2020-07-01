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
repo.remote().origin.repo.git.checkout("origin/master", "mcServerState.txt")
print("asdaasdadasdasdas")
f = file.open("mcServerState.txt", "r")
state = f.readline()
print(state)
if state == True
    print("Server is working")
    exit()
f.close()
print("asdaasdadasdasdas")

f.open("mcServerState.txt", "w")
f.write("True")
f.close()
print("asdaasdadasdasdas")

repo.git.add("mcServerState.txt")
repo.index.commit(COMMIT_MESSAGE)
origin = repo.remote(name='origin')
origin.push()
print("asdaasdadasdasdas")

repo.remotes.origin.pull()
print("asdaasdadasdasdas")

# os.chdir("McServer")
# #Here is where the server starts
# for output_line in run_command('java -Xmx1024M -Xms1024M -jar server.jar nogui'):
#     print(output_line)
# os.chdir("../")
# print("done")
