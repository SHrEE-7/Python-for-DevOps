import boto3

ec2_client = boto3.client('ec2')
all_available_vpcs = ec2_client.describe_vpcs()
print(all_available_vpcs)
vpcs = all_available_vpcs["Vpcs"]

# for vpc in vpcs:
    
