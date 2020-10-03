import boto3
session=boto3.Session(profile_name='default')
cloudwatch=session.client(service_name='cloudwatch')
for each in cloudwatch.list_dashboards()['ResponseMetadata']['RequestId']:
    print(each)