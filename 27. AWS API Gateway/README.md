#### INSTRUCTOR DETAILS

| Information | Details                                                                     |
| ----------- | --------------------------------------------------------------------------- |
| **Name**    | Moole Muralidhara Reddy                                                     |
| **Website** | [Vamsi Bhavani Website](https://www.vamsibhavani.in) |

# What is AWS API Gateway?

Amazon API Gateway is a fully managed AWS service used to create, publish, secure, monitor, and manage APIs at any scale.

It acts as an entry point between client applications and backend services such as:

* AWS Lambda
* EC2
* ECS
* EKS
* DynamoDB
* External HTTP services

API Gateway helps developers build secure and scalable APIs without managing infrastructure.

Official Documentation:
[Amazon API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)


# Features of AWS API Gateway

## 1. Fully Managed Service

* AWS manages infrastructure, scaling, maintenance, and availability automatically.
* No server management required.

## 2. Supports Multiple API Types

API Gateway supports:

* REST API
* HTTP API
* WebSocket API

## 3. AWS Lambda Integration

* Direct integration with AWS Lambda functions.
* Enables serverless application architecture.


## 4. Security Features

Supports:

* IAM Authentication
* Lambda Authorizers
* JWT Authentication
* API Keys
* AWS WAF Integration


## 5. Traffic Management

* Throttling
* Rate limiting
* Request validation
* Caching


## 6. Monitoring and Logging

Integrated with:

* CloudWatch Logs
* CloudWatch Metrics
* AWS X-Ray


## 7. High Scalability

* Automatically scales based on API traffic.
* Handles millions of API requests.


## 8. CORS Support

* Supports Cross-Origin Resource Sharing configuration.
* Useful for frontend applications.

---

# Types of APIs in AWS API Gateway

Amazon API Gateway supports multiple API types designed for different use cases and architectures.

## 1. HTTP API

### Definition

* HTTP APIs are lightweight, low-latency, and cost-effective APIs.
* Mainly designed for serverless workloads and modern applications.

### Features

* Low cost
* High performance
* Native CORS support
* Supports OIDC and OAuth2 authentication
* Easy configuration

### Works With

* AWS Lambda
* HTTP Backends

### Use Cases

* Serverless applications
* Microservices
* Mobile backends
* Lightweight REST APIs

### Advantages

* Faster than REST API
* Lower pricing
* Simple setup

### Limitations

* Fewer advanced API management features compared to REST API

---

## 2. WebSocket API

### Definition

* WebSocket APIs provide persistent, two-way communication between client and server.
* Used for real-time applications.

### Features

* Full-duplex communication
* Persistent connections
* Real-time messaging

### Works With

* AWS Lambda
* HTTP Backends
* AWS Services

### Use Cases

* Chat applications
* Live dashboards
* Gaming applications
* Real-time notifications

### Advantages

* Real-time communication
* Low latency updates
* Efficient persistent connection handling

### Limitations

* More complex connection management
* Not suitable for traditional request-response APIs

---

## 3. REST API

### Definition

* REST API provides complete API management capabilities.
* Offers full control over request processing, response transformation, security, throttling, and caching.

### Features

* Advanced API management
* Request validation
* Response transformation
* API Keys
* Usage plans
* Caching support

### Works With

* AWS Lambda
* HTTP Backends
* AWS Services

### Use Cases

* Enterprise APIs
* Complex API architectures
* Public APIs
* APIs requiring advanced security and transformations

### Advantages

* Rich feature set
* Full request/response control
* Better enterprise support

### Limitations

* Higher cost
* Slightly higher latency
* More configuration complexity

---

## 4. REST API Private

### Definition

* REST API Private is accessible only from within a VPC.
* Uses VPC endpoints and AWS PrivateLink.

### Features

* Private network access
* Internal API communication
* Enhanced security

### Works With

* AWS Lambda
* HTTP Backends
* AWS Services

### Use Cases

* Internal enterprise APIs
* Banking systems
* Internal microservices
* Secure backend communication

### Advantages

* Highly secure
* No public internet exposure
* Internal-only access

### Limitations

* Requires VPC configuration
* Not publicly accessible

# Comparison of API Types

| Feature                | HTTP API         | WebSocket API         | REST API         | REST API Private |
| ---------------------- | ---------------- | --------------------- | ---------------- | ---------------- |
| Communication Type     | Request-Response | Persistent Connection | Request-Response | Request-Response |
| Best For               | Lightweight APIs | Real-time Apps        | Enterprise APIs  | Internal APIs    |
| Cost                   | Lowest           | Moderate              | Higher           | Higher           |
| Latency                | Very Low         | Low                   | Moderate         | Low              |
| Advanced Features      | Limited          | Moderate              | Full Support     | Full Support     |
| Public Access          | Yes              | Yes                   | Yes              | No               |
| VPC Access             | Optional         | Optional              | Optional         | Required         |
| API Caching            | No               | No                    | Yes              | Yes              |
| Authentication Support | OIDC/OAuth2      | Custom                | Advanced         | Advanced         |


# Which API Type Should You Use?

| Scenario               | Recommended API  |
| ---------------------- | ---------------- |
| Simple serverless API  | HTTP API         |
| Chat application       | WebSocket API    |
| Enterprise application | REST API         |
| Internal secure API    | REST API Private |
| Real-time dashboard    | WebSocket API    |
| Cost-optimized API     | HTTP API         |

---
### API Endpoint Types in AWS API Gateway

Amazon API Gateway supports different endpoint types to control how API traffic is routed and accessed.

There are mainly 3 endpoint types:

1. Regional
2. Edge-Optimized
3. Private

---

# 1. Regional Endpoint

### Definition

* API is deployed in a specific AWS Region.
* Clients access the API directly from that region.

### Architecture

```text id="7r1g8n"
Client → Regional API Gateway Endpoint → Backend Service
```

### Features

* Best for clients within the same region.
* Lower latency for regional users.
* Supports custom domain names.
* Can integrate with CloudFront manually if required.

### Use Cases

* Internal enterprise applications
* Regional mobile applications
* Applications serving users from one geographic area

### Example

```text id="f4u9nm"
https://abcd123.execute-api.us-east-1.amazonaws.com
```

### Advantages

* Lower cost compared to Edge-Optimized
* Better control over CDN configuration
* Good regional performance

### Limitations

* Global users may experience higher latency
* No built-in global edge caching

---

# 2. Edge-Optimized Endpoint

### Definition

* API requests are routed through AWS CloudFront edge locations automatically.
* Optimized for globally distributed users.

### Architecture

```text id="a9d2wq"
Client → CloudFront Edge Location → API Gateway → Backend
```

### Features

* Uses AWS CloudFront automatically.
* Reduces latency for global users.
* Best for public internet APIs.

### Use Cases

* Public APIs
* Global applications
* Worldwide mobile/web applications

### Advantages

* Better performance for global users
* Built-in CDN support
* Lower latency worldwide

### Limitations

* Slightly higher cost
* Less control over CloudFront behavior
* Additional latency for users very close to the region sometimes

---

# 3. Private Endpoint

### Definition

* API is accessible only within a VPC using VPC Endpoints.
* Not exposed to the public internet.

### Architecture

```text id="m8g5pl"
Internal Client → VPC Endpoint → Private API Gateway → Backend
```

### Features

* Accessible only from VPC.
* Uses AWS PrivateLink.
* Highly secure internal communication.

### Use Cases

* Internal enterprise APIs
* Banking applications
* Secure backend communication
* Internal microservices

### Advantages

* Highly secure
* No internet exposure
* Private communication within AWS network

### Limitations

* Cannot be accessed publicly
* Requires VPC endpoint configuration
* More networking setup required


# Comparison of API Endpoint Types

| Feature             | Regional           | Edge-Optimized   | Private                |
| ------------------- | ------------------ | ---------------- | ---------------------- |
| Internet Accessible | Yes                | Yes              | No                     |
| Uses CloudFront     | Manual             | Automatic        | No                     |
| Best For            | Regional users     | Global users     | Internal APIs          |
| Latency             | Regional optimized | Global optimized | Internal VPC optimized |
| Security            | Standard           | Standard         | Highest                |
| Public Access       | Yes                | Yes              | No                     |
| VPC Support         | Optional           | Optional         | Required               |
| Cost                | Lower              | Higher           | Moderate               |

# Which Endpoint Type Should You Choose?

| Scenario                          | Recommended Endpoint |
| --------------------------------- | -------------------- |
| Internal company API              | Private              |
| India-only users                  | Regional             |
| Worldwide public API              | Edge-Optimized       |
| Serverless internal microservices | Private              |
| Public mobile application         | Edge-Optimized       |

---
