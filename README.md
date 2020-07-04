# To make a new server\
    &nbsp;&nbsp;&nbsp;1. Install gitbash and python3\
    &nbsp;&nbsp;&nbsp;2. Make a git profile\
    &nbsp;&nbsp;&nbsp;3. Make a git repo\
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1 Navigate to the directory you would like to use wit gitbash\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2 Paste the following:\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git init\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git add .\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git commit -m "initial commit"\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3 Open Github and login\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4 Click New Repository and give it a name\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5 Paste the following and change the relevant info in the {}\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git remote add origin git@github.com:{username in git}/{name of repository}\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git push -u origin master\
    &nbsp;&nbsp;&nbsp;4. In the newly created folder which should be named the same as the repository paste the following files\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.gitignore\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mcServerState.txt\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirements.txt\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SyncWorld.py
    &nbsp;&nbsp;&nbsp;5. In the same folder create a folder called McServer (case matters)\
    &nbsp;&nbsp;&nbsp;6. Paste your servers jar file in the McServer folde and rename it server.jar\
    &nbsp;&nbsp;&nbsp;7. In terminal paste the following:\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install -r .\requirements.txt\
    &nbsp;&nbsp;&nbsp;8. To start the server type in terminal:\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;py .\SyncWorld.py\


* If you need server.properties there is the default generated one in the repository just copy and rename it in the server folder
