import boto3
session=boto3.Session()
s3=session.resource('s3')
#bucketname='vikashk872'
#object=[]
#id=[]
#bucket= s3.bucket('vikashk872')
for each in s3.ObjectVersion :
    print(each)