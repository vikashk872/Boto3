import boto3
region=[]
session=boto3.Session(profile_name='default')

ec2=session.client(service_name='ec2')
for each_r in ec2.describe_regions()['Regions']:
    region.append(each_r['RegionName'])

for each_ec2 in region:
    print("Instances in "+ each_ec2)
    ec_in=session.client('ec2',region_name =each_ec2)
    for each_in in ec_in.describe_instances()['Reservations']:
        for each_in in each_in['Instances']:
            print(each_in['InstanceId'],each_in['State']['Name'],each_in['PrivateIpAddress'])

