#!/bin/sh
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec /opt/venv/bin/aws-lambda-rie /opt/venv/bin/python -m awslambdaric $1
else
    exec /opt/venv/bin/python -m awslambdaric $1
fi