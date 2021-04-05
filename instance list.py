import boto3
session= boto3.Session(profile_name='default')
list=[]
rds= session.client(service_name='rds')
response= rds.describe_db_snapshots(SnapshotType='manual',IncludePublic=True)['DBSnapshots']
#print(response)
for each_rds in response:
    property = rds.describe_db_snapshot_attributes(DBSnapshotIdentifier=each_rds['DBSnapshotIdentifier'])
    #print(property['DBSnapshotAttributesResult'])
    print("RDS Snapshot Name: "+  property['DBSnapshotAttributesResult']['DBSnapshotIdentifier'] , end='' )

    for each in property['DBSnapshotAttributesResult']['DBSnapshotAttributes']:
         print(" \t Snaphsot Available to { if value is all then its public} : ",end=''); print( each['AttributeValues'])