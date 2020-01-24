# aws-git-lambda

## Usage

This repository uses terraform to deploy the application
It works on creating a lambda function and setting a trigger to it with an API Gateway

## Deployment

1. Install terraform cli v0.12.16
1. Clone this directory
1. export AWS_ACCESS_KEY_ID=<your-key-here>
1. export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
1. run terraform init
1. run terraform plan first to make sure all is good. (Please populate prompts"
1. run terraform apply

## How to trigger

The API Gateway that gets generated is called myapi

example payload
```json
{
    "snowRequestId":"some-id",
    "environment":"stag",
    "cpuCount":"2",
    "memoryGB":"5"
}
```

curl -X POST https://api-gateway-way-enpoint/ops/update-terraform-repo --data '{"snowRequestId":"some-id","environment":"stag","cpuCount":"2","memoryGB":"5"}'