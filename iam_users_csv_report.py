import csv
import boto3
import os

def List_iam_users(writer):
    # Create an IAM client
    iam_user = boto3.client('iam')

#   List IAM users
    iam_users_list = iam_user.list_users()
    actual_users_list = iam_users_list['Users']
    empty_users_list = {}

    # Iterate through each user and write their details to the CSV file
    for user in actual_users_list:
            empty_users_list["user_name"]= user['UserName'],
            empty_users_list["user_id"]= user['UserId'],
            empty_users_list["arn"]= user['Arn'],
            empty_users_list["created_date"]= user['CreateDate'],
            empty_users_list["password_last_used"]= user.get('PasswordLastUsed', 'N/A')  # Use 'N/A' if the key is not present

            writer.writerow(empty_users_list)
        
    print("CSV has been generated and stored in same location")



def main():
    # Define the field names
    field_names = ['user_name', 'user_id', 'arn', 'created_date', 'password_last_used']
    file_name = "iam_users.csv"
    # Open a CSV file for writing
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        List_iam_users(writer)
    
main()