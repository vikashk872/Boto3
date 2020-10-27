#Return the details about the IAM user credentials being used
import boto3

session=boto3.Session(profile_name='default')
sts=session.client(service_name='sts')
response=sts.get_caller_identity()
#print(response)
print("Account ID : \t",response['Account'])
#print("Account ID : ",response.get('Account'))
print("User ID :\t",response['UserId'])
print("ARN:\t",response['Arn'])