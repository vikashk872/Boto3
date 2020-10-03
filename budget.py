import boto3
session=boto3.Session(profile_name='default')
budget=session.client(service_name='budgets')
for each in budget.describe_budgets(AccountId='985840231351')['ResponseMetadata']:
    print(each)