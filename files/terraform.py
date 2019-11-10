import os

# We need to create a file with the appropriate properties

def _DoesFileExist(file_name):


def CreateTFVarsFile(variables):
    with open("repo-dir/variables.tfvars", "w+") as file:
        for key, value in variables:
            file.write("{} = {}".format(key, value))
    

def AppendTFVarsFile(variables):
    with open("repo-dir/variables.tfvars","a+") as file:
        for key, value in variables:
            file.write("{} = {}".format(key, value))