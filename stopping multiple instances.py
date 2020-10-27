import boto3

file=open(r"C:\Users\vikash.kumar67\Desktop\instance.txt","r+")
#file.close()

session =boto3.Session(profile_name='default')
ec2=session.client(service_name='ec2')
ssm=session.client(service_name='ssm')
for each in file:
    print(each)
    print(ec2.start_instances(InstanceIds=[each]))