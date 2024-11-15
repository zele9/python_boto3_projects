import boto3
import csv
import os

def Instance_fun(writer):
    ec2 = boto3.client('ec2')
    empty_dict = {}

    list_instance_var = ec2.describe_instances()
    
    for reservation in list_instance_var['Reservations']:
        for instance in reservation['Instances']:
            empty_dict["AMI_ID"] = instance['ImageId']
            empty_dict["InstanceId"] = instance['InstanceId']
            empty_dict["Created_date"] = instance['LaunchTime']

            writer.writerow(empty_dict)
            print("CSV has been generated and stored in same location")

def main():
    field_names = ["AMI_ID","InstanceId","Created_date"]
    file_name = "empty_dict.csv"
    with open (file_name, "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        Instance_fun(writer)


main()