### Automated AMI Backups for EC2 Instances Using Lambda

This Python script is designed to **run in AWS Lambda** and **automatically create AMI backups** of EC2 instances that have a `Name` tag equal to `dev-mysql`.

Here's a breakdown of what each part does:

### 🔧 **Imports and Setup**
```python
import boto3
import datetime
import logging
```
- **boto3**: AWS SDK for Python, used to interact with AWS services.
- **datetime**: For timestamping backups.
- **logging**: For logging information and errors.

```python
logger = logging.getLogger()
logger.setLevel(logging.INFO)
```
- Sets up logging so we can track what the script is doing in AWS CloudWatch Logs.

```python
ec2_client = boto3.client('ec2')
```
- Initializes a client to interact with the EC2 service.

---

### 🔍 **Function: `get_mysql_instance_ids()`**

Purpose: Get all EC2 instances with the `Name=dev-mysql` tag.

```python
response = ec2_client.describe_instances(
    Filters=[{'Name': 'tag:Name', 'Values': ['dev-mysql']}]
)
```
- Uses a filter to find instances with the tag `Name=dev-mysql`.

```python
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])
```
- Iterates through all matching reservations and collects the `InstanceId` values.

If it fails, logs the error and returns an empty list.

---

### 💾 **Function: `create_ec2_backup(instance_id)`**

Purpose: Create an AMI (Amazon Machine Image) backup of a specific EC2 instance.

```python
instance_desc = ec2_client.describe_instances(InstanceIds=[instance_id])
tags = instance_desc['Reservations'][0]['Instances'][0].get('Tags', [])
```
- Fetches the instance's details to read its tags.

```python
name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), instance_id)
```
- Extracts the `Name` tag, or falls back to the instance ID if no tag is found.

```python
timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
ami_name = f'backup-{name_tag}-{timestamp}'
```
- Creates a unique name for the backup with a timestamp.

```python
response = ec2_client.create_image(
    InstanceId=instance_id,
    Name=ami_name,
    Description=f'Automated backup of {name_tag} ({instance_id}) taken on {timestamp}',
    NoReboot=True
)
```
- Creates the AMI without rebooting the instance (`NoReboot=True`).

```python
ec2_client.create_tags(
    Resources=[ami_id],
    Tags=[
        {'Key': 'Team', 'Value': 'DevOps'},
        {'Key': 'Name', 'Value': ami_name}
    ]
)
```
- Tags the new AMI for easier identification and management.

If an error occurs, it's logged and `None` is returned.

---

### 🚀 **Lambda Handler: `lambda_handler(event, context)`**

This is the entry point when the Lambda function is triggered.

1. Calls `get_mysql_instance_ids()` to find EC2 instances to back up.
2. Loops through each instance and calls `create_ec2_backup()`.
3. Collects all successfully created AMI IDs.
4. Returns a response with the list of created AMIs.

---

### ✅ **Sample Output**
If successful:
```json
{
  "statusCode": 200,
  "body": "Backup completed for AMIs: ami-0123456789abcdef0, ami-0abcdef1234567890"
}
```

If no matching instances found:
```json
{
  "statusCode": 404,
  "body": "No instances found with Name=dev-mysql tag."
}
```
