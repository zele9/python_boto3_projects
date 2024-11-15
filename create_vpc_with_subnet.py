import boto3
import os

# Create a client for the EC2 service
ec2 = boto3.client('ec2', region_name="us-west-2")

# Create a VPC
vpc_response = ec2.create_vpc(CidrBlock='10.11.0.0/16')

#Extract VPC ID from vpc_response dictionary and print
vpc_id = vpc_response['Vpc']['VpcId']
print(f'Created VPC with ID: {vpc_id}')

# Add a Name tag to the VPC
ec2.create_tags(
    Resources=[vpc_id],
    Tags=[{
            'Key': 'Name',
            'Value': 'NewAtabaVPC'
        }]
    )

# Create a subnet within the VPC
subnet_response = ec2.create_subnet(
    AvailabilityZone='us-west-2c',
    CidrBlock='10.11.1.0/24',
    VpcId=vpc_id
)
subnet_id = subnet_response['Subnet']['SubnetId']
print(f'Created Subnet with ID: {subnet_id}')

# Add a Name tag to the Subnet
ec2.create_tags(
    Resources=[subnet_id],
    Tags=[{
            'Key': 'Name',
            'Value': 'AtabaFirstSubnet'
        }]
    )

#Create an internet gateway and attach it to VPC
igw_response = ec2.create_internet_gateway()
igw_id = igw_response["InternetGateway"]["InternetGatewayId"]
print(igw_id)

igw_vpc_attachment = ec2.attach_internet_gateway(
    InternetGatewayId = igw_id,
    VpcId = vpc_id
)
print("Internet Gateway Attached Successfully")

# Create a route table within the VPC
route_table_response = ec2.create_route_table(VpcId=vpc_id)
route_table_id = route_table_response['RouteTable']['RouteTableId']
print(f'Created Route Table with ID: {route_table_id}')

# Add a Name tag to the Route Table
ec2.create_tags(
    Resources=[route_table_id],
    Tags=[{
        'Key': 'Name', 
        'Value': 'MyRouteTable'
        }]
    )

# Associate the Route Table with the Subnet
route_table_association_response = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)
route_table_association_id = route_table_association_response['AssociationId']
print(f'Associated Route Table with Subnet. Association ID: {route_table_association_id}')
