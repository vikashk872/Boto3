import boto3
session=boto3.Session(profile_name='default')

asg=session.client(service_name='autoscaling')

asgname = open("C:\\Users\\vikash.kumar67\\Desktop\\Python_Scripting\\scripting\\UCAS\\suspending asg\\asg.txt", "r")


for i in asgname:
    suspend=asg.suspend_processes(AutoScalingGroupName=i,
                                 #ScalingProcesses=['Launch','Terminate','AddToLoadBalalncer','AlarmNotification','AZRebalance','HealthCheck','InstanceRefresh','ReplaceUnhealthy',
                                #'ScheduledActions'
                                 )
    print(' Autoscaling Process suspended for : '+ i)

asgname.close()