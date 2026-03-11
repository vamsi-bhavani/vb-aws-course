#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is AWS Elastic Load Balancing?

AWS Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, IP addresses, and Lambda functions, to ensure high availability and fault tolerance for your applications.

### Benefits of AWS Elastic Load Balancing

1. **High Availability:** Distributes traffic across multiple instances or targets, reducing the risk of overloading any single resource.
2. **Fault Tolerance:** Automatically routes traffic away from unhealthy targets to healthy ones.
3. **Scalability:** Handles varying traffic loads by scaling resources up or down automatically.
4. **Security:** Provides SSL/TLS termination to encrypt traffic and integration with AWS WAF for web application firewall protection.
----
### What is an AWS Classic Load Balancer?

AWS Classic Load Balancer (CLB) is the original load balancer offering from AWS, primarily designed for applications that were built within the EC2-Classic network. It supports both EC2-Classic and EC2-VPC platforms.

### Features of a Classic Load Balancer

1. **Layer 4 and Layer 7 Load Balancing:** Supports both TCP (Layer 4) and HTTP/HTTPS (Layer 7) traffic.
2. **Sticky Sessions:** Supports session affinity, directing requests to the same instance.
3. **Health Checks:** Monitors the health of registered instances and routes traffic only to healthy instances.
4. **Cross-Zone Load Balancing:** Distributes traffic evenly across instances in multiple Availability Zones.
----
### Lab Session - Creation of an AWS Classic Load Balancer

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Classic Load Balancer:**
   - Click on "Load Balancers" in the left sidebar under "EC2."
   - Click on "Create Load Balancer" and choose "Classic Load Balancer."
   - Configure load balancer settings, including listeners, availability zones, security settings, and health checks.
   - Complete the creation and note the DNS name provided for your Classic Load Balancer.
----
### Lab Session - Deletion of a Classic Load Balancer

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Delete Classic Load Balancer:**
   - Click on "Load Balancers" in the left sidebar under "EC2."
   - Select the Classic Load Balancer you want to delete.
   - Click on "Actions > Delete" and confirm the deletion.
----
### What is an AWS Target Group?

An AWS Target Group is used with Application Load Balancers and Network Load Balancers to route requests to one or more registered targets, such as EC2 instances, IP addresses, or Lambda functions, based on routing rules.

### What is a Listener?

A Listener is a process that checks for connection requests from clients and manages traffic for one or more ports, forwarding requests to target groups associated with AWS load balancers based on rules defined for each listener.

### Lab Session - Creation of an AWS Target Group

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Target Group:**
   - Click on "Target Groups" in the left sidebar under "Load Balancing."
   - Click on "Create target group" and follow the wizard:
     - Define target group name, protocol (HTTP, HTTPS, TCP, etc.), and port.
     - Configure health checks to monitor the health of targets.
     - Register targets (EC2 instances, IP addresses, or Lambda functions) with the target group.
     - Complete the creation of the target group.
----
### What is an AWS Application Load Balancer?

AWS Application Load Balancer (ALB) operates at the application layer (Layer 7) and directs traffic based on URL routing rules, allowing multiple applications to be hosted on a single load balancer. It supports advanced routing, SSL termination, and content-based routing.

### Benefits of an AWS Application Load Balancer

1. **Content-Based Routing:** Routes traffic based on content of the request (e.g., URL path).
2. **Host-Based Routing:** Routes traffic based on host headers.
3. **Path-Based Routing:** Routes traffic based on URL paths.
4. **WebSocket Support:** Supports WebSocket traffic.
5. **Integrated with AWS WAF:** Provides protection against common web exploits and SQL injection.
----
### Lab Session - Creation of an Application Load Balancer

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Application Load Balancer:**
   - Click on "Load Balancers" in the left sidebar under "EC2."
   - Click on "Create Load Balancer" and choose "Application Load Balancer."
   - Configure load balancer settings, including listeners, availability zones, security settings, and routing rules.
   - Complete the creation and note the DNS name provided for your Application Load Balancer.
