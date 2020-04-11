import time
import boto
import boto.ec2.networkinterface

from settings.settings import AWS_ACCESS_GENERIC

ec2 = boto.connect_ec2(*AWS_ACCESS_GENERIC)

interface = boto.ec2.networkinterface.NetworkInterfaceSpecification(subnet_id='subnet-11d02d71',
                                                                    groups=['sg-0365c56d'],
                                                                    associate_public_ip_address=True)
interfaces = boto.ec2.networkinterface.NetworkInterfaceCollection(interface)

reservation = ec2.run_instances(image_id='ami-a1074dc8',
                                instance_type='t1.micro',
                                #the following two arguments are provided in the network_interface
                                #instead at the global level !!
                                #'security_group_ids': ['sg-0365c56d'],
                                #'subnet_id': 'subnet-11d02d71',
                                network_interfaces=interfaces,
                                key_name='keyPairName')

instance = reservation.instances[0]
instance.update()
while instance.state == "pending":
    print instance, instance.state
    time.sleep(5)
    instance.update()

instance.add_tag("Name", "some name")

print "done", instance