import git_interface
from files import terraform
import json
import boto3
import variables

def parse_webhook(event, context):
  
  """
  Get payload from API Gateway
  """
  tfvars = {}
  tfvars['environment'] = event['environment']
  tfvars['cpuCount'] = event['cpuCount']
  tfvars['memoryGB'] = event['memoryGB']

  git_interface.CloneRepo(variables.GIT_REPO, variables.GIT_USERNAME, variables.GIT_PASSWORD)
  terraform.AppendTFVarsFile(tfvars)
  git_interface.CreateBranch(event['snowRequestId'])
  git_interface.CommitChanges(event['snowRequestId'])
  git_interface.PushBranch("origin", event['snowRequestId'])
  git_interface.CleanRepo()
