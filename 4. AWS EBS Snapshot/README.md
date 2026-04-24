#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is a Snapshot in AWS?

An AWS snapshot is a point-in-time backup of an Amazon EBS (Elastic Block Store) volume.

It captures all the data stored in the EBS volume at the exact moment the snapshot is taken. Since the root volume of an Amazon EC2 instance is usually an EBS volume, it can also be backed up using snapshots.

Snapshots are stored in Amazon S3 and are incremental in nature. This means the first snapshot stores all the data, and the next snapshots store only the changed blocks, which helps reduce storage cost and improves efficiency.

Snapshots are mainly used for data backup, disaster recovery, restoring deleted or corrupted data, creating new EBS volumes, and generating AMIs (Amazon Machine Images) for launching identical EC2 instances.

They can be created, managed, copied, shared, and deleted using the AWS Management Console, AWS CLI, or SDKs.

----

### Lab Session - Creation of a Snapshot from an EBS Volume

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Select EBS Volumes:**
   - In the left sidebar, under "Elastic Block Store," click on "Volumes."
   - Select the EBS volume for which you want to create a snapshot.

3. **Create Snapshot:**
   - Right-click on the volume and select "Create Snapshot."
   - Provide a name and description for the snapshot.
   - Click "Create Snapshot" to initiate the snapshot creation process.
----
### Lab Session - Creation of an AWS AMI from a Snapshot

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Select Snapshots:**
   - In the left sidebar, under "Elastic Block Store," click on "Snapshots."
   - Select the snapshot from which you want to create an AMI.

3. **Create AMI:**
   - Right-click on the snapshot and select "Create Image."
   - Provide a name and description for the AMI.
   - Customize the AMI settings if needed (instance type, tags, etc.).
   - Click "Create Image" to initiate the AMI creation process.
----
### Lab Session - Creation of an EBS Volume from a Snapshot

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Select Snapshots:**
   - In the left sidebar, under "Elastic Block Store," click on "Snapshots."
   - Select the snapshot from which you want to create an EBS volume.

3. **Create Volume:**
   - Right-click on the snapshot and select "Create Volume."
   - Specify the volume type, size, and availability zone for the new EBS volume.
   - Click "Create Volume" to initiate the volume creation process.
----
### Options in a Snapshot

Snapshots in AWS offer several management options:

- **Copy Snapshot:** Create a copy of the snapshot in another AWS region.
- **Modify Snapshot:** Edit the description or permissions of the snapshot.
- **Create Volume:** Generate an EBS volume from the snapshot.
- **Create AMI:** Generate an Amazon Machine Image (AMI) from the snapshot.
----
### Lab Session - Deletion of Snapshots, Volumes, and AMIs

1. **Sign in to AWS Management Console:**
   - Navigate to the respective service dashboard (EC2 for volumes and instances, AMIs for images, etc.).

2. **Delete Snapshots:**
   - In the left sidebar, under "Elastic Block Store" or "AMIs," click on "Snapshots" or "Images."
   - Select the snapshot or AMI you want to delete.
   - Click "Actions > Delete" and confirm the deletion.

3. **Delete Volumes:**
   - In the left sidebar, under "Elastic Block Store," click on "Volumes."
   - Select the volume you want to delete.
   - Click "Actions > Delete Volume" and confirm the deletion.

4. **Delete AMIs:**
   - In the left sidebar, under "AMIs," click on "AMIs."
   - Select the AMI you want to delete.
   - Click "Actions > Deregister" to remove the AMI registration.
   - Once deregistered, select the snapshot associated with the AMI (if needed) and delete it as mentioned above.
