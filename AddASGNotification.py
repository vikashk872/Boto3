import boto3
session = boto3.Session(profile_name='default')
asgname = []

#variables used in the Program
environment = "Prod"   #change the environment name based on environmnet
description = 'mwmason'  #check the ASG tag value 
# To check the tag Values
condition1=0  #{Checks environment tag if present set it to 1}
condition2=0  #{Checks the Description tag , if present set it to 1}

asg = session.client('autoscaling')
for each in asg.describe_auto_scaling_groups()['AutoScalingGroups']:
   print(each)
   for tags in each['Tags']:
      print(tags['Key'],tags['Value'])
      if(tags['Key']=='Environment'):
           if (tags['Value']==environment):condition1=1
           else:exit(1)
      elif((tags['Key']=='description')):
            if(tags['Value']==description): condition2=1
            else: exit(1)
      else: exit(1)

#If both Tags are Present
   if condition1==1 and condition2==1:
        asgname.append(each['AutoScalingGroupName'])
   else:exit(1)
   asgname = list(dict.fromkeys(asgname)) #Remove any Duplicate ASG Name

print(asgname) #print the list of ASG
#Adding the Notification Type to ASG

for each in asgname:
   response = asg.put_notification_configuration(
        AutoScalingGroupName=each,
        TopicARN= 'arn:aws:sns:ap-south-1:985840231351:test',
        NotificationTypes=[
            'autoscaling:EC2_INSTANCE_LAUNCH',
            'autoscaling:EC2_INSTANCE_TERMINATE'
        ],
    )
   print(response)