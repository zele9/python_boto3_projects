import boto3
import os

iam = boto3.client('iam')
response = iam.list_users()
print(response['Users'])
