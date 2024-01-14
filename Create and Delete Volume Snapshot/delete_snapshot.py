import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name='ap-south-1')

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
)

sorted_by_date = sorted(snapshots['Snapshots'], key = itemgetter('StartTime'), reverse=True)

for snap in sorted_by_date[2:]:  #keep two latest snaps.
    ec2_client.delete_snapshot(
        SnapshotId=snap['SnapshotId']
    )