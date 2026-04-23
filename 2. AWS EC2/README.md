#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is Amazon EC2?

Amazon EC2 (Elastic Compute Cloud) is a web service that provides resizable compute capacity in the cloud. It allows you to obtain and configure virtual servers (known as instances) to run your applications, scalable depending on your needs.

### Features of Amazon EC2

1. **Scalability:** Easily scale compute resources up or down as needed.
2. **Variety of Instances:** Choose from various instance types optimized for different use cases (e.g., compute-optimized, memory-optimized).
3. **Security:** Secure instances with built-in security groups and key pairs.
4. **Flexible Pricing:** Pay only for the compute capacity you actually use.
5. **Integration:** Easily integrate with other AWS services and third-party tools.
----
### Amazon EC2 Instance Types and Use Cases

Amazon EC2 offers a variety of instance types to cater to different workloads and performance needs. Here are some common instance types along with their use cases:

1. **General Purpose Instances (e.g., M5, T3)**
   - **Description**: These instances offer a balance of compute, memory, and networking resources.
   - **Use Cases**:
     - Web servers
     - Small databases
     - Development environments

2. **Compute-Optimized Instances (e.g., C5, C6g)**
   - **Description**: These instances are optimized for compute-intensive workloads.
   - **Use Cases**:
     - High-performance computing
     - Scientific modeling
     - Batch processing

3. **Memory-Optimized Instances (e.g., R5, X1)**
   - **Description**: These instances are optimized for memory-intensive workloads.
   - **Use Cases**:
     - In-memory databases
     - Big data analytics
     - High-performance computing

4. **Storage-Optimized Instances (e.g., D2, I3)**
   - **Description**: These instances are optimized for storage-intensive workloads.
   - **Use Cases**:
     - NoSQL databases
     - Data warehousing
     - Elasticsearch

5. **GPU Instances (e.g., G4, P3)**
   - **Description**: These instances provide access to high-performance GPUs for graphics-intensive workloads.
   - **Use Cases**:
     - Video rendering
     - Machine learning
     - Gaming

6. **FPGA Instances (e.g., F1)**
   - **Description**: These instances are designed for the acceleration of custom hardware logic.
   - **Use Cases**:
     - Genomics analysis
     - Financial modeling
     - Real-time video processing

### Key Points

- **Instance Sizes**: Each instance type is available in different sizes, offering varying amounts of CPU, memory, storage, and networking capacity.
- **Customizable**: Users can select the instance type and size that best suits their specific workload requirements.
----
### Lab Session - Creation of a Linux EC2 Instance

1. **Sign in to AWS Management Console:** Navigate to the EC2 Dashboard.
2. **Launch Instance:** Click on "Launch Instance" to start the instance creation process.
3. **Choose AMI:** Select a Linux-based Amazon Machine Image (AMI) such as Amazon Linux or Ubuntu.
4. **Choose Instance Type:** Select an instance type based on your requirements (e.g., t2.micro for a free-tier eligible instance).
5. **Configure Instance:** Configure instance details, storage, tags, and security groups.
6. **Review and Launch:** Review your instance configuration and launch it.
7. **Connect to Instance:** Use SSH to connect to your Linux instance (details for connecting will vary based on your operating system).
----
### Lab Session - Downloading PuTTY and PuTTYgen

PuTTY is a popular SSH client for Windows, while PuTTYgen is used to generate and convert SSH keys.

1. **Download PuTTY:** Go to the PuTTY download page and download the PuTTY installer.
2. **Download PuTTYgen:** Download PuTTYgen from the same page.
3. **Install PuTTY:** Run the PuTTY installer and follow the installation instructions.
4. **Run PuTTYgen:** Launch PuTTYgen to generate or convert SSH keys as needed.

### Lab Session - Convert PEM to PPK file

To convert a PEM file (typically used in Linux) to a PPK file (used in PuTTY for Windows):

1. **Open PuTTYgen:** Launch PuTTYgen.
2. **Load PEM Key:** Click on "Load" and select your PEM file.
3. **Save Private Key:** Click on "Save private key" to save the key in PPK format.
----
### Lab Session - Connecting to Linux server

Use SSH to connect to your Linux server:

