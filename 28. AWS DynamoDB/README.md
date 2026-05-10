#### INSTRUCTOR DETAILS

| Information | Details                                                                     |
| ----------- | --------------------------------------------------------------------------- |
| **Name**    | Moole Muralidhara Reddy                                                     |
| **Website** | [Vamsi Bhavani Website](https://www.vamsibhavani.in) |

### What is NoSQL Database?

* A NoSQL database is a non-relational database designed for high scalability, flexibility, and performance.
* Unlike traditional SQL databases, NoSQL databases do not require fixed table schemas.
* They are mainly used for handling large amounts of structured, semi-structured, and unstructured data.
* NoSQL databases are designed to support distributed applications and massive-scale workloads.

### Examples of NoSQL Databases

* Amazon DynamoDB
* MongoDB
* Apache Cassandra
* Redis

---

### What is DynamoDB?

* Amazon DynamoDB is a fully managed NoSQL database service provided by [Amazon Web Services](https://aws.amazon.com?utm_source=chatgpt.com).
* It is designed to provide fast and predictable performance with seamless scalability.
* DynamoDB is serverless, meaning AWS automatically manages infrastructure, scaling, replication, and maintenance.
* It supports single-digit millisecond latency even at very large scale.

Official Documentation:
[Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/?utm_source=chatgpt.com)

---

### Features of DynamoDB

1. **Fully Managed Service:**

   * AWS manages servers, patching, maintenance, and scaling automatically.
   * No infrastructure management is required.

2. **Serverless Architecture:**

   * No need to provision or manage servers.
   * Pay only for the resources consumed.

3. **Automatic Scaling:**

   * Dynamically adjusts read and write throughput capacity.
   * Handles sudden traffic spikes efficiently.

4. **High Availability:**

   * Data is automatically replicated across multiple Availability Zones.
   * Ensures durability and fault tolerance.

5. **Flexible Schema:**

   * Each item in the table can have different attributes.
   * Suitable for evolving applications.

6. **High Performance:**

   * Provides single-digit millisecond response times.
   * Suitable for real-time applications.

7. **Security Integration:**

   * Supports IAM, encryption, backups, and VPC endpoints.
   * Ensures secure data access.

---

### Core Components of DynamoDB

| Component         | Description                         |
| ----------------- | ----------------------------------- |
| **Table**         | Collection of items/data            |
| **Item**          | Single record in a table            |
| **Attribute**     | Field or column value               |
| **Partition Key** | Primary key used to distribute data |
| **Sort Key**      | Optional key for sorting data       |

---

### DynamoDB Table Example

#### Employee Table

| EmpId | Name   | Department |
| ----- | ------ | ---------- |
| 101   | Murali | DevOps     |
| 102   | Ravi   | AWS        |

* Table Name → Employees
* Item → Single employee record
* Attributes → EmpId, Name, Department

---

### Use Cases of DynamoDB

1. **E-Commerce Applications:**

   * Product catalog management
   * Shopping carts
   * Order management

2. **Gaming Applications:**

   * Player profiles
   * Leaderboards
   * Game sessions

3. **IoT Applications:**

   * Sensor data storage
   * Device monitoring
   * Real-time telemetry

4. **Real-Time Applications:**

   * Chat applications
   * Notification systems
   * Live tracking systems

5. **Session Management:**

   * User sessions
   * Authentication tokens

6. **Analytics Applications:**

   * Event tracking
   * Clickstream analysis
   * Real-time dashboards

---

### DynamoDB Capacity Modes

1. **On-Demand Mode:**

   * Pay per request.
   * Automatically handles traffic scaling.
   * Best for unpredictable workloads.

2. **Provisioned Mode:**

   * Manually define read/write capacity units.
   * Best for predictable workloads.
   * Can reduce cost for stable traffic patterns.

---

### DynamoDB vs RDS

| Feature       | DynamoDB                 | RDS                     |
| ------------- | ------------------------ | ----------------------- |
| Database Type | NoSQL                    | Relational SQL          |
| Schema        | Flexible                 | Fixed                   |
| Scaling       | Horizontal               | Mostly Vertical         |
| Joins         | Not Supported            | Supported               |
| Performance   | Very High                | Moderate                |
| Best For      | Large-scale applications | Relational applications |

---
