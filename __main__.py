import pulumi
import pulumi_aws as aws

# Create a VPC
vpc = aws.ec2.Vpc("my-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_support=True,
    enable_dns_hostnames=True
)

# Create an Internet Gateway
internet_gateway = aws.ec2.InternetGateway("my-igw",
    vpc_id=vpc.id
)

# Create a Public Subnet
subnet = aws.ec2.Subnet("my-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    map_public_ip_on_launch=True
)

# Create a route table
route_table = aws.ec2.RouteTable("my-route-table",
    vpc_id=vpc.id,
    routes=[aws.ec2.RouteTableRouteArgs(
        cidr_block="0.0.0.0/0",
        gateway_id=internet_gateway.id,
    )]
)

# Associate the subnet with the route table
route_table_association = aws.ec2.RouteTableAssociation("my-route-table-association",
    subnet_id=subnet.id,
    route_table_id=route_table.id
)

# Security Group allowing SSH and HTTP
security_group = aws.ec2.SecurityGroup("my-sec-group",
    vpc_id=vpc.id,
    description="Allow SSH and HTTP",
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=22,
            to_port=22,
            cidr_blocks=["0.0.0.0/0"],
        ),
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=80,
            to_port=80,
            cidr_blocks=["0.0.0.0/0"],
        ),
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=443,
            to_port=443,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ],
    egress=[
        aws.ec2.SecurityGroupEgressArgs(
            protocol="-1",
            from_port=0,
            to_port=0,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ]
)

'''
So, Here's the plan:

1. Get the private IP of the current instance.
2. If the private IP is the same as the private IP of the first instance, start the Ray cluster.
Thus, making it the head node.
3. If the private IP is not the same as the private IP of the first instance, connect to the Ray cluster.
Thus, making it a worker node.
'''

# User data to install Ray and start/connect to the Ray cluster
# User data to install Ray in a virtual environment and start/connect to the Ray cluster
user_data = """#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3-venv
python3 -m venv ray_env
source ray_env/bin/activate
pip install ray

# Get the private IP of the current instance
PRIVATE_IP=$(curl http://169.254.169.254/latest/meta-data/local-ipv4)

# If this is the first instance (the head node)
if [ "$PRIVATE_IP" == "your_first_instance_private_ip" ]; then
    # Start the Ray cluster
    ray start --head --port=6379
else
    # This is a worker node, so connect to the Ray cluster
    ray start --address='your_first_instance_private_ip:6379'
fi
"""

# Create EC2 Instances
instances = []
for i in range(3):
    instance = aws.ec2.Instance(f"my-instance-{i+1}",
        instance_type="t2.micro",
        vpc_security_group_ids=[security_group.id],
        ami="ami-003c463c8207b4dfa", # Use an appropriate Ubuntu AMI ID for your region
        subnet_id=subnet.id,
        user_data=user_data,
        key_name="key-pair-poridhi-poc"  # Make sure to create a key pair and replace this with your key pair name
    )
    instances.append(instance)

# Export the instance public IPs
for i, instance in enumerate(instances):
    pulumi.export(f"instance_{i+1}_public_ip", instance.public_ip)