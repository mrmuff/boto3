import boto3
ec2=boto3.resource('ec2')

base=ec2.instances()

print(base)