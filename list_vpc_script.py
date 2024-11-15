import boto3
import os

ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
print(response['Vpcs'])
