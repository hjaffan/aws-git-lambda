import os

# First Need to Clone a repo


def CloneRepo(repo, username, password):
    try:
        os.system("git clone https://{}:{}@{} repo-dir".format(username,password,repo))
    except Exception as e:
        os.error(e)
        exit(100) # 100 Error means failed to clone repo

def CreateBranch(branch_name):
    try:
        os.system("cd repo-dir && git checkout -B {}".format(branch_name))
    except Exception as e:
        os.error(e)
        exit(200)

def CommitChanges(branch_name):
    try:
        os.system("cd repo-dir && git commit -am 'Updating Instance type via automation'")
    except Exception as e:
        os.error(e)
        exec(300)

def PushBranch(origin, branch_name):
    try:
        os.system("cd repo-dir && git push -u {} {}".format(origin, branch_name))
    except Exception as e:
        os.error(e)
        exec(300)    

def CleanRepo():
    try:
        os.system("rm -rf repo-dir/")
    except Exception as e:
        os.error(e)
        exec(400)