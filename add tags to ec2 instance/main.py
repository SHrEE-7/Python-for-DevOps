import boto3

ec2_client_paris = boto3.client('ec2')
ec2_resource_paris = boto3.resource('ec2')
ec2_client_frankfurt = boto3.client('ec2')
ec2_resource_frankfurt = boto3.resource('ec2')


instance_ids_paris = []
instance_ids_frankfurt = []

reservations_paris = ec2_client_paris.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instance_ids_paris.append(ins['InstanceId'])

response = ec2_resource_paris.create_tags(
    Resources = instance_ids_paris,
    Tags = [
        {
            "Key":"Environment",
            "Value":"Prod"
        },
    ]
)

reservations_frankfurt = ec2_client_frankfurt.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instance_ids_frankfurt.append(ins['InstanceId'])

response = ec2_resource_frankfurt.create_tags(
    Resources = instance_ids_frankfurt,
    Tags = [
        {
            "Key":"Environment",
            "Value":"Test"
        },
    ]
)