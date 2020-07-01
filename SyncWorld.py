from requests import get
from git import Repo
import os
import socket
import subprocess

PATH_OF_GIT_REPO = os.getcwd()
COMMIT_MESSAGE = 'updated ip list'

def ping(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect((host, port)):
            s.close()
    except:
        return False
    return True

def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

ip = get('https://api.ipify.org').text

# if os.path.isdir(PATH_OF_GIT_REPO+"\\.git") == False:
#     repo = git.Repo.init("~/")
# else:

repo = Repo(PATH_OF_GIT_REPO)
ips = []
ipInListFlag = False
with open("mcServerIps.txt", "r" ) as file:
    for line in file:
        currentLine = line[:-1]
        if currentLine == ip:
            ipInListFlag = True
        ips.append(currentLine)
    file.close()

if(not ipInListFlag):
    file = open("mcServerIps.txt", "a")
    file.write(ip + "\n")
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add("mcServerIps.txt")
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

serverIsWorkingSomewhere = False
serverIsWorkingOnIp = ""
for i in ips:
    if ping(i,25565):
        serverIsWorkingSomewhere = True
        serverIsWorkingOnIp = i + ":25565"


if serverIsWorkingSomewhere:
    print("Server is working on " + serverIsWorkingOnIp)
    exit()
repo.remotes.origin.pull()
os.chdir("McServer")
#Here is where the server starts
for output_line in run_command('java -Xmx1024M -Xms1024M -jar server.jar'):
    print(output_line)
os.chdir("../")
print("done")
