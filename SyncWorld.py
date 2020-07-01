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
                     stderr=subprocess.STDOUT,
                     shell=True)
    return iter(p.stdout.readline, b'')

repo = Repo(PATH_OF_GIT_REPO)
def getShitDone():
    repo.remote("origin").repo.git.checkout("origin/master", "mcServerState.txt")
    return True

if getShitDone():
    print("Got shit done")

f = open("mcServerState.txt", "r")
state = f.readline()

try:
    if state == "True":
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

    print("No server is running starting yours")

    repo.remotes.origin.pull()

    os.chdir("McServer")
    print(os.getcwd())
    #Here is where the server starts
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'server.jar')
    for output_line in run_command('java -Xmx1024M -Xms1024M -jar '+ my_file + " nogui"):
        print(output_line)

    os.chdir("../")
except Exception as err:
    os.chdir("../")
    f = open("mcServerState.txt", "w")
    f.write("False")
    f.close()

    repo.git.add("mcServerState.txt")
    repo.index.commit("World Save")
    origin = repo.remote(name='origin')
    origin.push()   

    print("There was an error")
    print(err)
    exit()

f = open("mcServerState.txt", "w")
f.write("False")
f.close()

repo.git.add(".")
repo.index.commit("World Save")
origin = repo.remote(name='origin')
origin.push()

print("done")
