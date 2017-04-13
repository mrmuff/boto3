# This lists ec2 instances
import boto3

AWS_ACCESS_KEY_ID = "AKIAIO4H7NVHGJ7NPC6Q"
AWS_SECRET_ACCESS_KEY = "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"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

ec2 = session.resource('ec2', region_name='us-west-2')

instances = ec2.instances.filter()
for instance in instances:
    print(instance.id)