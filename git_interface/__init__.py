import os
import git
import variables

# First Need to Clone a repo

new_repo_path = variables.NEW_REPO_PATH
commit_env = variables.commit_env

def CloneRepo(repo, username, password):
    try:
        git.exec_command('clone', '{}'.format(repo), 'repo', cwd="{}".format(new_repo_path))
    except Exception as e:
        os.error(e)
        print(e)
        exit(100) # 100 Error means failed to clone repo

def CreateBranch(branch_name):
    try:
        git.exec_command('checkout', '-B',  '{}'.format(branch_name), cwd="{}/repo".format(new_repo_path))
    except Exception as e:
        print(e)
        os.error(e)
        exit(200)

def CommitChanges(branch_name):
    try:
        git.exec_command('add', '.', cwd="{}/repo".format(new_repo_path))
        git.exec_command('commit','-m "Updating Instance type via automation"', cwd="{}/repo".format(new_repo_path), env=commit_env)
    except Exception as e:
        os.error(e)
        exec(300)

def PushBranch(origin, branch_name):
    try:
         git.exec_command("push", "-u", "{}".format(origin), "{}".format(branch_name), cwd="{}/repo".format(new_repo_path))
    except Exception as e:
        os.error(e)
        exec(300)    

def CleanRepo():
    try:
        os.system("rm -rf {}/repo".format(new_repo_path))
    except Exception as e:
        os.error(e)
        exec(400)