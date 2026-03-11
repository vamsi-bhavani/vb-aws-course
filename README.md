# AWS Zero to Hero Series Syllabus

## Prerequisites:
1. Windows/ Mac laptop
2. Basic Linux Commands

## Day 1: AWS Overview
- What is Cloud Computing?
- Benefits of Cloud Computing
- Types of Cloud Computing
- Types of Cloud Services
- What is AWS?
- Advantages of AWS
- Disadvantages of AWS
- AWS Global Infrastructure
- Regions
- Availability Zones
- Lab Session - Creation of an AWS account

## Day 2: Amazon Elastic Compute Cloud (EC2)

- What is Amazon EC2?
- Features of Amazon EC2
- Amazon EC2 Instance Types
- Lab Session - Creation of a Linux EC2 instance
- Lab Session - Downloading PuTTY and PuTTYgen
- Lab Session - Convert PEM to PPK file
- Lab Session - Connecting to Linux server
- Lab Session - Creation of a Windows EC2 instance
- Lab Session - Create an AMI from an Amazon EC2 Instance
- Lab Session - Creation of a Ubuntu EC2 instance
- What is an Elastic IP?
- Lab Session - Creating an Elastic IP and Attaching it to an EC2 Instance
- What is a Security Group?
- Lab Session - Creating a Security Group and Attaching it to an EC2 Instance
- Spot Instances, On-Demand Instances, Savings Plans, Reserved Instances, Dedicated Hosts, Scheduled Instances, Capacity Reservations
- Lab Session - Opening a support ticket with AWS
- Lab Session - Requesting Service Quotas in AWS
- Lab Session - Metadata and user data in EC2

## Day 3: AWS EBS (Elastic Block Storage)

- What is AWS EBS?
- Features of AWS EBS
- Types of EBS Volumes
- Lab Session - Creation of an EBS Volume
- Lab Session - Attach an EBS volume to a Linux EC2 instance
- Lab Session - Increase the size of an existing EBS volume on a Linux EC2 instance
- Lab Session - Attach an EBS volume to a Windows EC2 instance
- Lab Session - Increase the size of an existing EBS volume on a Windows EC2 instance
- Lab Session - Change the EBS volume type

## Day 4: AWS EBS Snapshot

- What is a Snapshot in AWS?
- Lab Session - Creation of a snapshot from an EC2 instance
- Lab Session - Creation of a snapshot from an EBS volume
- Lab Session - Creation of an AWS AMI from a snapshot
- Lab Session - Creation of an EBS volume from a snapshot
- Options in a Snapshot
- Lab Session - Deletion of Snapshots, Volumes, and AMIs

## Day 5: AWS IAM (Identity Access Management)

- What is AWS IAM?
- Features of AWS IAM
- Lab Session - AWS IAM Users
- Lab Session - AWS IAM User Groups
- What are AWS IAM Policies?
- Types of AWS IAM Policies
- Lab Session - Configuring AWS CLI
- Lab Session - Named profiles for the AWS CLI
- What is an IAM role?
- Lab Session - How to attach the IAM role to an EC2 instance?
- Root Account vs IAM user
- Lab Session - AWS IAM Password Policy
- Lab Session - Multi-Factor Authentication (MFA) for AWS IAM
- IAM Best Practices

## Day 6: AWS ASG (Auto Scaling Group)

- What is an Auto Scaling Group?
- Benefits of an Auto Scaling Group
- What is a Launch Configuration?
- Benefits of a Launch Configuration
- Drawbacks of a Launch Configuration
- Lab Session - Creation of an AWS Launch Configuration
- What is an AWS Launch Template?
- Benefits of an AWS Launch Template
- Lab Session - Creation of an AWS Launch Template
- Difference between a Launch Template and a Launch Configuration
- Lab Session - Creation of an ASG through an AWS Launch Configuration
- Lab Session - Creation of an ASG through an AWS Launch Template
- Lab Session - Enabling CloudWatch monitoring in an ASG
- Lab Session - Deletion of an ASG

## Day 7: AWS ELB (Elastic Load Balancing)

- What is AWS Elastic Load Balancing?
- Benefits of AWS Elastic Load Balancing
- What is an AWS Classic Load Balancer?
- Features of a Classic Load Balancer
- Lab Session - Creation of an AWS Classic Load Balancer
- Lab Session - Deletion of a Classic Load Balancer
- What is an AWS Target Group?
- What is a Listener?
- Lab Session - Creation of an AWS Target Group
- What is an AWS Application Load Balancer?
- Benefits of an AWS Application Load Balancer
- Lab Session - Creation of an Application Load Balancer
- Lab Session - Attaching an ALB to a new Auto Scaling group
- Lab Session - Deletion of an ALB
- What is an AWS Network Load Balancer?
- Benefits of an AWS Network Load Balancer
- Lab Session - Creation of an AWS Network Load Balancer
- Lab Session - Deletion of an NLB
- Difference between an ALB and an NLB
- Lab Session - Attaching an NLB  to an Auto Scaling group