----
### Lab Session - Deletion of an ALB

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Delete Application Load Balancer:**
   - Click on "Load Balancers" in the left sidebar under "EC2."
   - Select the Application Load Balancer you want to delete.
   - Click on "Actions > Delete" and confirm the deletion.

----
### What is an AWS Network Load Balancer?

AWS Network Load Balancer (NLB) is a load balancing solution designed to handle high volumes of traffic with low latency. It operates at the transport layer (Layer 4) and is capable of handling millions of requests per second while maintaining ultra-low latencies.

### Benefits of an AWS Network Load Balancer

1. **High Throughput:** Handles millions of requests per second with ultra-low latencies.
2. **Static IP:** Provides a static IP address per Availability Zone (AZ) for easy integration with applications.
3. **TLS Termination:** Supports TLS termination for end-to-end encryption.
4. **Target Group Support:** Routes traffic to target groups using IP addresses and ports.
5. **Health Checks:** Performs health checks on targets to ensure only healthy targets receive traffic.
----
### Lab Session - Creation of an AWS Network Load Balancer

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Network Load Balancer:**
   - Click on "Load Balancers" in the left sidebar under "EC2."
   - Click on "Create Load Balancer" and choose "Network Load Balancer."
   - Configure load balancer settings, including listeners, availability zones, security settings, and target groups.
   - Complete the creation and note the DNS name provided for your Network Load Balancer.
----
### Lab Session - Deletion of an NLB

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Delete Network Load Balancer:**
   - Click on "Load Balancers" in the left sidebar under "EC2."
   - Select the Network Load Balancer you want to delete.
   - Click on "Actions > Delete" and confirm the deletion.
----

### Difference between an Application Load Balancer (ALB) and a Network Load Balancer (NLB)

| Feature                         | Application Load Balancer (ALB)                          | Network Load Balancer (NLB)                              |
|---------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| **Layer**                       | Operates at Layer 7 (Application layer)                  | Operates at Layer 4 (Transport layer)                    |
| **Use Case**                    | Ideal for HTTP/HTTPS traffic and advanced routing        | Ideal for TCP, UDP, and TLS traffic requiring high performance |
| **Routing**                     | Supports advanced routing based on HTTP headers, paths, and hostnames | Routes traffic based on IP protocol data without inspection |
| **Performance**                 | Suitable for applications requiring intelligent routing decisions | High performance, low latency required for real-time applications |
| **Protocol Support**            | HTTP, HTTPS, WebSocket                                   | TCP, UDP, TLS                                            |
| **SSL Termination**             | Supports SSL termination                                 | Supports SSL passthrough and SSL termination             |
| **Target Type**                 | Can route to EC2 instances, IP addresses, Lambda functions | Can route to EC2 instances, IP addresses, and AWS PrivateLink endpoints |
| **Health Checks**               | Supports health checks based on HTTP/HTTPS status codes and content | Supports health checks based on TCP connections and responses |
| **WebSocket Support**           | Yes                                                      | No                                                       |
| **Sticky Sessions**             | Yes, using cookies                                       | No                                                       |
| **Host-based and Path-based Routing** | Yes                                                      | No                                                       |
| **Cost**                        | Generally more expensive due to advanced features        | Generally less expensive due to its simplicity and lower overhead |


----
### Lab Session - Attaching an ALB to a New Auto Scaling Group

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Auto Scaling Group (ASG):**
   - Click on "Auto Scaling Groups" in the left sidebar under "Auto Scaling."
   - Click on "Create Auto Scaling group" and follow the wizard to create a new Auto Scaling group.
   - Configure scaling policies, network settings, and tags.
   - Choose the existing Application Load Balancer (ALB) during the creation process to attach it to the Auto Scaling group.
----
### Lab Session - Attaching an ALB to an Existing Auto Scaling Group

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Modify Auto Scaling Group (ASG):**
   - Click on "Auto Scaling Groups" in the left sidebar under "Auto Scaling."
   - Select the Auto Scaling group to which you want to attach the Application Load Balancer (ALB).
   - Click on "Edit" and modify the ASG settings to attach the existing ALB.
   - Update the Auto Scaling group configuration to include the ALB and complete the modification process.
