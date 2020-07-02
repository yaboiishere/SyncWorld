from requests import get
from git import Repo
import os
import socket
import subprocess
import time

#git variables
PATH_OF_GIT_REPO = os.getcwd()
COMMIT_MESSAGE = 'updated state'
repo = Repo(PATH_OF_GIT_REPO)

#Just starts a command and returns the output
def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,
                     shell=True)
    return iter(p.stdout.readline, b'')

#Pulls from git repo because it won't push later
repo.remotes.origin.pull()

#Opens mcServerState.txt and gets the value
f = open("mcServerState.txt", "r")
state = f.readline()
print(state)

try:
    #If the value is True it shuts down the script
    if state == "True":
        print("Server is working")
        exit()
    f.close()

    #Updates the value
    f = open("mcServerState.txt", "w")
    f.write("True")
    f.close()
    
    #Uploads the txt to Git
    repo.git.add("mcServerState.txt")
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

    print("No server is running starting yours")

    #Changes the current working directory so the server unpacks in the proper folder
    os.chdir("McServer")
    print(os.getcwd())

    #Here is where the server starts
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'server.jar')
    for output_line in run_command('java -Xmx1024M -Xms1024M -jar '+ my_file + " nogui"):
        print(output_line)

    #Changes the current directory to parrent, so to be able to upload to git
    os.chdir("../")

#If an error occurs the state will not be stuck on true
except Exception as err:
    os.chdir("../")
    f = open("mcServerState.txt", "w")
    f.write("False")
    f.close()

    repo.git.add("mcServerState.txt")
    repo.index.commit("Server Failed Exception")
    origin = repo.remote(name='origin')
    origin.push()   

    print("There was an error")
    print(err)
    exit()

#Saves the world data and changes the state, also pushes to github
f = open("mcServerState.txt", "w")
f.write("False")
f.close()

repo.git.add(".")
repo.index.commit("World Save")
origin = repo.remote(name='origin')
origin.push()

print("done")
