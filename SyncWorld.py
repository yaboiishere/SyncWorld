from requests import get
import subprocess
from git import Repo
import os

PATH_OF_GIT_REPO = os.getcwd()
COMMIT_MESSAGE = 'updated ip list'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add("mcServerIps.txt")
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

ip = get('https://api.ipify.org').text

ips = []
with open("mcServerIps.txt", "r" ) as file:
    for line in file:
        currentLine = line[:-1]
        ips.append(currentLine)
    file.close()
ipInListFlag = False

for i in ips:
    if(i==ip):
        ipInListFlag = True
        break

if(not ipInListFlag):
    file = open("mcServerIps.txt", "a")
    file.write(ip)
    git_push()





