import boto3
session=boto3.Session(profile_name='default')
iam=session.client(service_name='iam')
file = open("C:\\Users\\vikash.kumar67\\Desktop\\Python_Scripting\\scripting\\iamuser.txt", "r")
for i in file.readlines():
    policy = iam.Policy('arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')
    detach_policy = policy.detach_user(UserName= i)
    group = iam.Group('Tester')
   response = group.remove_user(UserName= i)
    print("Deleting IAM User: "+ i)
    iam.delete_user(UserName= i)