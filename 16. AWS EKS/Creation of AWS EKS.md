#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |


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
Note: We are going to use the INFRA  VPC.
```
### Step 3: Create the KeyPair
```xml
KeyPair Name: infra
```

### Step 4: Create the AWS EKS Cluster Role
```xml
Name: infra-cluster-role
```
Attach the below policies for the cluster Role:
```xml
AmazonEKSClusterPolicy
```
### Step 5: Create the AWS EKS Cluster
```xml
Cluster Name: infra-cluster
```

### Step 6: Create the AWS EKS worker node Role
```xml
Name: infra-cluster-worker-node-role
```
Attach the below policies for the worker node Role:
```xml
AmazonEKSWorkerNodePolicy
AmazonEC2ContainerRegistryReadOnly
AmazonEKS_CNI_Policy
```

### Step 7: Create the Node Group
```xml
Worker group name: infra-cluster-worker-node
```

### Step 8: Configure the AWS CLI using Access Key ID & Secret Access Key
```bash
aws configure --profile infra
```

### Step 9: Connect to the EKS cluster using the command below
```bash
aws eks update-kubeconfig --name dev-cluster --region us-east-1 --profile infra
```

#### Congratulations: You have successfully created the AWS EKS Cluster.
