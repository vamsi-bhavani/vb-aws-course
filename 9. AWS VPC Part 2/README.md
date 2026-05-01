#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### NAT Gateway and NAT Instance in AWS VPC

**NAT (Network Address Translation) Gateway** and **NAT Instance** are used to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating connections with those instances.

### NAT Gateway

**NAT Gateway** is a managed service provided by AWS that enables instances in a private subnet to connect to the internet. It is highly available and scalable, automatically managed by AWS.

**Key Features of NAT Gateway:**
- **Managed Service:** AWS manages the NAT Gateway, ensuring high availability and scalability.
- **Automatic Scaling:** It automatically scales up to meet bandwidth requirements.
- **Ease of Use:** Simple to set up and requires minimal maintenance.
- **High Availability:** Deployed in a specific availability zone but can be set up with multiple NAT Gateways across different zones for redundancy.
  
### NAT Instance

**NAT Instance** is an EC2 instance configured to perform network address translation (NAT) for instances in a private subnet.

**Key Features of NAT Instance:**
- **Customizable:** You can customize the instance to meet specific requirements.
- **Scalability:** Requires manual intervention to scale.
- **Management:** Requires management of instance lifecycle, including updates and monitoring.
- **High Availability:** High availability must be manually configured using scripts or services like Auto Scaling.

### Differences between NAT Gateway and NAT Instance

| Feature                | NAT Gateway                   | NAT Instance                  |
|------------------------|-------------------------------|-------------------------------|
| **Management**         | Managed by AWS                | Managed by the user           |
| **Scalability**        | Automatic scaling             | Manual scaling required       |
| **High Availability**  | Built-in high availability    | User must configure           |
| **Ease of Setup**      | Simple, managed setup         | Complex, user-managed setup   |
| **Cost**               | Pay per hour and data transfer| Pay per instance hour         |
| **Customizability**    | Limited customization         | Highly customizable           |

----
### Lab Session - Create a NAT Gateway in AWS VPC

1. **Create a NAT Gateway:**
   - Navigate to the VPC dashboard.
   - In the left pane, choose "NAT Gateways".
   - Click on "Create NAT Gateway".
   - Select the public subnet in which the NAT Gateway will be created.
   - Allocate a new Elastic IP for the NAT Gateway.
   - Click on "Create NAT Gateway".

2. **Update Route Tables:**
   - Navigate to the Route Tables section in the VPC dashboard.
   - Select the route table associated with the private subnet.
   - Add a new route with `0.0.0.0/0` as the destination and the NAT Gateway ID as the target.
