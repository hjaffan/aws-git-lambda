
variable "description" {
  description = "Description of what your Lambda Function does."
}

variable "function_name" {
  description = "A unique name for your Lambda Function"
  default = "parse_webhook"
}

variable "handler_name" {
  description = "The function entrypoint in your code."
  default = "main.parse_webhook"
}

variable "memory_size" {
  description = "Amount of memory in MB your Lambda Function can use at runtime."
  default     = "128"
}

variable "runtime" {
  description = "runtime"
  default     = "python3.7"
}

variable "timeout" {
  description = "The amount of time your Lambda Function has to run in seconds. Defaults to 5 minutes"
  default     = "300"
}

variable "source_code_path" {
  description = "Path to the source file or directory containing your Lambda source code & requirements.txt if applicable"
}

variable "output_path" {
  description = "Path to the function's deployment package within local filesystem. eg: /path/to/lambda.zip"
  default     = "lambda.zip"
}

variable "environment" {
  description = "Environment configuration for the Lambda function"
  type        = map
  default     = {}
}

variable "myregion" {
  description = "Region to create API Gateway"
  default = "us-east-1"
}

variable "accountId" {
  description = "Account ID"
}

variable "git_repo" {
  description = "HTTPS Git Repo URL"
}

variable "full_name" {
  description = "Full name for commiter config"
}

variable "git_email" {
  description = "E-mail address for git commiter"
}

variable "git_username" {
    description = "Username to commit to repo. User must have access"
}

variable "git_password" {
  description = "Password for the username"
}

variable "skip_ssl" {
  description = "Skip SSL validation to remote host. Keep true if signed by internal CA"
  default = true
}
