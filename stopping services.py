import boto3

file=open(r"C:\Users\vikash.kumar67\Desktop\instance.txt","r")

session =boto3.Session(profile_name='default')
ec2=session.client(service_name='ec2')
ssm=session.client(service_name='ssm')
for each in file:
    #ec2.stop_instances(InstanceIds=each)
    print(each)
    #each=str(each).strip('\n')
    response=ssm.send_command(InstanceIds=[each],
    DocumentName = 'AWS-RunPowerShellScript',
    Parameters = {"commands": ["date;ipconfig"]} )
    print(response)
    

