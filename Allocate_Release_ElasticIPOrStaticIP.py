
import boto3
from botocore.exceptions import ClientError

#ec2 = boto3.client('ec2',region_name='ap-south-1')

ec2 = boto3.client('ec2',region_name='us-east-1')

try:
    allocation = ec2.allocate_address(Domain='vpc')
    response = ec2.associate_address(AllocationId=allocation['AllocationId'],
                                     InstanceId="i-0b0cf191392155f53")
    print(response)

except ClientError as e:
    print(e)




"""
import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

try:
    response = ec2.release_address(AllocationId='ALLOCATION_ID')
    print('Address released')
except ClientError as e:
    print(e)

"""