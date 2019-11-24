import os
import variables
# We need to create a file with the appropriate properties

new_repo_path = variables.NEW_REPO_PATH

def CreateTFVarsFile(variables):
    with open("{}/repo/variables.tfvars".format(new_repo_path), "w+") as file:
        for key, value in variables.items():
            file.write("\"{}\" = \"{}\" \n".format(key, value))
    

def AppendTFVarsFile(variables):
    with open("{}/repo/variables.tfvars".format(new_repo_path),"a+") as file:
        for key, value in variables.items():
            file.write("\"{}\" = \"{}\" \n".format(key, value))