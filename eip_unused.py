import boto3
region=[]
session=boto3.Session(profile_name='default')

ec2=session.client(service_name='ec2')
addresses_dict = ec2.describe_addresses()
for eip_dict in addresses_dict['Addresses']:
     if "InstanceId" not in eip_dict:
          print (eip_dict['PublicIp'] + " doesn't have any instances associated, releasing")
          ec2.release_address(AllocationId=eip_dict['AllocationId'])