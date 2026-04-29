#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is VPC Peering?

- **VPC Peering** is a networking connection between two Virtual Private Clouds (VPCs) that allows you to route traffic between them using private IP addresses.
- Instances in either VPC can communicate with each other as if they are within the same network.
- VPC peering allows for seamless communication across different VPCs, whether they are in the same account, different accounts, or even different regions (inter-region VPC peering).

### VPC Peering Key Points

1. You can create a VPC peering connection between:
   - Your own VPCs.
   - A VPC in another AWS account.
   - A VPC in a different AWS Region.

2. A VPC peering connection is a one-to-one relationship between two VPCs.

3. You can create multiple VPC peering connections for each VPC.

4. Transitive peering relationships are not supported.

5. You can modify a VPC peering connection to enable instances in your VPC to communicate with linked EC2-Classic instances in the peer VPC.

6. There is no single point of failure for communication or a bandwidth bottleneck.

7. A VPC peering connection helps facilitate the transfer of data.

8. The traffic remains in the private IP space.

![VPC Peering Diagram  - Moole Muralidhara Reddy.png](https://github.com/vamsi-bhavani/vb-aws-course/blob/main/Day-15/images/Day%2015-VPC%20Peering%20Diagram%20-%20Moole%20Muralidhara%20Reddy%20-%20Tech%20World%20with%20Murali.png)

----
### Types of VPC Peering

1. **Intra-Account VPC Peering**:
  -  Intra-region VPC peering within the same AWS account
  -  Intra-region VPC peering within the different AWS account

2. **Inter-Account VPC Peering**:
  -  Inter-region VPC peering within the same AWS account
  -  Inter-region VPC peering within the different AWS account

### Intra-Region VPC Peering
Intra-region VPC peering refers to peering connections between VPCs within the same AWS region.

#### Characteristics:
- **Low Latency**: Since the VPCs are in the same region, the latency is typically very low.
- **High Bandwidth**: The bandwidth available for data transfer is high.
- **Reduced Costs**: Data transfer charges are generally lower compared to inter-region data transfer.

#### Use Cases:
- **Microservices Architecture**: Different microservices running in separate VPCs within the same region can communicate securely and efficiently.
- **Data Segregation**: Separate environments (e.g., development, testing, production) in different VPCs within the same region can interact when necessary.

### Inter-Region VPC Peering
Inter-region VPC peering refers to peering connections between VPCs in different AWS regions.

#### Characteristics:
- **Cross-Region Communication**: Enables communication between resources in different regions, which is crucial for global applications.
- **Higher Latency**: Since the VPCs are in different regions, the latency is higher compared to intra-region peering.
- **Higher Costs**: Data transfer costs between regions are higher compared to intra-region transfers.

#### Use Cases:
- **Global Applications**: Applications with a global user base that require resources in multiple regions to communicate.
- **Disaster Recovery**: Replicating data and services across regions for disaster recovery and business continuity.
