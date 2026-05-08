#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |


# What is AWS Route 53?

- Amazon Route 53 is a highly available and scalable DNS (Domain Name System) web service provided by AWS.
- It translates human-readable domain names such as `www.devopsbymurali.com` into IP addresses such as `192.0.2.1`, allowing users to access applications and services over the internet.

Route 53 can also:

* Register domain names
* Route traffic using different routing policies
* Perform health checks and failover
* Manage both public and private DNS records

# Key Features of Route 53

### Highly Available and Scalable

Route 53 uses a globally distributed DNS infrastructure designed to handle large volumes of DNS queries with high availability.

### Multiple Routing Policies

Route 53 supports different routing policies, including:

* Simple Routing
* Weighted Routing
* Latency-based Routing
* Failover Routing
* Geolocation Routing
* Geoproximity Routing
* Multi-value Answer Routing

### Health Checks and Failover

Route 53 can monitor the health of applications and automatically route traffic away from unhealthy endpoints.

### Public and Private DNS

* Public Hosted Zones resolve domain names over the internet.
* Private Hosted Zones provide DNS resolution within Amazon VPCs.

### Integration with AWS Services

Route 53 integrates with AWS resources such as:

* Amazon EC2
* Elastic Load Balancer (ELB/ALB/NLB)
* CloudFront
* S3 static website endpoints
* API Gateway

### Security and Access Control

Route 53 integrates with IAM for access control and supports DNSSEC for DNS security.

### Cost-Effective

Users pay only for hosted zones, DNS queries, health checks, and optional features used.

----
### What is a Hosted Zone in Route53?

- **Hosted Zone:** A container that holds information about how you want Amazon Route 53 to respond to DNS queries for a domain and its subdomains. It consists of a collection of resource record sets (RRsets) that Route 53 returns in response to DNS queries.

A **Hosted Zone** is basically a **DNS database for your domain**.

Example domain:

`example.com`

Inside that hosted zone, you store DNS entries like:

