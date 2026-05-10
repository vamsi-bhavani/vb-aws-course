#### INSTRUCTOR DETAILS

| Information | Details                                                                     |
| ----------- | --------------------------------------------------------------------------- |
| **Name**    | Moole Muralidhara Reddy                                                     |
| **Website** | [Vamsi Bhavani Website](https://www.vamsibhavani.in) |

### What is AWS SQS?

Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service provided by [Amazon Web Services](https://aws.amazon.com?utm_source=chatgpt.com).

It enables distributed applications, microservices, and serverless applications to communicate asynchronously using queues.

Amazon SQS helps:

* Decouple applications
* Improve scalability
* Increase fault tolerance
* Handle traffic spikes
* Ensure reliable message delivery

Official Documentation:
[Amazon SQS Documentation](https://docs.aws.amazon.com/sqs/)

---

### Why Do We Need SQS?

Without SQS:

```text id="7b7x3m"
Application A → Directly communicates → Application B
```

Problem:

* If Application B fails, the entire workflow may fail.
* Heavy traffic can overload backend services.

With SQS:

```text id="5x7c8r"
Application A → Amazon SQS Queue → Application B
```

Advantages:

* Messages are stored safely in queue.
* Backend services can process messages later.
* Services become loosely coupled.

---

### Features of AWS SQS

### 1. Fully Managed Service

* AWS manages infrastructure, scaling, and maintenance automatically.
* No server management required.

### 2. Asynchronous Communication

* Applications communicate through messages instead of direct connections.
* Improves system reliability.

### 3. High Scalability

* Automatically scales to process millions of messages.


### 4. High Availability

* Messages are replicated across multiple AWS servers.
* Ensures durability and fault tolerance.

### 5. Secure Messaging

Supports:

* IAM policies
* Encryption
* Access control
* VPC endpoints


### 6. Dead Letter Queue (DLQ)

* Stores failed or unprocessed messages.
* Helps in troubleshooting failures.


### 7. Visibility Timeout

* Prevents multiple consumers from processing the same message simultaneously.


### 8. Message Retention

* Messages can be retained from:

  * 1 minute to 14 days


### 9. Long Polling

* Reduces empty responses.
* Improves efficiency and reduces cost.

---
### Types of SQS Queues

| Queue Type     | Description                                              |
| -------------- | -------------------------------------------------------- |
| Standard Queue | High throughput with at-least-once delivery              |
| FIFO Queue     | First-In-First-Out ordering with exactly-once processing |

### Standard Queue

### Definition

* Standard Queue is the default queue type in Amazon Simple Queue Service.
* It is designed for maximum throughput, scalability, and availability.
* Message ordering is not guaranteed strictly.

### Features

* Nearly unlimited throughput
* Best-effort ordering
* At-least-once message delivery
* Duplicate messages possible
* Very high scalability

### Advantages

1. Handles massive traffic
2. Highly scalable
3. Lower latency
4. Cost effective
5. Suitable for distributed systems

### Limitations

1. Duplicate messages may occur
2. Message order is not guaranteed
3. Applications must handle duplicate processing

### Use Cases

* Background processing
* Event-driven systems
* Distributed applications
* Log processing
* Email processing systems

### Real-Time Example — Zomato

```text id="j1bg4s"
User Places Order
       ↓
Standard Queue
       ↓
Restaurant Service
```

* Thousands of food orders can be processed simultaneously.
* Exact message order usually does not matter.

---

### FIFO Queue

### Definition

* FIFO Queue guarantees:

  * First-In-First-Out ordering
  * Exactly-once message processing
* Messages are processed in the same order they are sent.

### Features

* Strict message ordering
* Exactly-once processing
* No duplicate messages
* Message deduplication support
* Lower throughput compared to Standard Queue

### Advantages

1. Prevents duplicate processing
2. Guarantees message sequence
3. Suitable for critical systems
4. Better data consistency

### Limitations

1. Lower throughput than Standard Queue
2. Slightly higher cost
3. Not ideal for extremely high-traffic workloads

### Use Cases

* Banking applications
* Financial systems
* Payment processing
* Order processing systems
* Inventory management

### Real-Time Example — Banking System

```text id="hn5wpm"
Transaction 1 → FIFO Queue → Processed First
Transaction 2 → FIFO Queue → Processed Second
```

Example:

* ₹500 debit should happen before ₹1000 debit if sent earlier.
* Order of transactions is extremely important.

### Standard Queue vs FIFO Queue

| Feature            | Standard Queue          | FIFO Queue               |
| ------------------ | ----------------------- | ------------------------ |
| Throughput         | Very High               | Moderate                 |
| Message Ordering   | Best-effort             | Strict ordering          |
| Duplicate Messages | Possible                | Not allowed              |
| Delivery Type      | At-least-once           | Exactly-once             |
| Performance        | Faster                  | Slightly slower          |
| Cost               | Lower                   | Higher                   |
| Best For           | High-scale applications | Critical ordered systems |

### Important Naming Rule

### Standard Queue

Example:

```text id="3r8k0q"
EmployeeQueue
```

### FIFO Queue

Queue name must end with:

```text id="q67m2k"
.fifo
```

Example:

```text id="qv8j1c"
EmployeeQueue.fifo
```

### Which Queue Should You Choose?

| Scenario                   | Recommended Queue |
| -------------------------- | ----------------- |
| Zomato orders              | Standard Queue    |
| Chat notifications         | Standard Queue    |
| Banking transactions       | FIFO Queue        |
| Payment processing         | FIFO Queue        |
| High traffic systems       | Standard Queue    |
| Ordered processing systems | FIFO Queue        |

---

### Lab Session : Creation of Standard SQS Queue

### Step 1 — Create Standard SQS Queue

```
EmployeeQueue

```

### Step 2 — Send Message to SQS Queue

###Command

```bash id="c7m1ps"
aws sqs send-message \
--queue-url https://sqs.us-east-1.amazonaws.com/617618117734/EmployeeQueue \
--message-body "Hello from AWS SQS" \
--region us-east-1
```

### Example JSON Message

```bash id="h2f7vk"
aws sqs send-message \
--queue-url https://sqs.us-east-1.amazonaws.com/617618117734/EmployeeQueue \
--message-body '{"EmpId":"101","Name":"Murali","Department":"DevOps"}' \
--region us-east-1
```

---

### Step 3 — Read Messages from SQS Queue

### Command

```bash id="q9x2eb"
aws sqs receive-message \
--queue-url https://sqs.us-east-1.amazonaws.com/617618117734/EmployeeQueue \
--region us-east-1
```

### Expected Output

```json id="2v5nlg"
{
    "Messages": [
        {
            "MessageId": "xxxx",
            "ReceiptHandle": "AQEBxxxx",
            "Body": "Hello from AWS SQS"
        }
    ]
}
```
### Important Note

* ReceiptHandle is required to delete the message.
* Every receive operation generates a new ReceiptHandle.

### Step 4 — Delete Message from SQS Queue

### Command

```bash id="8r1pzc"
aws sqs delete-message \
--queue-url https://sqs.us-east-1.amazonaws.com/617618117734/EmployeeQueue \
--receipt-handle AQEBxxxx \
--region us-east-1
```

### Full Workflow

```text id="4u2vbe"
Create Queue
     ↓
Send Message
     ↓
Receive Message
     ↓
Process Message
     ↓
Delete Message
```

### Real-Time Example — Zomato

```text id="1j9vkp"
Customer Places Order
        ↓
Order Message Sent to SQS
        ↓
Restaurant Service Reads Message
        ↓
Processes Order
        ↓
Deletes Message
```
