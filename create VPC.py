import boto3
session=boto3.Session(profile_name='default')
vpc=session.client(service_name='ec2')
#creating VPC
vpc_cidr='10.0.0.0/16'
vpc_name="VPC_BOTO3"
response=vpc.create_vpc(CidrBlock=vpc_cidr)
print(response)
vpc_id=response['Vpc']['VpcId']
vpc.create_tags(Resources=[vpc_id],
                Tags=[{'Key':'Name','Value':vpc_name}])
print('\n VPC Tags '+ vpc_name + ' Added to '+ vpc_id)

#Create Public Subnet
public_Cidr='10.0.0.0/24'
subnet_response=vpc.create_subnet(VpcId=vpc_id,CidrBlock=public_Cidr)
#print(subnet_response)
subnet_id=subnet_response['Subnet']['SubnetId']
print("\n Created Public Subnet : "+ subnet_id  + " For VPC " + vpc_id)

#create Private Subnet
private_cidr='10.0.1.0/24'
private_subnet=vpc.create_subnet(VpcId=vpc_id,CidrBlock=private_cidr)
#print(private_subnet)
private_subnet_id=private_subnet['Subnet']['SubnetId']
print("\n Created Public Subnet : " + private_subnet_id + " For Vpc "+ vpc_id)

#creating Internet Gateway
igw=vpc.create_internet_gateway()
print(igw)
igw_id=igw['InternetGateway']['InternetGatewayId']
igw_name='Boto3_IGW'
vpc.create_tags(Resources=[igw_id],Tags=[{'Key':'Name','Value':igw_name}])
print("\n Internet Gateway Tag " + igw_name + 'Added to '+ igw_id)

#Adding the Internet Gateway to Public Subnet
vpc.attach_internet_gateway(InternetGatewayId=igw_id,VpcId=vpc_id)
print('\n Attached Internet Gateway '+ igw_id + 'to VPC' + vpc_id)

#Making Subnet Public
#Creating the Route Table
route_table=vpc.create_route_table(VpcId=vpc_id)
rtb_id=route_table['RouteTable']['RouteTableId']
print('\n Created Public Route table ' + rtb_id + 'For Vpc ' + vpc_id)

#Createing the route to IGW
vpc.create_route(RouteTableId=rtb_id,GatewayId=igw_id,DestinationCidrBlock='0.0.0.0/0')
print("\n Added Route for IGW" + igw_id + 'to Route Table '  + rtb_id)

#Associate Public Subnet to route table
vpc.associate_route_table(RouteTableId=rtb_id,SubnetId=subnet_id)
print('\nAssociated Public Subnet ' + subnet_id + ' to Route table' + rtb_id)

#Allow auto assign Public IPV4v addredd to subnet
vpc.modify_subnet_attribute(MapPublicIpOnLaunch= {'Value': True},SubnetId=subnet_id)
print('\n Enabled Auto Assign Public Ip for Subnet ' + subnet_id)

