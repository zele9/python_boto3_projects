import boto3
import os

s3 = boto3.client('s3')
response = s3.list_buckets()
print(response['Buckets'])