| Type  | Name                                      | Value           |
| ----- | ----------------------------------------- | --------------- |
| A     | example.com                               | 1.2.3.4         |
| CNAME | [www.example.com](http://www.example.com) | example.com     |
| MX    | example.com                               | mail.google.com |

These entries are called **DNS records**.

In Route 53, AWS groups records as **Resource Record Sets (RRsets)**.

So:

* **Resource** = domain/subdomain
* **Record** = DNS entry
* **Set** = group of records of same name + type

Example:

Suppose you have:

```text
example.com -> 1.1.1.1
example.com -> 2.2.2.2
```

Both are:

* same name (`example.com`)
* same type (`A`)

Together they form **one RRset**.

That’s why AWS says:

> Hosted Zone contains a collection of RRsets.

Because the hosted zone is just storing all DNS mappings.

Simple mental model:

```text
Hosted Zone
   ├── A record set
   ├── CNAME record set
   ├── MX record set
   └── TXT record set
```

Real example in Route 53:

```text
Hosted Zone: example.com

RRset 1:
Type: A
Name: example.com
Values:
 - 1.1.1.1
 - 2.2.2.2

RRset 2:
Type: CNAME
Name: www.example.com
Value:
 - example.com
```


### Types of Hosted Zones

1. **Public Hosted Zone:** Manages domain names that are publicly accessible on the internet.
2. **Private Hosted Zone:** Manages domain names within an Amazon VPC (Virtual Private Cloud) and is accessible only from instances within the VPC.
----
### Lab Session - Creating a Public Hosted Zone in AWS Route53

1. **Sign in to AWS Management Console:**
   - Navigate to the Route 53 Dashboard at [AWS Management Console](https://console.aws.amazon.com/route53/).

2. **Create Hosted Zone:**
   - Click on "Create Hosted Zone."
   - Enter your domain name (e.g., example.com).
   - Choose the type (public or private).
   - Click "Create" to create the hosted zone.
----
### What are Records in a Hosted Zone?

- In AWS Route 53, a **record** is a DNS entry that maps a domain name to an IP address or another domain name.
- When a DNS resolver receives a request for a domain name, it queries the DNS server for the appropriate DNS record to resolve the domain to its corresponding resource.

### Types of Records

AWS Route 53 supports several types of DNS records that can be added to a hosted zone:

1. **A (Address) Record**:
   - Maps a domain name to an IPv4 address.

2. **AAAA (IPv6 Address) Record**:
   - Maps a domain name to an IPv6 address.

3. **CNAME (Canonical Name) Record**:
   - Maps a domain name to another domain name, creating an alias.

4. **MX (Mail Exchange) Record**:
   - Specifies mail servers responsible for accepting email messages for a domain.

5. **NS (Name Server) Record**:
   - Specifies the name servers for a domain.

6. **PTR (Pointer) Record**:
   - Maps an IP address to a domain name, used for reverse DNS lookups.

7. **SOA (Start of Authority) Record**:
   - Contains information about the DNS zone, including the primary name server and contact details.

8. **SPF (Sender Policy Framework) Record**:
   - Specifies servers authorized to send email on behalf of a domain.

9. **SRV (Service) Record**:
   - Specifies the location of a specific service, such as a web server or SIP server.

10. **TXT (Text) Record**:
    - Allows adding arbitrary text to a DNS record, used for domain verification or other purposes.
----
### What is Routing Policy?

- **Routing Policy:** Specifies how Amazon Route 53 responds to DNS queries. It determines which resource records to serve based on various criteria such as geographic location, latency, or health checks.

### Types of Routing Policies

1. **Simple Routing:** Associates a single resource record set with a single endpoint.
2. **Weighted Routing:** Distributes traffic among multiple resources based on assigned weights.
3. **Latency-Based Routing:** Directs traffic based on the lowest network latency for end users.
4. **Failover Routing:** Routes traffic to a standby resource in case of primary resource failure.
5. **Geolocation Routing:** Routes traffic based on the geographic location of the end user.
6. **Multi-Value Answer Routing:** Allows Route 53 to respond to DNS queries with up to eight healthy records selected at random.
----
### Lab Session - Creating a Record in a Hosted Zone

1. **Sign in to AWS Management Console:**
   - Navigate to the Route 53 Dashboard at [AWS Management Console](https://console.aws.amazon.com/route53/).

2. **Select Hosted Zone:**
   - Choose the hosted zone where you want to create the record.

3. **Create Record:**
   - Click on "Create Record Set."
   - Enter the details for the record (name, type, value, TTL).
   - Click "Create" to create the record set.
----
### Lab Session - Creating a Private Hosted Zone in AWS Route53

1. **Sign in to AWS Management Console:**
   - Navigate to the Route 53 Dashboard at [AWS Management Console](https://console.aws.amazon.com/route53/).

2. **Create Private Hosted Zone:**
   - Click on "Create Hosted Zone."
   - Enter your domain name (e.g., example.internal).
   - Choose the type as "Private hosted zone for Amazon VPC."
   - Select the VPCs where you want the private hosted zone to be accessible.
   - Click "Create" to create the private hosted zone.
----
### Lab Session - Configuring Query Logging for a Hosted Zone

1. **Sign in to AWS Management Console:**
   - Navigate to the Route 53 Dashboard at [AWS Management Console](https://console.aws.amazon.com/route53/).

2. **Select Hosted Zone:**
   - Choose the hosted zone for which you want to enable query logging.

3. **Configure Query Logging:**
   - Click on "Create Query Logging Config."
   - Configure the logging details (log group, IAM role).
   - Click "Create" to enable query logging.
----
### Lab Session - Deletion of a Hosted Zone

1. **Sign in to AWS Management Console:**
   - Navigate to the Route 53 Dashboard at [AWS Management Console](https://console.aws.amazon.com/route53/).

2. **Select Hosted Zone:**
   - Choose the hosted zone you want to delete.

3. **Delete Hosted Zone:**
   - Click on "Delete Hosted Zone."
   - Follow the confirmation prompts to delete the hosted zone.