1. **Open Terminal (Linux/Mac) or PuTTY (Windows):** Launch your SSH client.
2. **SSH Command:** Use the SSH command with the instance's public IP address or DNS name and your private key file:
   ```
   ssh -i /path/to/private-key.pem ec2-user@public-ip-address
   ```
   Replace `/path/to/private-key.pem` with the path to your PEM file, `ec2-user` with your instance's username (may vary by AMI), and `public-ip-address` with your instance's public IP address or DNS.

----
### Lab Session - Creation of a Windows EC2 Instance

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Launch Instance:**
   - Click on "Launch Instance" to start the instance creation process.

3. **Choose AMI:**
   - In the "Step 1: Choose an Amazon Machine Image (AMI)" section, click on "AWS Marketplace" on the left sidebar.
   - Search for "Windows Server" and select a suitable Windows Server AMI. Ensure you choose a version that suits your requirements (e.g., Windows Server 2019 Base).

4. **Choose Instance Type:**
   - Select an instance type based on your requirements (e.g., t2.micro for a free-tier eligible instance). Click "Next: Configure Instance Details" when ready.

5. **Configure Instance:**
   - Configure instance details such as:
     - Number of instances to launch.
     - Network settings (usually default VPC and subnet settings are fine).
     - Optionally, configure advanced settings like IAM role, monitoring, and instance shutdown behavior. Click "Next: Add Storage" when ready.

6. **Add Storage:**
   - Specify the storage requirements for your instance. The default settings are typically sufficient for basic needs. Click "Next: Add Tags" when ready.

7. **Add Tags:**
   - Optionally, add tags to your instance for easier identification and management. Click "Next: Configure Security Group" when ready.

8. **Configure Security Group:**
   - Configure security group settings to control inbound and outbound traffic to your instance. At least allow RDP (Remote Desktop Protocol) access (port 3389) for Windows instances. You may also want to allow HTTP (port 80) or HTTPS (port 443) depending on your application needs.

9. **Review Instance Launch:**
   - Review all your instance details. Ensure everything is configured correctly. Click "Launch" when ready.

10. **Select Key Pair:**
    - In the pop-up window, select an existing key pair or create a new key pair. Note that for Windows instances, you typically do not need to use SSH keys directly. Instead, you will use RDP to connect.

11. **Access Windows Instance:**
    - Once the instance is launched, note the public IP address or DNS name of your instance from the EC2 dashboard.

12. **Connect to Windows Instance:**
    - Use Remote Desktop Protocol (RDP) to connect to your Windows instance. On your local machine:
      - Search for "Remote Desktop Connection" in the Start menu (Windows).
      - Enter the public IP address or DNS name of your instance. Click "Connect."
      - Enter the credentials (username and password) specified during instance launch.

13. **Start Using Windows Instance:**
    - You are now connected to your Windows EC2 instance. Start configuring Windows settings, installing applications, and exploring the capabilities of Windows on AWS.
----

### Lab Session - Create an AMI from an Amazon EC2 Instance

1. **Select Instance:** In the EC2 Dashboard, select the instance you want to create an AMI from.
2. **Actions > Image and templates > Create image (AMI):** Click on "Actions," then "Image and templates," and finally "Create image (AMI)."
3. **Enter Image Details:** Provide a name and description for your AMI.
4. **Create Image:** Click "Create image" to initiate the AMI creation process.
5. **Use AMI:** Once created, you can use this AMI to launch new instances with the same configuration as the original instance.

### Lab Session - Creation of a Ubuntu EC2 Instance

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Launch Instance:**
   - Click on "Launch Instance" to start the instance creation process.

3. **Choose AMI:**
   - In the "Step 1: Choose an Amazon Machine Image (AMI)" section, search for "Ubuntu" in the search bar.
   - Select the Ubuntu AMI of your choice (e.g., Ubuntu Server 20.04 LTS).

4. **Choose Instance Type:**
   - Select an instance type based on your requirements (e.g., t2.micro for a free-tier eligible instance). Click "Next: Configure Instance Details" when ready.

