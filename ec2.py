import boto3

def create_ec2_instance():
    # Initialize a session using your AWS credentials
    ec2 = boto3.resource('ec2', region_name='ap-south-1')

    # Define instance details
    instances = ec2.create_instances(
        ImageId='ami-0dee22c13ea7a9a67',  # Replace with your desired AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',        # Choose your instance type
        KeyName='krish',            # Replace with your key pair name
        SecurityGroupIds=['sg-0856544a855425ece'],  # Replace with your Security Group ID
        SubnetId='subnet-0cea46b3f4d693e04',        # Replace with your Subnet ID
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'MyBoto3Instance'}]
            }
        ]
    )

    print("EC2 Instance created with ID:", instances[0].id)

if __name__ == "__main__":
    create_ec2_instance()
