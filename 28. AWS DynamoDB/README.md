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

* Amazon DynamoDB is a fully managed NoSQL database service provided by [Amazon Web Services](https://aws.amazon.com).
* It is designed to provide fast and predictable performance with seamless scalability.
* DynamoDB is serverless, meaning AWS automatically manages infrastructure, scaling, replication, and maintenance.
* It supports single-digit millisecond latency even at very large scale.

Official Documentation:
[Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)

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


### Core Components of DynamoDB

| Component         | Description                         |
| ----------------- | ----------------------------------- |
| **Table**         | Collection of items/data            |
| **Item**          | Single record in a table            |
| **Attribute**     | Field or column value               |
| **Partition Key** | Primary key used to distribute data |
| **Sort Key**      | Optional key for sorting data       |

### DynamoDB Table Example

#### Employee Table

| EmpId | Name   | Department | Email                                       | Address   |
| ----- | ------ | ---------- | ------------------------------------------- | --------- |
| 101   | Murali | DevOps     | murali@gmail.com                            |           |
| 102   | Ravi   | AWS        |                                             | Hyderabad |

* **Table Name** → Employees
* **Item** → Single employee record
* **Attributes** → EmpId, Name, Department, Email, Address

### Important Point

* In Amazon DynamoDB, every item can have different attributes.
* Unlike SQL databases, all records do not need the same columns/values.

#### Example:

* Murali has Email but no Address.
* Ravi has Address but no Email.

This is one of the major advantages of NoSQL databases like DynamoDB.

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
### Limitations of DynamoDB

1. **No SQL Joins:**

   * Joins are not supported like relational databases.
   * Data must be designed differently compared to SQL databases.

2. **Complex Query Limitations:**

   * Complex relational queries are difficult.
   * Not ideal for highly relational applications.

3. **Partition Key Design is Critical:**

   * Poor partition key design can create hot partitions.
   * Can impact performance and increase costs.

4. **Limited Transaction Complexity:**

   * Supports transactions, but not as flexible as relational databases.
   * Complex multi-table operations are difficult.

5. **Item Size Limitation:**

   * Maximum item size is 400 KB.
   * Large documents may require splitting data.

6. **Cost Can Increase Quickly:**

   * Poor design or heavy traffic can increase read/write costs significantly.
   * Scans are expensive for large tables.

---

### Difference between DynamoDB vs RDS

| Feature                   | DynamoDB                      | RDS                                       |
| ------------------------- | ----------------------------- | ----------------------------------------- |
| Database Type             | NoSQL                         | Relational SQL                            |
| Schema                    | Flexible                      | Fixed                                     |
| Scaling                   | Horizontal                    | Mostly Vertical                           |
| Joins                     | Not Supported                 | Supported                                 |
| Performance               | Very High                     | Moderate                                  |
| Infrastructure Management | Fully Managed Serverless      | Managed but requires DB administration    |
| Latency                   | Single-digit milliseconds     | Higher compared to DynamoDB               |
| Transactions              | Limited support               | Strong transaction support                |
| Auto Scaling              | Automatic                     | Limited/Manual depending on configuration |
| Storage Structure         | Key-Value / Document          | Tables with rows and columns              |
| Best For                  | Large-scale applications      | Relational applications                   |
| Common Use Cases          | Gaming, IoT, Real-time apps   | Banking, ERP, HRMS applications           |
| Query Language            | No SQL queries                | Supports SQL                              |
| Cost Model                | Pay per request / Provisioned | Instance-based pricing                    |
| Availability              | Multi-AZ by default           | Multi-AZ optional                         |
| Data Relationships        | Weak relational support       | Strong relational support                 |

---

### Creating DynamoDB Table Using AWS Console

1. **Open DynamoDB Service:**

   * Sign in to the AWS Management Console.
   * Search for and open Amazon DynamoDB service.

2. **Create Table:**

   * Click on **"Create Table"** button.

3. **Enter Table Details:**

   * Provide the required table details:

     * Table Name
     * Partition Key
     * Sort Key (optional)

Example:

| Setting       | Value                 |
| ------------- | --------------------- |
| Table Name    | Employees             |
| Partition Key | EmpId                 |
| Sort Key      | Department (Optional) |

4. **Choose Table Settings:**

   * Select:

     * **On-Demand Capacity Mode** for automatic scaling.
   * Configure additional settings if required:

     * Secondary Indexes
     * Encryption
     * Tags
     * Streams

5. **Review Configuration:**

   * Verify table configuration details.
   * Ensure partition key design is correct for proper performance.

6. **Create Table:**

   * Click on **"Create Table."**
   * AWS will provision the DynamoDB table automatically.


### After Table Creation

You can perform operations like:

1. **Insert Items**

   * Add employee records into the table.

2. **Read Data**

   * Retrieve items using partition key.

3. **Update Items**

   * Modify existing employee details.

4. **Delete Items**

   * Remove unwanted records.


### Example Employee Table

| EmpId | Name   | Department | Email                                       | Address   |
| ----- | ------ | ---------- | ------------------------------------------- | --------- |
| 101   | Murali | DevOps     | murali@gmail.com                            |           |
| 102   | Ravi   | AWS        |                                             | Hyderabad |


### Important Note

* In Amazon DynamoDB, different items can contain different attributes.
* DynamoDB does not require fixed schemas like relational databases.
* This flexibility makes DynamoDB suitable for evolving applications and large-scale workloads.
