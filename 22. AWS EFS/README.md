#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is AWS EFS
AWS EFS stands for Amazon Elastic File System. It is a scalable, fully managed file storage service provided by Amazon Web Services (AWS) designed to provide shared access to file storage across multiple EC2 instances or containers.

### Key Features of AWS EFS:

1. **Scalability**:
   - AWS EFS can automatically scale its storage capacity up or down as you add or remove files without the need to provision or manage storage.

2. **Shared File Storage**:
   - EFS allows multiple EC2 instances and containers to access shared file storage concurrently, making it suitable for applications that require shared access to files.

3. **High Availability and Durability**:
   - EFS is designed for high availability and durability by storing data redundantly across multiple availability zones within a region.

4. **Performance**:
   - EFS provides low-latency performance for file operations and is optimized for a wide range of workloads, including big data analytics, media processing, and web serving.

5. **Integration**:
   - EFS integrates seamlessly with other AWS services like EC2, ECS (Elastic Container Service), EKS (Elastic Kubernetes Service), and Lambda, allowing you to use it as a file system for applications running on these services.

6. **Security**:
   - EFS supports encryption of data at rest and in transit, helping you meet security and compliance requirements.
----
### Benefits of AWS EFS:

- **Ease of Use**: AWS EFS is easy to deploy and manage, with no need to provision storage or manage file systems.

- **Scalability**: EFS scales automatically to petabytes of data, allowing you to grow your storage seamlessly with your application's needs.

- **Performance**: It provides low-latency performance suitable for a wide range of applications, including those requiring high throughput and low latency access to files.

- **Cost-effective**: You pay only for the storage used, without any upfront costs or minimum fees. EFS also offers cost savings compared to managing and scaling your own file storage infrastructure.

- **Reliability**: With data stored redundantly across multiple availability zones, EFS ensures high availability and durability for your file storage needs.
----
### Use Cases of AWS EFS

1. **Content Management:** Storing and sharing content files, documents, and media assets among multiple EC2 instances.

2. **Big Data Analytics:** Providing shared access to data files for analytics and processing across multiple instances.

3. **Web Serving:** Hosting web content that needs to be accessed by multiple web servers.

4. **Container Storage:** Storing persistent data for containers managed by Kubernetes or ECS.

5. **Database Backups:** Storing database backups and logs accessible by multiple instances.
----
### Types of AWS EFS Storage Classes

AWS EFS currently offers two storage classes:

1. **Standard Storage:** This is the default storage class that is suitable for workloads with a broad range of access patterns, including frequently accessed data and larger volumes of data.

2. **Infrequent Access (IA) Storage:** This storage class is optimized for workloads that access data less frequently but require cost-effective storage. It provides a lower price point compared to standard storage, with a retrieval fee when accessing data.
----
### Lab Session - Creation of AWS EFS

1. **Sign in to AWS Management Console:**
   - Navigate to the AWS EFS Dashboard at [AWS Management Console](https://console.aws.amazon.com/efs/).

2. **Create File System:**
   - Click on "Create file system."
   - Choose the appropriate settings, including the VPC and subnets where you want to create the EFS.
   - Optionally configure performance mode and encryption settings.
   - Click "Create file system" to create the EFS.
----
### Lab Session - Mounting AWS EFS in an EC2 Instance

1. **Install NFS Client on EC2 Instance:**
   - SSH into your EC2 instance.
   - Install NFS client software. For example, on Amazon Linux or CentOS, you can run `sudo yum install -y nfs-utils`.

2. **Retrieve File System ID:**
   - Go to the AWS EFS Dashboard.
   - Select your EFS file system and note down the File System ID.

3. **Mount EFS to EC2 Instance:**
   - Create a mount point on your EC2 instance. For example, `sudo mkdir /mnt/efs`.
   - Mount the EFS file system to your instance using the File System ID. For example:
     ```
     sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 <File System ID>:/ /mnt/efs
     ```
   - Replace `<File System ID>` with your actual File System ID.
----
### Lab Session - Deletion of AWS EFS

1. **Sign in to AWS Management Console:**
   - Navigate to the AWS EFS Dashboard at [AWS Management Console](https://console.aws.amazon.com/efs/).

2. **Select EFS File System:**
   - Select the EFS file system you want to delete.

3. **Delete EFS File System:**
   - Click on "Actions" -> "Delete file system."
   - Confirm the deletion when prompted.

### Summary

AWS EFS provides scalable, shared file storage for AWS cloud environments, suitable for a variety of use cases including content management, big data analytics, and container storage. By creating, mounting, and managing EFS file systems, you can efficiently store and share files across multiple EC2 instances while benefiting from AWS's scalability and reliability.
