def launch_instance(ami_id, name, type, size, ec2):
   rc = ec2.create_instances(
    ImageId=ami_id,
    MinCount=1,
    MaxCount=1,
    KeyName=key_name,
    InstanceType=size,
    NetworkInterfaces=[
        {
            'DeviceIndex': 0,
            'SubnetId': subnet,
            'AssociatePublicIpAddress': True,
            'Groups': sg
        },
    ]
   )

   instance_id = rc[0].id
   instance_name = name + '-' + type
   ec2.create_tags(
    Resources = [instance_id],
    Tags = [{'Key': 'Name', 'Value': instance_name}]
   )

   return (instance_id, instance_name)