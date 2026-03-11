# 📘 AWS Lambda – Overview, Runtimes, and Limitations

#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |

| **Website**              | https://www.vamsibhavani.in              |
vamsibhavani.in

## 🧭 What is AWS Lambda

- **AWS Lambda** is a **serverless compute service** that enables you to run code without provisioning or managing servers.
- It automatically scales your applications by running code in response to events and only charges for the compute time consumed.

---

## 🚀 Why Use AWS Lambda?

| Feature              | Benefit                                                                 |
|----------------------|-------------------------------------------------------------------------|
| **Serverless**       | No server management needed                                              |
| **Cost-Effective**   | Pay only for the execution time (billed per ms)                          |
| **Event-Driven**     | React to triggers from S3, DynamoDB, API Gateway, CloudWatch, etc.       |
| **Scalable**         | Automatically handles thousands of concurrent executions                 |
| **Fast Deployment**  | Just upload the code and configure trigger and IAM role                  |
| **Secure**           | Integrates with IAM for fine-grained access control                      |

---

## ⚙️ Supported Runtimes

AWS Lambda supports a variety of runtimes to suit different programming environments.

### 🔸 Official Runtimes

| Language     | Runtime Identifier       |
|--------------|--------------------------|
| Node.js      | `nodejs18.x`, `nodejs16.x` |
| Python       | `python3.12`, `python3.11`, `python3.10`, `python3.9` |
| Java         | `java21`, `java17`, `java11` |
| Go           | `go1.x`                  |
| Ruby         | `ruby3.2`                |
| .NET         | `dotnet8`, `dotnet7`, `dotnet6` (via custom container) |
| Custom       | `provided.al2`           |

### 🔸 Custom Runtimes

If your language is not natively supported, you can build a custom runtime using the **Lambda Runtime API**.

### 🔸 Container Images

AWS Lambda also supports functions packaged as **container images** (up to 10 GB), using:
- AWS base images (Amazon Linux 2)
- Custom-built images

---

## 🧱 Limitations

### 🔹 General Limits

| Resource                         | Limit                                                   |
|----------------------------------|----------------------------------------------------------|
| **Max execution timeout**        | 15 minutes (900 seconds)                                |
| **Memory allocation**            | 128 MB to 10,240 MB (10 GB)                             |
| **Ephemeral disk (`/tmp`)**      | 512 MB (up to 10 GB with `ephemeralStorage`)            |
| **Deployment package (ZIP)**     | 50 MB (direct upload), 250 MB (unzipped, including layers) |
| **Container image size**         | 10 GB                                                   |
| **Concurrent executions**        | 1,000 (default, adjustable with request)                |
| **Environment variable size**    | 4 KB total                                              |

---

### 🔹 Security & IAM

| Limitation                    | Description                                               |
|-------------------------------|-----------------------------------------------------------|
| **IAM required**              | Must attach an IAM role with correct permissions          |
| **Timeout risks**             | Sensitive operations may fail if timeouts are mismanaged  |

---

### 🔹 Networking Constraints

| Constraint                   | Description                                                      |
|------------------------------|------------------------------------------------------------------|
| **No public internet (VPC)** | Lambda in a private VPC needs a NAT Gateway to access the internet |
| **ENI limitations**          | Elastic Network Interface allocation is limited in VPC setups    |

---

### 🔹 Other Considerations

| Limit                        | Description                                                       |
|------------------------------|--------------------------------------------------------------------|
| **Max Lambda layers**        | 5 per function                                                     |
| **Payload size (Request)**   | 6 MB (synchronous), 256 KB (asynchronous)                          |
| **Payload size (API Gateway)** | 6 MB                                                            |
| **No GPU support**           | Cannot be used for GPU-intensive workloads (e.g., ML model training) |

---

## 🛠️ Workarounds for Common Limitations

| Limitation                  | Workaround                                                    |
|-----------------------------|---------------------------------------------------------------|
| 15-minute timeout           | Use **Step Functions** to chain multiple Lambda functions     |
| Large payloads              | Upload to **S3** and pass the object key to Lambda            |
| Need persistent storage     | Use **S3, DynamoDB, or EFS**                                  |
| VPC access with internet    | Attach a **NAT Gateway** or keep Lambda outside the VPC       |
