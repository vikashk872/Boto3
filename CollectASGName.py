import boto3
session=boto3.Session(profile_name='default')

asg=session.client(service_name='autoscaling')
for i in asg.describe_auto_scaling_groups()['AutoScalingGroups']:
    #print(i['AutoScalingGroupName'])
    file=open("C:\\Users\\vikash.kumar67\\Desktop\\Python_Scripting\\scripting\\UCAS\\collectasg.txt", "w")
    file.write((i['AutoScalingGroupName']))
    file.close()
    file = open("C:\\Users\\vikash.kumar67\\Desktop\\Python_Scripting\\scripting\\UCAS\\collectasg.txt", "r")
    print(file.read())
    file.close()
