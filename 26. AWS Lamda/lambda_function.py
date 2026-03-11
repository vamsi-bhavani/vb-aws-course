import boto3
import datetime
import logging

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize EC2 client
ec2_client = boto3.client('ec2')

def get_mysql_instance_ids():
    """Fetches EC2 instance IDs where the Name tag is 'dev-mysql'"""
    try:
        response = ec2_client.describe_instances(
            Filters=[
                {'Name': 'tag:Name', 'Values': ['dev-mysql']}
            ]
        )

        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])

        return instance_ids

    except Exception as e:
        logger.error(f"Error fetching instances: {str(e)}")
        return []

def create_ec2_backup(instance_id):
    """Creates an AMI backup of the specified EC2 instance, using its Name tag"""
    try:
        # Fetch instance details
        instance_desc = ec2_client.describe_instances(InstanceIds=[instance_id])
        tags = instance_desc['Reservations'][0]['Instances'][0].get('Tags', [])
        
        # Extract the Name tag or fallback to instance ID
        name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), instance_id)
        
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
        ami_name = f'backup-{name_tag}-{timestamp}'

        response = ec2_client.create_image(
            InstanceId=instance_id,
            Name=ami_name,
            Description=f'Automated backup of {name_tag} ({instance_id}) taken on {timestamp}',
            NoReboot=True
        )

        ami_id = response['ImageId']
        logger.info(f'AMI created successfully: {ami_id} with name {ami_name}')

        # Tag the AMI
        ec2_client.create_tags(
            Resources=[ami_id],
            Tags=[
                {'Key': 'Team', 'Value': 'DevOps'},
                {'Key': 'Name', 'Value': ami_name}
            ]
        )
        logger.info(f'Tagged AMI {ami_id} with Team=DevOps and Name={ami_name}')

        return ami_id
    except Exception as e:
        logger.error(f'Error creating AMI for instance {instance_id}: {str(e)}')
        return None

def lambda_handler(event, context):
    """Lambda function entry point"""
    instance_ids = get_mysql_instance_ids()
    
    if not instance_ids:
        logger.warning("No instances found with Name=dev-mysql tag.")
        return {"statusCode": 404, "body": "No instances found with Name=dev-mysql tag."}
    
    ami_ids = []
    for instance_id in instance_ids:
        logger.info(f"Backing up instance: {instance_id}")
        ami_id = create_ec2_backup(instance_id)
        if ami_id:
            ami_ids.append(ami_id)

    return {
        "statusCode": 200,
        "body": f"Backup completed for AMIs: {', '.join(ami_ids)}"
    }