5. **Configure Instance:**
   - Configure instance details such as:
     - Number of instances to launch.
     - Network settings (usually default VPC and subnet settings are fine).
     - Optionally, configure advanced settings like IAM role, monitoring, and instance shutdown behavior. Click "Next: Add Storage" when ready.

6. **Add Storage:**
   - Specify the storage requirements for your instance. The default settings are typically sufficient for basic needs. Click "Next: Add Tags" when ready.

7. **Add Tags:**
   - Optionally, add tags to your instance for easier identification and management. Click "Next: Configure Security Group" when ready.

8. **Configure Security Group:**
   - Configure security group settings to control inbound and outbound traffic to your instance. At least allow SSH (port 22) access for Linux instances. You may also want to allow HTTP (port 80) or HTTPS (port 443) depending on your application needs.

9. **Review Instance Launch:**
   - Review all your instance details. Ensure everything is configured correctly. Click "Launch" when ready.

10. **Select Key Pair:**
    - In the pop-up window, select an existing key pair or create a new key pair. Key pairs are used to securely connect to your instance via SSH.

11. **Access Instance:**
    - Once the instance is launched, note the public IP address or DNS name of your instance from the EC2 dashboard.

12. **Connect to Ubuntu Instance:**
    - Use SSH to connect to your Ubuntu instance. Open a terminal on your local machine (Linux/Mac) or use PuTTY on Windows:
      ```
      ssh -i /path/to/private-key.pem ubuntu@public-ip-address
      ```
      Replace `/path/to/private-key.pem` with the path to your private key file, `ubuntu` with the default username for Ubuntu instances, and `public-ip-address` with the public IP address of your instance.

13. **Start Using Ubuntu Instance:**
    - You are now connected to your Ubuntu EC2 instance. Start installing applications, configuring services, and exploring the capabilities of Ubuntu on AWS.
----
### AWS Elastic IP (EIP)

AWS Elastic IP (EIP) is a static, public IP address that can be allocated to your AWS resources, such as Amazon EC2 instances, to enable communication with the internet.

#### Key Features and Benefits:

1. **Static IP Address**
   - Unlike dynamic IP addresses that can change when an instance is stopped or started, an EIP remains constant.

2. **Persistent Association**
   - An EIP remains associated with your AWS account until you choose to release it, ensuring continuity of services and reliable access.

3. **Flexibility**
   - EIPs can be remapped to another instance within your account, allowing you to quickly recover from instance or availability zone failures.

4. **Availability**
   - EIPs enable your AWS resources to have a fixed public IP address, facilitating communication with the internet or external systems.

#### Use Cases:

1. **Web Hosting**
   - Assign an EIP to your EC2 instance running a web server to ensure users can reliably access your website.

2. **Disaster Recovery**
   - Quickly remap an EIP to a standby instance in case of failure, minimizing downtime and ensuring business continuity.

### **Important Considerations**

* **Cost**

  * **All public IPv4 addresses in AWS (including Elastic IPs) are now charged**, whether they are:

    * Associated with a running instance
    * Associated with a stopped instance
    * Or not associated with any resource
  * AWS charges per hour for each public IPv4 address.

* **Limits**

  * AWS still limits the number of Elastic IPs per region (default is usually 5).
  * You can request a quota increase if needed.

* **Best Practices**

  * Use Elastic IPs only when necessary.
  * Release unused Elastic IPs to avoid ongoing charges.
  * Consider using alternatives like:
    * AWS Load Balancers
    * Private IPs + NAT Gateway
    * DNS (Route 53) instead of static IPs where possible

---

#### How to Allocate and Associate an EIP:

1. **Allocate an EIP**:
   - In the AWS Management Console, go to the EC2 Dashboard.
   - Click on "Elastic IPs" in the sidebar.
   - Click the "Allocate new address" button and confirm.

2. **Associate an EIP with an EC2 Instance**:
   - Select the allocated EIP.
   - Click on the "Actions" dropdown and select "Associate address."
   - Choose the instance or network interface you want to associate the EIP with, and confirm the association.

----
### AWS Security Groups

A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic.

#### Key Features and Benefits:

1. **Inbound and Outbound Rules**
   - **Inbound Rules**: Control the incoming traffic to your instance.
   - **Outbound Rules**: Control the outgoing traffic from your instance.

