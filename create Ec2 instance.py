import boto3
session=boto3.Session(profile_name='default')
InstanceName= input("Enter the Name of the Instance to be created: ")
region=input("Enter the Region in which u want your instance to be deployed: ")
ec2=session.client(service_name='ec2',region_name=region)
resource =ec2.run_instances(
#check the mentioned AMI exist in the given region
    ImageId='ami-0b44050b2d893d5f7',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance' ,
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': InstanceName,
                },
            ]
        },
    ],

)
print(resource['Instances'])