import boto3
session=boto3.Session(profile_name='default')
iam=session.client(service_name='iam')
file = open("C:\\Users\\vikash.kumar67\\Desktop\\Python_Scripting\\scripting\\iamuser.txt", "r")
for i in file.readlines():
    print("Deleting IAM User: "+ i)
    iam.delete_user(UserName= i)
