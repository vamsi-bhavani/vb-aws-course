#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |


## What is AWS EKS?

- Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service that simplifies running Kubernetes on AWS without needing to install and operate your own Kubernetes control plane or nodes.
- Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.
- EKS provides a highly available, secure, and scalable Kubernetes environment for applications.

## Key Features of AWS EKS

1. **Managed Kubernetes Control Plane**
   - AWS EKS manages the Kubernetes control plane, including the API servers and the etcd database. This ensures high availability and scalability without the operational overhead.

2. **Integration with AWS Services**
   - EKS integrates with various AWS services such as IAM for security, CloudWatch for monitoring, and AWS Load Balancer for load balancing, simplifying the management of Kubernetes applications.

3. **Security and Compliance**
   - EKS offers robust security features including VPC isolation, IAM roles for service accounts, and integration with AWS Key Management Service (KMS) for secrets encryption.

4. **Scalability and Performance**
   - EKS supports scaling both the control plane and worker nodes seamlessly. It allows for automatic scaling of applications with Kubernetes’ built-in Horizontal Pod Autoscaler.

5. **High Availability**
   - EKS runs the Kubernetes control plane across multiple AWS Availability Zones, ensuring high availability and resilience against failures.

6. **Flexibility**
   - EKS supports a variety of Kubernetes add-ons, such as the AWS VPC CNI plugin for networking, and is compatible with existing Kubernetes tools and applications.

## Benefits of Using AWS EKS

1. **Ease of Use**
   - EKS simplifies the process of running Kubernetes on AWS by managing the control plane, allowing developers to focus on building and deploying applications rather than managing infrastructure.

2. **Cost Efficiency**
   - With EKS, you only pay for the worker nodes and the EKS service. This can be more cost-effective compared to running a self-managed Kubernetes cluster, especially when considering the reduced operational overhead.

3. **Reliability**
   - Leveraging AWS’s global infrastructure, EKS provides a reliable environment for running production-grade Kubernetes workloads, ensuring minimal downtime and robust performance.

4. **Security**
   - EKS provides multiple layers of security, including network isolation, IAM policies, and integration with AWS security services, ensuring that your applications are secure.

5. **Community and Ecosystem**
   - As Kubernetes is an open-source project, EKS benefits from a large and active community, offering a wealth of resources, tools, and extensions to enhance your Kubernetes experience.

6. **Seamless Integration**
   - EKS integrates seamlessly with other AWS services, allowing you to take advantage of AWS’s comprehensive suite of services for databases, machine learning, analytics, and more.
----
## Setting up AWS EKS Step-by-Step Guide

### Step 1: Create the IAM user and provide Admin Access
```xml
Username: moole
```

### Step 1.1: Login to the AWS Console using moole user
```xml
UserName: moole
```

### Step 2: Create the VPC and 2 public subnets
```xml
Note: We are going to use the default VPC so we don't need to create the VPC.
```

### Step 3: Create the KeyPair
```xml
KeyPair Name: dev
```

### Step 4: Create the AWS EKS Cluster Role
```xml
Name: dev-cluster-role
```
Attach the below policies for the cluster Role:
```xml
AmazonEKSClusterPolicy
```
### Step 5: Create the AWS EKS Cluster
```xml
Cluster Name: dev-cluster
```

### Step 6: Create the AWS EKS worker node Role
```xml
Name: dev-cluster-worker-node-role
```
Attach the below policies for the worker node Role:
```xml
AmazonEKSWorkerNodePolicy
AmazonEC2ContainerRegistryReadOnly
AmazonEKS_CNI_Policy
```

### Step 7: Create the Node Group
```xml
Worker group name: dev-cluster-worker-node
```

### Step 8: Configure the AWS CLI using Access Key ID & Secret Access Key
```bash
aws configure --profile dev
```

### Step 9: Connect to the EKS cluster using the command below
```bash
aws eks update-kubeconfig --name dev-cluster --region us-east-1 --profile dev
```

#### Congratulations: You have successfully created the AWS EKS Cluster.
```
