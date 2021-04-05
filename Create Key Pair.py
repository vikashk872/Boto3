import boto3
import sys

session = boto3.Session(profile_name='default')
key_pair_name = 'Boto3-Key-Pair'
ec2 = session.client(service_name='ec2')

response = ec2.create_key_pair(KeyName=key_pair_name)
print('Created Key Pair with Name: ' + key_pair_name)

with open('C:/Users/vikash.kumar67/Desktop/Boto3-Key-Pair.pem','w') as file:
    file.write(response['KeyMaterial'])
print('Downloaded the key pair file into C:\\Users\\vikash.kumar67\\Desktop\\  location ')