## Day 8: AWS S3 (Simple Storage Service)

- What is AWS Simple Storage Service (S3)?
- Buckets and Objects in Amazon S3
- Types of storage classes in AWS S3
- Lab Session - Create an S3 bucket
- Lab Session - Upload objects to S3 using the AWS Console
- Lab Session - Upload objects to S3 using the AWS CLI
- S3 Versioning and enabling it
- Bucket Policy in Amazon S3
- Working with the Bucket Policy for S3 bucket
- S3 Bucket Lifecycle
- Hosting a static website using Amazon S3
- Presigned URLs in AWS S3
- Lab Session - Working with Presigned URLs in AWS S3
- Server-side encryption for Amazon S3 buckets
- Lab Session - Delete an S3 bucket

## Day 9: AWS VPC (Virtual Private Cloud) Part 1

- What is AWS VPC (Virtual Private Cloud)?
- Key features of AWS VPC
- CIDR (Classless Inter-Domain Routing)
- Lab Session - Choose the appropriate CIDR Block
- IPV4 and IPV6
- Subnets in AWS VPC
- Types of Subnets in AWS VPC
- Subnet sizing for IPV4
- Subnet routing in AWS VPC
- Route table in AWS VPC
- Components of a Route table
- Internet Gateway (IGW) in AWS VPC
- Lab Session - Overview of the Default VPC in AWS
- Lab Session - Create a customized VPC in AWS
- NAT Gateway and NAT Instance in AWS VPC
- Differences between NAT Gateway and NAT Instance
- Lab Session - Create a NAT Instance in AWS VPC
- Lab Session - Create a NAT Gateway in AWS VPC
- Lab Session - Delete a NAT Gateway in AWS VPC

## Day 10: AWS VPC (Virtual Private Cloud) Part 2

- Network Access Control List (NACL) in AWS VPC
- Lab Session - Create a Network Access Control List (NACL) in AWS VPC
- Security Group in AWS VPC
- Lab Session - Create a Security Group in AWS VPC
- Differences between NACL and Security Group in AWS VPC
- VPC Flow Logs and how to create them
- Lab Session - Enable VPC Flow Logs

## Day 11: AWS VPC (Virtual Private Cloud) Part 3

- Options for configuring an AWS VPC
- DHCP Option Set in AWS VPC
- DNS Hostnames and DNS Resolution in AWS VPC
- VPC Endpoints in AWS and types available
- Lab Session - Create a Gateway VPC Endpoint for S3 in AWS
- Prefix Lists in AWS VPC
- Elastic Network Interface (ENI) in AWS
- Lab Session - Create an ENI in AWS
- Lab Session - Delete an AWS VPC

## Day 12: AWS VPC Peering

- What is VPC Peering?
- Key aspects of VPC Peering
- Types of VPC Peering
- Lab Session - Intra-region VPC peering within the same AWS account
- Lab Session - Delete intra-region VPC peering within the same AWS account
- Lab Session - Establish intra-region VPC peering with a different AWS account
- Lab Session - Terminate intra-region VPC peering with a different AWS account
- Lab Session - Inter-region VPC peering within the same AWS account
- Lab Session - Remove inter-region VPC peering within the same AWS account
- Lab Session - Configure inter-region VPC peering with a different AWS account
- Lab Session - Remove inter-region VPC peering with a different AWS account

## Day 13: AWS CloudWatch

- What is CloudWatch?
- Key Features of CloudWatch
- Lab Session - Creating a log group in AWS CloudWatch
- Lab Session - Sending VPC Flow logs to a CloudWatch log group
- Lab Session - Setting up a CloudWatch alarm for an EC2 Instance

## Day 14: AWS CloudTrail

- What is AWS CloudTrail?
- Log event types in CloudTrail
- Lab Session - Setting up AWS CloudTrail to send logs to an S3 bucket
- Lab Session - Deletion of CloudTrail

## Day 15: AWS ECR (Elastic Container Registry)

- What is AWS ECR?
- Types of Repositories
- Components of Amazon ECR
- Features of Amazon ECR
- Lab Session - Creating an ECR repository in AWS
- Lab Session - Pushing a docker image to AWS ECR
- Lab Session - Setting up Lifecycle Policy in ECR
- Lab Session - Setting up Replication configuration in ECR

## Day 16: AWS EKS (Elastic Kubernetes Service)

