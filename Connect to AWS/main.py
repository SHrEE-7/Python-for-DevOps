import boto3

ec2_client = boto3.client('ec2')
# ec2_client = boto3.client('ec2', region_name = "ap-south-2")  // explicitly specify the region.
all_available_vpcs = ec2_client.describe_vpcs()
# print(all_available_vpcs)
vpcs = all_available_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    
