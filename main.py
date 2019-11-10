from git import git
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

  git.CloneRepo(variables.GIT_REPO, variables.GIT_USERNAME, variables.GIT_PASSWORD)
  terraform.AppendTFVarsFile(tfvars)
  git.CreateBranch(event['snowRequestId'])
  git.CommitChanges(event['snowRequestId'])
  git.PushBranch("origin", event['snowRequestId'])
  git.CleanRepo()
