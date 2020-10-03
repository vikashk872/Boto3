import boto3
session=boto3.Session(profile_name='default')
iam=session.client(service_name='iam')
for each_u in iam.list_users()['Users']:
    print('UserName \t\tUserID \t\t\t\t\t\t ARN \t\t\t\t\t\t\t\tCreation Date')
    print(each_u['UserName']+ '\t' +each_u['UserId']+ '\t' +each_u['Arn']+ '\t',each_u['CreateDate'])