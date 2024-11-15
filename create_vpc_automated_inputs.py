import boto3
import os

vpc = boto3.client('ec2', region_name="us-west-2")

vpc_cidr = input("Enter CIDR for VPC: ")
create_vpc = vpc.create_vpc(CidrBlock=vpc_cidr)
vpc_id = create_vpc['Vpc'][VpcId]
print(vpc_id)

subnet_cidr = input("Enter CIDR for Subnet: ")
create_subnet = vpc.create_subnet(CidrBlock=subnet_cidr, VipcId=vpc_id)
subnet_id = create_subnet['Subnet']['SubnetId']
print(subnet_id)
