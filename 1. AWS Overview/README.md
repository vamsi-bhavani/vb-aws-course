#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in                                                  |
### What is Cloud Computing?

- Cloud computing refers to the delivery of computing services—such as servers, storage, databases, networking, software, and more—over the internet ("the cloud").
- It enables users to access and utilize these resources on-demand, rather than maintaining physical hardware or infrastructure locally.

### Benefits of Cloud Computing

1. **Scalability:** Easily scale resources up or down based on demand.
2. **Cost Efficiency:** Pay only for what you use, reducing upfront costs.
3. **Flexibility:** Access resources from anywhere with an internet connection.
4. **Reliability:** Providers often offer high uptime and redundancy.
5. **Security:** Cloud providers invest in robust security measures.
----
### Types of Cloud Computing

## 1. Public Cloud
Resources are owned and operated by third-party providers, accessible over the internet by the general public.

**Example:**
1. **Amazon Web Services (AWS):** You can rent servers and storage space online.
2. **Microsoft Azure:** You can host websites and store data on Microsoft's servers.
3. **Google Cloud Platform (GCP):** You can use Google's infrastructure to run applications and store data.

## 2. Private Cloud
Dedicated resources operated solely for a single organization.

**Example:**
1. **Company Data Center:** A business has its own servers and storage in-house.
2. **VMware vSphere:** A company uses software to manage its own private servers.
3. **OpenStack:** A company sets up and manages its own cloud infrastructure using open-source tools.

## 3. Hybrid Cloud
Combination of public and private clouds, allowing data and applications to be shared between them.

----
### Types of Cloud Services
1. **Infrastructure as a Service (IaaS):**
- IaaS provides users with access to virtualized computing resources such as servers, storage, and networking, which can be used to build and deploy their own applications and services.
- Users are responsible for managing and maintaining the software and applications they deploy on the infrastructure provided by the IaaS provider.

**Examples:**

1. **Amazon Elastic Compute Cloud (EC2):**
   - Provides resizable compute capacity in the cloud.
   - Users can launch virtual servers, known as instances, and run applications on them.

2. **Amazon Simple Storage Service (S3):**
   - Scalable object storage service.
   - Users can store and retrieve any amount of data at any time.

3. **Amazon Elastic Block Store (EBS):**
   - Provides block-level storage volumes for use with EC2 instances.
   - Users can create, attach, and manage storage volumes for their virtual servers.

4. **Amazon Virtual Private Cloud (VPC):**
   - Enables users to launch AWS resources into a virtual network.
   - Users can control their virtual networking environment, including selection of IP address range, creation of subnets, and configuration of route tables and gateways.

2.**Platform as a Service (PaaS):**

- PaaS provides users with a platform for building and deploying their own applications without having to worry about managing the underlying infrastructure.
- PaaS providers typically offer pre-configured software, tools, and application programming interfaces (APIs) that make it easier for developers to build, test, and deploy their applications.

**Examples:**

1. **AWS Elastic Beanstalk:**
   - A platform that allows users to deploy and manage applications without worrying about the underlying infrastructure.
   - Automatically handles the deployment, from capacity provisioning, load balancing, and auto-scaling to application health monitoring.

2. **AWS Lambda:**
   - A serverless compute service that lets users run code without provisioning or managing servers.
   - Users can run code in response to events and automatically scale from a few requests per day to thousands per second.

3. **Amazon API Gateway:**
   - A fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
   - Enables users to create RESTful APIs and WebSocket APIs for real-time two-way communication applications.

4. **Amazon Elastic Container Service (ECS):**
   - A highly scalable, high-performance container orchestration service that supports Docker containers.
   - Allows users to easily run, stop, and manage containers on a cluster of EC2 instances.


3.**Software as a Service (SaaS):**
- SaaS provides users with access to fully managed software applications and services that are hosted by a third-party provider.
- Users typically access SaaS applications through a web browser or mobile app, and the provider is responsible for maintaining and updating the software.

**Examples:**

1. **Amazon WorkSpaces:**
   - A managed, secure Desktop-as-a-Service (DaaS) solution.
   - Users can provision Windows or Linux desktops in just a few minutes and quickly scale to provide thousands of desktops to workers across the globe.

2. **Amazon Chime:**
   - A communications service that allows users to meet, chat, and place business calls inside and outside of their organization.
   - Provides a secure, scalable, and feature-rich communications platform accessible from any device.

3. **Amazon WorkDocs:**
   - A secure enterprise document storage and sharing service.
   - Allows users to create, edit, and share content, and provides administrative controls and feedback capabilities.

4. **Amazon WorkMail:**
   - A secure, managed business email and calendaring service.
   - Compatible with existing email clients and offers strong security features to protect data.

----

**What is AWS?**

- AWS (Amazon Web Services) is a cloud computing platform by Amazon that provides on-demand access to services like virtual servers (EC2), storage (S3), databases, networking, and machine learning tools.
- Instead of owning physical hardware, businesses can run applications and store data on AWS infrastructure over the internet.

**Advantages of AWS**

* **Global Reach:** AWS operates data centers in multiple regions worldwide, ensuring low latency and high availability.
* **Scalability:** Resources can be scaled up or down instantly based on demand.
* **Cost-Effective:** Pay-as-you-go pricing eliminates the need for large upfront investments.
* **Security:** Offers robust security features, including encryption and compliance with global standards.
* **Wide Service Range:** Provides hundreds of services for computing, analytics, AI, and more.

**Disadvantages of AWS**

* **Complexity:** The large number of services can be overwhelming for beginners.
* **Cost Management:** Costs can increase quickly without proper monitoring and optimization.
* **Data Transfer Costs:** Charges apply for transferring data between regions or outside AWS.
* **Vendor Lock-in:** Migrating away from AWS can be difficult once deeply integrated.

----
### AWS Global Infrastructure

#### Regions

- AWS Regions are geographically separate locations around the world where AWS clusters its data centers.
- Each region is designed to be independent and consists of multiple Availability Zones.
- Users can choose a region based on factors like latency, compliance, and cost.

#### Availability Zones

- Availability Zones (AZs) are physically separate data centers within a region.
- Each AZ has its own power, cooling, and networking, making them isolated from failures in other zones.
- At the same time, AZs within a region are connected through high-speed networks, allowing applications to be distributed across multiple zones for high availability and fault tolerance.

----
### Lab Session - Creation of an AWS Account

Creating an AWS account involves:

1. **Go to AWS Website:** Navigate to aws.amazon.com and click "Create an AWS Account."
2. **Provide Information:** Enter required details including email, password, and payment information.
3. **Verify Account:** Follow steps to verify your identity and payment method.
4. **Access Console:** Once verified, log in to the AWS Management Console to start using AWS services.