2. **Default Security Group**
   - If you don't specify a security group when you launch an instance, Amazon EC2 uses the default security group.

3. **Flexible Rule Management**
   - You can add, modify, or remove rules in a security group at any time.
   - New and modified rules are automatically applied to all instances associated with the security group.

4. **Multiple Security Groups**
   - You can specify one or more security groups when you launch an instance.
   - Amazon EC2 evaluates all rules from all security groups associated with an instance to decide whether to allow traffic.

#### How Security Groups Work:

- **Creating Security Groups**:
  - In the AWS Management Console, go to the EC2 Dashboard.
  - Click on "Security Groups" in the sidebar.
  - Click the "Create security group" button and define the group name, description, and VPC.
  - Add inbound and outbound rules as needed.

- **Inbound and Outbound Rules**:
  - **Inbound Rules**: Define which traffic is allowed to reach your instance. Example: Allow SSH access on port 22 from a specific IP range.
  - **Outbound Rules**: Define which traffic is allowed to leave your instance. Example: Allow all outbound traffic to any destination.

- **Modifying Security Groups**:
  - Select the security group you want to modify.
  - Add, edit, or remove inbound and outbound rules as necessary.
  - Changes are automatically applied to all associated instances.

#### Important Considerations:

- **Stateful Nature**:
  - Security groups are stateful, meaning if you allow an incoming request from an IP, the response is automatically allowed.

- **Evaluation of Rules**:
  - When Amazon EC2 decides whether to allow traffic to reach an instance, it evaluates all of the rules from all of the security groups associated with the instance.

- **Changes Applied Automatically**:
  - Any changes to security group rules are immediately applied to all associated instances without needing to restart them.

By effectively managing security groups, you can enhance the security of your AWS environment by controlling access to and from your EC2 instances.

----
### Spot Instances, On-Demand Instances, Savings Plans, Reserved Instances, Dedicated Hosts, Scheduled Instances, Capacity Reservations

Amazon EC2 offers a variety of instance purchasing options to help you optimize costs and meet your specific workload requirements. Here are the main options:

1. **Spot Instances**
   - **Description**: Allows you to bid on unused EC2 capacity at potentially lower prices than On-Demand instances.
   - **Use Cases**:
     - Fault-tolerant workloads
     - Big data analysis
     - Batch processing
     - CI/CD workloads

2. **On-Demand Instances**
   - **Description**: Allows you to pay for compute capacity by the hour or second, with no long-term commitments.
   - **Use Cases**:
     - Short-term, spiky, or unpredictable workloads
     - Applications being developed or tested for the first time

3. **Savings Plans**
   - **Description**: Offers significant savings over On-Demand instances in exchange for committing to a consistent amount of usage (measured in USD per hour) for a 1- or 3-year term.
   - **Use Cases**:
     - Long-term, stable workloads
     - Ability to commit to consistent usage for cost savings

4. **Reserved Instances**
   - **Description**: Provides a significant discount (up to 75%) compared to On-Demand pricing in exchange for a 1- or 3-year commitment.
   - **Use Cases**:
     - Steady-state workloads
     - Applications with predictable usage patterns

5. **Dedicated Hosts**
   - **Description**: Physical EC2 servers dedicated for your use, helping you address compliance requirements and reduce costs by using your existing server-bound software licenses.
   - **Use Cases**:
     - Licensing requirements that do not support multi-tenancy or cloud deployments
     - Compliance and regulatory requirements

6. **Scheduled Instances**
   - **Description**: Allows you to purchase instances that are always available on the specified recurring schedule, matching your capacity needs.
   - **Use Cases**:
     - Predictable workloads that require a fraction of a day, week, or month
     - Batch processing during specific times

7. **Capacity Reservations**
   - **Description**: Ensures that you have reserved capacity for your EC2 instances in a specific Availability Zone for any duration.
   - **Use Cases**:
     - Applications requiring guaranteed compute capacity
     - Business-critical workloads that need to avoid capacity constraints

### Summary

