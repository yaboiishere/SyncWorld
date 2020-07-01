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
repo.remote("origin").repo.git.checkout("origin/master", "mcServerState.txt")

f = open("mcServerState.txt", "r")
state = f.readline()
print("No server is running starting yours")
try:
    if state == True:
        print("Server is working")
        exit()
    f.close()

    f = open("mcServerState.txt", "w")
    f.write("True")
    f.close()

    repo.git.add("mcServerState.txt")
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

    repo.remotes.origin.pull()

    os.chdir("McServer")

    #Here is where the server starts
    for output_line in run_command('java -Xmx1024M -Xms1024M -jar server.jar nogui'):
        print(output_line)

    os.chdir("../")
except as err:
    os.chdir("../")
    f = open("mcServerState.txt", "w")
    f.write("False")
    f.close()

    repo.git.add(".")
    repo.index.commit("World Save")
    origin = repo.remote(name='origin')
    origin.push()   

    print("There was an error")
    print(err)
    exit()

f = open("mcServerState.txt", "w")
f.write("False")
f.close()

repo.git.add("mcServerState.txt")
repo.index.commit("World Save")
origin = repo.remote(name='origin')
origin.push()

print("done")
