# aws-git-lambda

## Usage

This repository uses the serverless framework found [here](https://serverless.com/)

## Deployment

1. Install aws cli
1. Install sls cli
1. Install Docker
1. sls plugin install -n serverless-python-requirements
1. export AWS_ACCESS_KEY_ID=<your-key-here>
1. export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
1. Update Environment variables in serverless.yml
```yaml
functions:
  parse_webhook:
    handler: main.parse_webhook
    environment:
      GIT_REPO: "Please Populate"
      FULL_NAME: "Please Populate"
      GIT_EMAIL: "Please Populate"
      GIT_USERNAME: "Please Populate"
      GIT_PASSWORD: "Please Populate"
      SKIP_SSL: true
```
1. serverless deploy


* Reference for [deployment](https://serverless.com/framework/docs/providers/aws/guide/deploying/)