- What is Amazon Elastic Kubernetes Service?
- How does Amazon EKS work?
- Lab Session - Installation of AWS CLI in Windows
- Lab Session - Installation of kubectl in Linux
- Lab Session - Installation of kubectl in Windows
- Lab Session - Creating an AWS IAM User
- Lab Session - Creating an EKS Cluster through the AWS Console
- Lab Session - Connecting to the EKS cluster
- Lab Session - Deploying a sample application in Kubernetes

## Day 17: AWS KMS

- What is AWS KMS?
- Features and benefits of KMS
- Different types of keys in KMS
- Lab Session - Creating a KMS key
- Lab Session - Encrypting an EBS volume using AWS KMS
- Lab Session - Deletion of KMS

## Day 18: AWS SES , SNS
- What is AWS SES?
- Lab Session - Creating AWS SES
- Lab Session - Deletion of AWS SES
- What is AWS SNS?
- Lab Session - Creating AWS SNS
- Lab Session - Deletion of AWS SNS


## Day 19: AWS RDS (Relational Database Service).

- What is RDS?
- Features of RDS
- RDS Subnet Group
- Parameter groups
- Option groups
- Amazon RDS storage types
- Lab Session - Creating a MySQL database in AWS RDS
- Lab Session - Connecting to the RDS MySQL from an AWS EC2 instance
- Lab Session - Installation of MySQL Workbench
- Lab Session - Connecting to the RDS MySQL from MySQL Workbench
- Lab Session - Deletion of RDS MySQL version

## Day 20: AWS Route53

- What is AWS Route53?
- Benefits of Route53
- What is a hosted zone in Route53?
- Types of hosted zones
- Lab Session - Creating a public hosted zone in AWS Route53
- What are records in a hosted zone?
- Types of records
- What is Routing Policy?
- Types of Routing policies
- Lab Session - Creating a record in a hosted zone
- Lab Session - Creating a private hosted zone in AWS Route53
- Lab Session - Configuring query logging for a Hosted Zone
- Lab Session - Deletion of a Hosted Zone

## Day 21: AWS ACM (AWS Certificate Manager)

- What is AWS ACM?
- Lab Session - Creating AWS ACM
- Lab Session - Integrating AWS ACM with an Application Load Balancer
- Lab Session - Deletion of AWS ACM

## Day 22: AWS EFS (Elastic File System)

- What is AWS EFS?
- Use cases of AWS EFS
- Types of AWS EFS Storage Classes
- Lab Session - Creation of AWS EFS
- Lab Session - Mounting AWS EFS in an EC2 instance
- Lab Session - Deletion of AWS EFS

## Day 23: AWS Systems Manager and Secret Manager

- What is AWS Systems Manager?
- Supported operating systems and machine types
- What is SSM Agent?
- Working with SSM Agent
- What is Parameter Store?
- Creating the Parameter Store
- What is Run Command?
- Setting up Run Command
- What is Patch Manager?
- Working with Patch Manager
- What is Secret Manager?
- Working with Secret Manager

## Day 24: AWS Calculator

- Introduction to AWS Calculator
- Overview of AWS Pricing
- Basic Navigation and Interface
- Cost Estimation for EC2 Instances, EBS, RDS
- Practical Exercises with Different Instance Types

## Day 25: AWS Billing and Cost Management

- What is AWS Billing and Cost Management?
- Features of AWS Billing and Cost Management
- Getting set up with Billing
- Setting up a budget

## Day 26: AWS Lambda

- What is AWs Lambda
- Why do we use AWs Lambda
- Automated AMI Backups for EC2 Instances Using Lambda

## Day 27: AWS API Gateway

- What is AWS API Gateway
- What is the usage of AWS API Gateway
- Creation of AWS API Gateway

## Day 28: AWS DynamoDB

- What is AWS DynamoDB
- Why do we use the DynamoDB?
- Creation of DynamoDB Tables

## Day 29: AWS SQS

- What is SQS?
- Types of Queues in SQS
- What is the difference between Standard Queue and FIFO Queue in SQS?
- Creation of AWS SQS

## Day 30: On-Premises to AWS Migration Process
- What is On-Premises
- End-to-End Cloud Migration Plan from On-Premises to AWS

# Conclusion
Congratulations on completing the "AWS Zero to Hero Series" curriculum! By now, you should have built a strong foundation in core AWS services and gained practical knowledge of cloud concepts. With this understanding, you are well prepared to explore more advanced AWS topics, work on real-world cloud architectures, and pursue AWS certifications.

Keep practicing, building projects, and exploring new AWS services to continue your cloud journey. The learning never stops in the world of cloud computing!