- **Spot Instances**: Cost-effective for fault-tolerant and flexible workloads.
- **On-Demand Instances**: Best for short-term, unpredictable workloads without upfront commitment.
- **Savings Plans**: Offer cost savings for consistent usage over a long term.
- **Reserved Instances**: Suitable for predictable and steady-state applications with long-term commitments.
- **Dedicated Hosts**: Address licensing and compliance requirements with dedicated physical servers.
- **Scheduled Instances**: Ideal for predictable workloads requiring specific schedules.
- **Capacity Reservations**: Guarantee capacity for business-critical applications.

Each of these options provides different pricing models and flexibility, allowing you to optimize costs while meeting the specific needs of your workloads.

----
### Lab Session - Opening a Support Ticket with AWS

### Example Description for an EBS Issue: Unable to Mount in Linux Server

Here is an example of a detailed description you might provide for an issue where you are unable to mount an EBS volume on a Linux server:

---

**Service**: Elastic Block Store (EBS)  
**Category**: Volume Availability  
**Severity**: System impaired  

**Description**:
I am experiencing an issue with mounting an EBS volume on my Linux server. The details are as follows:

- **Volume ID**: vol-0abc12345def67890
- **Instance ID**: i-0abc12345def67890
- **Issue**: Unable to mount the EBS volume to the EC2 instance.

Please assist in diagnosing and resolving this issue, as it is preventing us from accessing important data on the EBS volume. Can we have a quick call to discuss this further?

----
### What is Metadata in Amazon EC2?

- **Metadata** refers to instance-specific information that is available from within the instance itself.
- AWS provides this through a special metadata service accessible at `http://169.254.169.254/latest/meta-data/`.

**How does it work?**
- Metadata is not passed to the instance like userdata; instead, the instance retrieves it by making HTTP requests to the metadata service.

**Common Use Cases:**
1. **Retrieve Instance Information**: Such as instance ID, IP address, AMI ID, or region.
2. **Dynamic Configuration**: Use metadata to configure the instance dynamically based on its environment.

**Example Metadata Categories:**
- `ami-id`: AMI ID of the instance.
- `instance-id`: Unique ID of the instance.
- `public-ipv4`: Public IP address assigned to the instance.
- `security-groups`: Security groups associated with the instance.

**Retrieving Metadata Example:**
To get the instance ID:
```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

---
### What is User Data in Amazon EC2?

- **Userdata** refers to a script or configuration passed to an EC2 instance during its launch.
- It is often used to perform automated actions when an instance starts for the first time.

**How does it work?**
- The script is executed by the cloud-init service (on Linux instances) or EC2Config/EC2Launch (on Windows instances).
- The execution occurs only during the first boot.

**Common Use Cases:**
1. **Install Software**: Automatically install packages or applications.
2. **Run Commands**: Execute initialization scripts, such as setting up a web server or database.
3. **Configuration**: Apply specific configurations, such as creating a user or modifying system settings.
4. **Download Files**: Retrieve files or dependencies from the internet or S3 buckets.

**Example:**
Auto-Tag EC2 Instance Using User Data Script:
```bash
#!/bin/bash

# Update the package index
yum update -y

# Fetch the instance ID from metadata
INSTANCE_ID=$(curl -s -H "X-aws-ec2-metadata-token: $(curl -s -X PUT -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" http://169.254.169.254/latest/api/token)" http://169.254.169.254/latest/meta-data/instance-id)

# Fetch the region from metadata
REGION=$(curl -s -H "X-aws-ec2-metadata-token: $(curl -s -X PUT -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" http://169.254.169.254/latest/api/token)" http://169.254.169.254/latest/meta-data/placement/region)

# Define the tag value
TAG_VALUE="ldev-eks-$INSTANCE_ID"

# Set the tag for the instance
aws ec2 create-tags --resources $INSTANCE_ID --tags Key=Name,Value=$TAG_VALUE --region $REGION
```
---

### Key Differences

| Aspect          | Userdata                                 | Metadata                                    |
|------------------|------------------------------------------|--------------------------------------------|
| Purpose          | Provide initialization scripts          | Retrieve instance-specific information     |
| Execution        | Run once at the first boot              | Accessed dynamically during runtime        |
| Scope            | Custom scripts or configurations        | Built-in AWS-provided instance details     |
| Accessibility    | Passed during instance launch           | Retrieved via HTTP calls inside the instance |
