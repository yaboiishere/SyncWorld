To make a new server\
    1. Install gitbash and python3\
    2. Make a git profile\
    3. Make a git repo\
        3.1 Navigate to the directory you would like to use wit gitbash\
        3.2 Paste the following:
            git init
            git add .
            git commit -m "initial commit"
        3.3 Open Github and login
        3.4 Click New Repository and give it a name
        3.5 Paste the following and change the relevant info in the {}
            git remote add origin git@github.com:{username in git}/{name of repository}
            git push -u origin master
    4. In the newly created folder which should be named the same as the repository paste the following files
        .gitignore
        mcServerState.txt
        requirements.txt
        SyncWorld.py
    5. In the same folder create a folder called McServer (case matters)
    6. Paste your servers jar file in the McServer folde and rename it server.jar
    7. In terminal paste the following:
        pip install -r .\requirements.txt
    8. To start the server type in terminal:
        py .\SyncWorld.py


If you need server.properties there is the default generated one in the repository just copy and rename it in the server folder