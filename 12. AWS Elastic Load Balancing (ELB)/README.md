#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

## What is AWS Elastic Load Balancing (ELB)?

AWS Amazon Web Services Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets such as EC2 instances, IP addresses, containers, and Lambda functions to ensure high availability, fault tolerance, and better application performance.

ELB helps applications remain available by routing traffic only to healthy targets and balancing the load across multiple resources.

### Benefits of AWS Elastic Load Balancing (ELB)

* **High Availability:** Distributes traffic across multiple instances or targets, reducing overload on a single resource.

* **Fault Tolerance:** Automatically detects unhealthy targets and redirects traffic to healthy targets.

* **Scalability:** Handles changing traffic loads by working with Auto Scaling to increase or decrease resources automatically.

* **Security:** Supports SSL/TLS termination for encrypted traffic and integrates with AWS WAF for additional protection.

* **Health Checks:** Continuously monitors target health and sends traffic only to healthy resources.

* **Better Performance:** Improves application responsiveness by balancing traffic efficiently across backend targets.

* **Multi-AZ Support:** Distributes traffic across multiple Availability Zones for better reliability and disaster recovery.


----

## What is an AWS Classic Load Balancer?

AWS Amazon Web Services Classic Load Balancer (CLB) is the original load balancer service provided by AWS, mainly designed for applications running in the older EC2-Classic network. It supports both EC2-Classic and EC2-VPC platforms and can handle both Layer 4 (TCP) and Layer 7 (HTTP/HTTPS) traffic.

### Features of AWS Classic Load Balancer (CLB)

* **Layer 4 and Layer 7 Load Balancing:** Supports both TCP (Layer 4) and HTTP/HTTPS (Layer 7) traffic.

* **Sticky Sessions:** Supports session affinity by sending user requests to the same backend instance.

* **Health Checks:** Continuously monitors registered instances and sends traffic only to healthy instances.

* **Cross-Zone Load Balancing:** Distributes incoming traffic evenly across multiple Availability Zones.

* **SSL Termination: **Handles SSL/TLS encryption and decryption at the load balancer level.

### Drawbacks of AWS Classic Load Balancer (CLB)

* **Limited Routing Features:** Does not support advanced routing like path-based or host-based routing.

* **No Microservices Support:** Not suitable for modern microservices and container-based architectures.

* **Lower Performance:** Less efficient compared to ALB and NLB for high-scale applications.

* **Basic Protocol Support:** Limited support for modern protocols and advanced traffic handling.

* **Legacy Service:** Considered an older generation service, and AWS recommends using ALB or NLB for new applications.

* **Less Flexible Scaling:** Does not provide the same level of performance optimization as newer load balancers.

* **Weak Integration:** Limited integration with modern AWS services compared to ALB and NLB.

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

## What is an AWS Target Group?

AWS Amazon Web Services Target Group is used with Application Load Balancer (ALB) and Network Load Balancer (NLB) to route incoming requests to one or more registered targets such as EC2 instances, IP addresses or Lambda functions based on routing rules.

It helps the load balancer decide where to send traffic and performs health checks to ensure traffic goes only to healthy targets.

## What is a Listener?

A Listener is a process that checks for connection requests from clients using a specific protocol and port, such as HTTP:80 or HTTPS:443.

It receives incoming traffic on the load balancer and forwards requests to the appropriate target group based on the rules configured for that listener.

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

### Benefits of AWS Application Load Balancer (ALB)

* **Works at Application Layer (Layer 7):** Operates at Layer 7 and makes routing decisions based on application-level information like URLs and hostnames.

* **Content-Based Routing:** Routes traffic based on the content of the request (e.g., URL path).

* **Host-Based Routing:** Routes traffic based on host headers (e.g., different domains pointing to different target groups).

* **Path-Based Routing:** Routes traffic based on URL paths (e.g., `/api`, `/admin`, `/images`).

* **SSL/TLS Termination:** Handles SSL certificates at the load balancer level, reducing encryption/decryption load on backend servers.

* **WebSocket Support:** Supports long-lived WebSocket connections for real-time applications like chat apps and live dashboards.

* **Integrated with AWS WAF:** Protects applications from common web attacks like SQL injection and cross-site scripting (XSS).

* **Multiple Applications on One Load Balancer:** Allows multiple applications to run behind a single ALB using routing rules.

* **Better for Microservices and Containers:** Works well with microservices architecture and integrates with services like ECS and EKS.

* **Health Checks:** Continuously monitors backend targets and sends traffic only to healthy instances.
  
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

- AWS Amazon Web Services Network Load Balancer (NLB) is a high-performance load balancing service designed to handle very high volumes of traffic with ultra-low latency.
- It operates at the Transport Layer (Layer 4) and routes traffic based on TCP, UDP, and TLS protocols.
- It is capable of handling millions of requests per second while maintaining high performance and scalability.

### Benefits of AWS Network Load Balancer (NLB)

* **Works at Transport Layer (Layer 4):** Operates at Layer 4 and routes traffic based on TCP, UDP, and TLS connections.

* **High Throughput:** Handles millions of requests per second with ultra-low latency and high performance.

* **Static IP:** Provides a static IP address for each Availability Zone, making integration with external systems easier.

* **TLS Termination:** Supports TLS termination to handle secure encrypted traffic efficiently.

* **Target Group Support:** Routes traffic to targets using IP addresses, EC2 instances, or ports for flexible backend management.

* **Health Checks:** Continuously checks target health and sends traffic only to healthy targets.

* **Better for Real-Time Applications:** Ideal for gaming, IoT, video streaming, and high-performance applications requiring fast response.

* **Highly Scalable:** Automatically scales to handle sudden and large traffic spikes without performance issues.

* **Supports Multi-Protocol Traffic:** Can handle both TCP and UDP traffic efficiently.
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
| **Protocol Support**            | HTTP, HTTPS                                   | TCP, UDP, TLS                                            |
| **SSL Termination**             | Supports SSL termination                                 | Supports SSL passthrough and SSL termination             |
| **Target Type**                 | Can route to EC2 instances, IP addresses, Lambda functions | Can route to EC2 instances, IP addresses |
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
