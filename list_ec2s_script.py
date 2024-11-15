import boto3
import os

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
instances = [instance for reservation in response['Reservations'] for instance in reservation['Instances']]
print(instances)