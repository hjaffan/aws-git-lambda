
# API Gateway

resource "aws_api_gateway_rest_api" "api" {
  name = "myapi"
}

resource "aws_api_gateway_resource" "resource" {
  path_part   = "resource"
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_method" "method" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  resource_id   = aws_api_gateway_resource.resource.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "integration" {
  rest_api_id             = aws_api_gateway_rest_api.api.id
  resource_id             = aws_api_gateway_resource.resource.id
  http_method             = aws_api_gateway_method.method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda.invoke_arn
}

# Lambda
resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "arn:aws:execute-api:${var.myregion}:${var.accountId}:${aws_api_gateway_rest_api.api.id}/*/${aws_api_gateway_method.method.http_method}${aws_api_gateway_resource.resource.path}"
}

resource "random_string" "name" {
  length  = 4
  special = false
  upper   = false
}

data "archive_file" "dir_hash_zip" {
  type        = "zip"
  source_dir  = "${var.source_code_path}/"
  output_path = "${path.module}/dir_hash_zip"
}
data "aws_iam_policy_document" "policy" {
  statement {
    sid    = ""
    effect = "Allow"

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "role" {
  name = "myrole"

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
POLICY
}

resource "null_resource" "install_python_dependencies" {
  triggers = {
    requirements = "${sha1(file("${var.source_code_path}/requirements.txt"))}"
    dir_hash     = "${data.archive_file.dir_hash_zip.output_base64sha256}"
  }

  provisioner "local-exec" {
    command = "bash ${path.module}/scripts/py_pkg.sh"

    environment = {
      source_code_path = var.source_code_path
      path_cwd         = path.cwd
      path_module      = path.module
      runtime          = var.runtime
      function_name    = var.function_name
      random_string    = random_string.name.result
    }
  }
}

data "archive_file" "lambda_zip" {
  depends_on  = [null_resource.install_python_dependencies]
  type        = "zip"
  source_dir  = "${path.cwd}/lambda_pkg_${random_string.name.result}/"
  output_path = var.output_path
}

resource "aws_lambda_function" "lambda" {
  filename         = var.output_path
  description      = var.description
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  role    = aws_iam_role.role.arn
  function_name    = var.function_name
  handler          = var.handler_name
  runtime          = var.runtime
  timeout          = var.timeout
  memory_size      = var.memory_size
  environment {
    variables = {
      GIT_REPO = var.git_repo
      FULL_NAME = var.full_name
      GIT_EMAIL = var.git_email
      GIT_USERNAME = var.git_username
      GIT_PASSWORD = var.git_password
      SKIP_SSL = var.skip_ssl
    }
  }
}