# AWS Resource Management Script

This repository contains Python scripts for managing AWS resources using the Boto3 library. The scripts include functionality for creating VPCs, subnets, route tables, list EC2 instances, IAM Users, S3 buckets, VPCs generating CSV reports for EC2 instances and IAM users.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have an AWS account with appropriate permissions to manage VPCs, subnets, route tables, EC2 instances, S3 Buckets and IAM users.
- You have Python 3.x installed on your machine.
- You have Boto3 and other required packages installed.

To install Boto3, use the following command:
pip install boto3

Usage
Creating VPC, Subnet, and Route Table
The create_vpc_subnet_route.py script creates a VPC, subnet, and route table, and associates the route table with the subnet.

Run the script:
python create_vpc_subnet_route.py

Generating CSV Report for EC2 Instances
The create_csv_report.py script generates a CSV report of your EC2 instances, including details such as AMI ID, instance ID, and launch time.

Run the script:
python create_csv_report.py

Generating CSV Report for IAM Users
The iam_users_csv_report.py script generates a CSV report of your IAM users, including details such as user name, user ID, ARN, creation date, and last password used.

Run the script:
python iam_users_csv_report.py

Contributing
If you want to contribute to this repository, please follow these steps:
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a pull request.

License
This repository is licensed under the MIT License. See the LICENSE file for more information.
