import boto3
session=boto3.Session(profile_name='default')
s3=session.client(service_name='s3')

for eachb in s3.list_buckets()['Buckets']:
    print("Bucket name "+ "\t Creation Date")
    print("==============" + "=============================")
    print("")
    print(eachb['Name'], "\t",eachb['CreationDate'])
    acl= s3.get_bucket_acl( Bucket=eachb['Name'])
    print(acl)
    