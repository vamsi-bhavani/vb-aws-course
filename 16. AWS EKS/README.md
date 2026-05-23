#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is Amazon EKS?

Amazon EKS (Elastic Kubernetes Service) is a managed Kubernetes service provided by AWS. It helps us run Kubernetes clusters without managing the control plane.

Kubernetes is an open-source platform used to deploy, scale, and manage containerized applications.

In EKS, AWS takes care of the control plane components like API server and etcd, while we focus on deploying and managing applications.

EKS provides a secure, scalable, and highly available environment for running production workloads.


##  Key Features of EKS

### 1. Managed Control Plane

AWS fully manages Kubernetes master components.

- **Example 1:** No need to install or patch API servers
- **Example 2:** No need to manage etcd backups or failures


### 2. Integration with AWS Services

EKS tightly integrates with AWS ecosystem.

- **Example 1:** IAM is used for authentication and authorization
- **Example 2:** CloudWatch is used for logs and monitoring


### 3. High Availability

EKS control plane runs across multiple Availability Zones.

- **Example 1:** If one AZ fails, cluster still runs
- **Example 2:** API server remains accessible without downtime


### 4. Scalability

Supports scaling at both pod and infrastructure level.

- **Example 1:** Horizontal Pod Autoscaler increases pods based on CPU
- **Example 2:** Cluster Autoscaler automatically adds/removes EC2 nodes

### 5. Security

EKS provides multiple security layers.

- **Example 1:** IAM Roles for Service Accounts (IRSA) for secure access
- **Example 2:** Secrets encrypted using AWS KMS


### 6. Networking

Uses AWS VPC for networking.

- **Example 1:** Each pod gets IP from VPC

### 7. Flexibility

Supports standard Kubernetes tools and add-ons.

- **Example 1:** Helm charts can be deployed easily
- **Example 2:** Tools like Prometheus, Grafana, ArgoCD can be used

### 8. Multiple Compute Options

Supports EC2 and Fargate.

- **Example 1:** EC2 for full control and customization
- **Example 2:** Fargate for serverless container execution


##  Benefits of EKS

### 1. Reduced Operational Effort

AWS manages control plane.

- **Example 1:** No need to maintain master nodes
- **Example 2:** No need to handle control plane upgrades

### 2. Reliability

Built on AWS global infrastructure.

- **Example 1:** Multi-AZ architecture ensures uptime
- **Example 2:** Suitable for production workloads

### 3. Security

Strong integration with AWS security services.

- **Example 1:** IAM-based access control
- **Example 2:** Private clusters inside VPC

### 4. Cost

Cost depends on architecture and usage.

- **Example 1:** Pay for cluster + EC2 + Load Balancer
- **Example 2:** Extra cost for storage and data transfer

### 5. Ecosystem Support

Based on Kubernetes open-source ecosystem.

- **Example 1:** Supports all Kubernetes tools
- **Example 2:** Large community and documentation

