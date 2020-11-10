import boto3
session=boto3.Session(profile_name='default')
elb=session.client(service_name='elb')
for i in elb.describe_load_balancers()['LoadBalancerDescriptions']:
    #print(i['LoadBalancerName'])
    file = open("C:\\Users\\vikash.kumar67\\Desktop\\Python_Scripting\\scripting\\UCAS\\collectelb.txt", "w")
    file.write(i['LoadBalancerName'])
    file.close()
    file = open("C:\\Users\\vikash.kumar67\\Desktop\\Python_Scripting\\scripting\\UCAS\\collectelb.txt", "r")
    print(file.read())
    file.close()