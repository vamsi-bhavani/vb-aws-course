#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is a Snapshot in AWS?
- A snapshot in AWS refers to a point-in-time backup of an EBS volume or an EC2 instance's root volume.
- It captures the entire state of the volume at the moment the snapshot is taken, including all data, configurations, and settings.
- Snapshots are stored in Amazon S3 and are incremental, meaning only the changed blocks since the last snapshot are stored.
- They are crucial for data backup, disaster recovery, and creating new volumes or AMIs.

1. **Backup at a Point-in-Time:** A snapshot captures the exact state of the EBS volume or EC2 instance's root volume at the moment the snapshot command is issued. It includes all data, configurations, operating system, and application settings.

2. **Incremental Backup:** Snapshots in AWS are incremental, meaning that only the blocks on the volume that have changed since the last snapshot are stored anew. This helps in reducing storage costs and improves the efficiency of backup operations.

3. **Storage Location:** Snapshots are stored in Amazon S3 (Simple Storage Service), which provides durable and secure object storage. This storage mechanism ensures that snapshots are highly reliable and accessible when needed.

4. **Use Cases:**
   - **Data Backup and Recovery:** Snapshots are essential for creating backups of critical data, allowing you to restore data in case of accidental deletion, corruption, or other data loss scenarios.
   - **Disaster Recovery:** They play a crucial role in disaster recovery strategies by providing a recovery point from which you can restore systems quickly.
   - **Creating New Volumes or AMIs:** Snapshots can be used to create new EBS volumes or Amazon Machine Images (AMIs). This is useful for launching new EC2 instances with the same configurations as the original instance.
   - **Data Migration and Testing:** Snapshots facilitate data migration between AWS regions or accounts and provide a snapshot of a known good state for testing purposes.

5. **Management and Access:** You can manage snapshots through the AWS Management Console, AWS Command Line Interface (CLI), or AWS SDKs. Snapshots can be tagged, copied, shared, and deleted as per your requirements.

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
