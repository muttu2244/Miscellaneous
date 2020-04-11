import boto3
import sys


def main():
    """
    This script shows and example of Boto3 integration with Stratoscale.
    The scenario is as such:
         1. Instantiate an instance from an AMI,
         2. Create a 20 GB volume,
         3. Attach the volume to the created AMI.
    """

    # creating a connection to Stratoscale AWS Compatible region
    client = boto3.Session.client(boto3.session.Session(), service_name="ec2", region_name="symphony",
                                  endpoint_url="https://<cluster ip>/api/v2/ec2/",
                                  verify=False,
                                  aws_access_key_id="<key>",
                                  aws_secret_access_key="<secret>")

    # finding our Centos image, grabbing its image ID
    images = client.describe_images()
    image_id = next(image['ImageId'] for image in images if 'centos' in image['Name'])

    print "Found desired image with ID: " + image_id

    # running a new instance using our Centos image ID
    ec2_instance = client.run_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1
    )

    # check if EC2 instance was created successfully
    if ec2_instance['ResponseMetadata']['HTTPStatusCode'] == 200:
        print "Successfully created instance! " + ec2_instance['Instances'][0]['InstanceId']

    # create an EBS volume, 20G size
    ebs_vol = client.create_volume(
        Size=20,
        AvailabilityZone='symphony'
    )

    volume_id = ebs_vol['VolumeId']

    # check that the EBS volume had been created successfully
    if ebs_vol['ResponseMetadata']['HTTPStatusCode'] == 200:
        print "Successfully created Volume! " + volume_id

    # attaching EBS volume to our EC2 instance
    attach_resp = client.attach_volume(
        VolumeId=volume_id,
        InstanceId=ec2_instance['Instances'][0]['InstanceId'],
        Device='/dev/sdm'
    )

if __name__ == '__main__':
sys.exit(main(sys.argv[1:]))


"""

# create VPC
vpc = boto.create_vpc(CidrBlock='10.0.0.0/24')
vpc_id = vpc['Vpc']['VpcId']
 
# create subnet
subnet = boto.create_subnet(VpcId=vpc_id, CidrBlock='10.0.0.0/24')
 
# create security group
response = boto.create_security_group(GroupName='my_group_name', Description='my_description', VpcId=vpc_id)
security_group_id = response['GroupId']
 
# add two ingress rules to thew newly created security group,
# CIDR notation "0.0.0.0/0" allows access from anywhere
boto.authorize_security_group_ingress(GroupId=security_group_id, IpPermissions=},
    {'FromPort': 4000, 'ToPort': 4000, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
 
# create instance assuming your image id is image_id
i1 = self.boto.run_instances(ImageId=image_id, MinCount=1, MaxCount=1,
                             NetworkInterfaces=[{'SubnetId': subnet_id, 'Groups': , 'DeviceIndex': 0}])



# create a new key pair for your account
key = boto.create_key_pair(KeyName="my_key_name")
 
# get the unencrypted PEM encoded RSA private key
# that you will later add to the machine from which you
# want to access the instance
pem = key['KeyMaterial']
 
i1 = boto.run_instances(KeyName='my_key_name', ImageId=image_id, MinCount=1, MaxCount=1, 
                        NetworkInterfaces=[{'SubnetId': subnet_id, 'Groups': , 'DeviceIndex': 0}])
 
# create a floating IP in our VPC
allocation = sboto.allocate_address(Domain='vpc')
allocation_id = allocation['AllocationId']
 
# associate address with instance after getting its ID
boto.associate_address(InstanceId=i1_instance_id, allocation_id)

"""



















