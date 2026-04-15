#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is AWS S3:
1. **Definition**: Amazon S3 is a simple storage service offering durable, highly available, and scalable data storage infrastructure at low costs.
2. **Object Storage**: It is a key-based object store.
3. **File Upload**: Allows uploading files ranging from 0 bytes to 5TB each.
4. **Scalability**: Offers unlimited storage capacity.
5. **Bucket Storage**: Files are stored in containers called buckets.
6. **Key Structure**: Keys (object identifiers) can mimic hierarchical structures.
7. **Data Accessibility**: Enables storing and retrieving any amount of data from anywhere on the internet.
8. **Global Unique Names**: Operates with a universal namespace; bucket names must be globally unique.
9. **DNS Name**: Each bucket has a DNS name for access (e.g., `https://s3-eu-east-2.amazonaws.com/bucket_name`).

### Bucket:
1. **Object Container**: Buckets are containers for storing objects.
2. **Hierarchy**: Does not provide object hierarchy natively but uses object key names (prefixes) to simulate folders.
3. **Folder Simulation**: Users can create folders within buckets using object key names.
4. **Nested Buckets**: Nested buckets are not supported.
5. **URL Access**: Bucket names are part of the URL for accessing stored objects.
6. **Region Specific**: Each S3 bucket is specific to a region.
7. **Global Name Uniqueness**: Names must be globally unique due to S3's universal namespace.
8. **Logging**: Supports enabling logging to track access and usage.

### Objects in Bucket:
- **Definition**: Objects are individual items stored in an S3 bucket.
- **Characteristics**: Each object has a unique key and can store data up to 5TB, along with optional metadata.
- **Hierarchy**: Objects are organized using unique keys, often resembling file paths, to simulate folder structures.
- **Access**: Accessed via URLs incorporating bucket names and object keys (e.g., `https://s3.amazonaws.com/bucket_name/object_key`).
- **Operations**: Common operations include upload, download, copy, delete, and list, managed via AWS SDKs, CLI, or AWS Management Console.
----
### Types of Storage Classes in AWS S3

1. **Standard:** Provides high durability, availability, and performance for frequently accessed data.
2. **Intelligent-Tiering:** Automatically moves objects between two access tiers based on changing access patterns.
3. **Standard-IA (Infrequent Access):** For data that is accessed less frequently but requires rapid access when needed.
4. **One Zone-IA:** Lower-cost option for infrequently accessed data that doesn't require multiple Availability Zone resilience.
5. **Glacier and Glacier Deep Archive:** For archival data with retrieval times ranging from minutes to hours.

----
### Lab Session - Create an S3 Bucket

1. **Sign in to AWS Management Console:**
   - Navigate to the S3 Dashboard at [AWS Management Console](https://s3.console.aws.amazon.com/s3/).

2. **Create S3 Bucket:**
   - Click on "Create bucket."
   - Enter a unique bucket name and choose a region.
   - Configure optional settings like versioning, logging, and tags.
   - Review and create the bucket.
----
### Lab Session - Upload Objects to S3 using the AWS Console

1. **Sign in to AWS Management Console:**
   - Navigate to the S3 Dashboard at [AWS Management Console](https://s3.console.aws.amazon.com/s3/).

2. **Upload Objects:**
   - Select the bucket to which you want to upload objects.
   - Click on "Upload" and select files from your local machine.
   - Configure upload options and permissions as needed.
   - Upload the files to the S3 bucket.
----
### Lab Session - Upload Objects to S3 using the AWS CLI

1. **Open Command Line Interface:**
   - Open a terminal or command prompt on your local machine.

2. **Upload Objects using AWS CLI:**
   - Use the `aws s3 cp` command to copy files to S3:
     ```bash
     aws s3 cp <local_file_path> s3://<bucket_name>/<remote_file_name>
     ```
   - Optionally, use `aws s3 sync` for syncing directories:
     ```bash
     aws s3 sync <local_directory> s3://<bucket_name>/<remote_directory>
     ```
     cp (needs recursive)
     ```bash
     aws s3 cp ./data s3://my-bucket/data --recursive
    ```
----
### S3 Versioning and Enabling it

- **Versioning:** Keeps multiple variants of an object in the same bucket.
- **Enable Versioning:**
   - Sign in to AWS Management Console.
   - Navigate to S3 Dashboard.
   - Select the bucket and click on "Properties."
   - Under "Advanced settings," enable versioning.
----
### Bucket Policy in Amazon S3

- **Bucket Policy:** JSON-based access policy applied at the bucket level to manage permissions.
- **Working with Bucket Policy for S3 Bucket:**
   - Define permissions for who can access (e.g., IAM users, roles, or specific IP ranges).
   - Define actions allowed (e.g., read, write, delete).
   - Apply conditions for access (e.g., based on IP address, user agent).
----
### Lab Session - Working with the Bucket Policy for S3 Bucket

1. **Sign in to AWS Management Console:**
   - Navigate to the S3 Dashboard at [AWS Management Console](https://s3.console.aws.amazon.com/s3/).

2. **Configure Bucket Policy:**
   - Select the bucket and click on "Permissions."
   - Click on "Bucket Policy" and enter or modify the JSON policy document.
   - Use AWS policy generator to generate a policy based on requirements.
   - Review and apply the policy to manage access to the S3 bucket.
----

### Access Control List (ACL) in Amazon S3:
- **Purpose**: ACLs define who can access your buckets and objects and what level of access they have (read, write, etc.).
- **Types**: S3 supports both bucket-level and object-level ACLs.
- **Permissions**: ACLs can grant permissions to AWS accounts or predefined groups (e.g., authenticated users, everyone).
- **Granularity**: Object ACLs can be more granular than bucket ACLs, allowing specific permissions per object.
- **Management**: ACLs can be managed using AWS Management Console, AWS CLI, or SDKs.
- **Alternatives**: S3 also supports more flexible and recommended access management through Bucket Policies and IAM policies.

ACLs provide a straightforward way to control access to your S3 resources based on specific needs and security requirements.

----
### Lab Session - Apply ACL for S3 Bucket

1. **Sign in to AWS Management Console:**
   - Navigate to the S3 Dashboard at [AWS Management Console](https://s3.console.aws.amazon.com/s3/).

2. **Apply ACL for S3 Bucket:**
   - Select the bucket for which you want to modify ACL.
   - Click on "Permissions."
   - Under "Access control list (ACL)," configure permissions for specific AWS accounts or users.
   - Choose permissions like read, write, or full control.
----

### Amazon S3 (Simple Storage Service) bucket lifecycle

- Amazon S3 (Simple Storage Service) bucket lifecycle management allows you to manage your objects so that they are stored cost-effectively throughout their lifecycle.
- You can define lifecycle rules to transition objects between different storage classes or to expire objects after a specified period.

### Key Concepts

1. **Lifecycle Configuration**: A set of rules that define actions (transition or expiration) on a group of objects within an S3 bucket.

2. **Storage Classes**: Different storage classes like STANDARD, INTELLIGENT_TIERING, STANDARD_IA (Infrequent Access), ONEZONE_IA, GLACIER, and DEEP_ARCHIVE.

3. **Transition Actions**: Moving objects to a different storage class.

4. **Expiration Actions**: Deleting objects after a specified period.

### Creating a Lifecycle Rule

1. **Log in to AWS Management Console**:
   Go to the S3 service.

2. **Select the Bucket**:
   Choose the bucket you want to configure.

3. **Go to the Management Tab**:
   Navigate to the "Management" tab in the bucket's properties.

4. **Lifecycle Rules**:
   Click on "Lifecycle" and then "Add lifecycle rule."

5. **Configure Rule**:
   - **Rule Name**: Give your rule a meaningful name.
   - **Scope**: Choose if the rule applies to all objects or to a subset of objects (prefix or tags).

6. **Set Transition Actions**:
   - Add transitions to move objects to different storage classes. Specify the number of days after object creation when the transition should occur.
   - Example: Move objects to STANDARD_IA after 30 days and to GLACIER after 365 days.

7. **Set Expiration Actions**:
   - Define when objects should be deleted (e.g., 365 days after creation).
   - Optionally, set clean-up options for incomplete multipart uploads.

8. **Review and Create**:
   Review your rule configurations and create the lifecycle rule.

----
### Hosting a Static Website using Amazon S3

1. **Sign in to AWS Management Console:**
   - Navigate to the S3 Dashboard at [AWS Management Console](https://s3.console.aws.amazon.com/s3/).

2. **Hosting a Static Website:**
   - Select the bucket you want to use for hosting.
   - Click on "Properties" and then "Static website hosting."
   - Enable static website hosting and configure index and error documents.
   - Note the endpoint URL provided for accessing your static website.

----
### Presigned URLs in AWS S3

**Presigned URLs:** URLs that grant temporary access to download or upload a specific S3 object with a specified expiration time.

### Lab Session - Working with Presigned URLs in AWS S3
 **Generate Presigned URL (Download):**
   - Use AWS SDK or AWS CLI to generate a presigned URL for an object.
   - Example using AWS CLI:
     ```bash
     aws s3 presign s3://<bucket_name>/<object_key> --expires-in 3600
     ```
   - This URL allows temporary access to download the object for one hour.

----

### Server-side Encryption for Amazon S3 Buckets:
- **Definition**: It encrypts objects stored in S3 buckets at the server level, ensuring data confidentiality.
- **Types**:
  - **SSE-S3**: Server-side encryption with Amazon S3-managed keys (SSE-S3). AWS manages and rotates keys automatically.
  - **SSE-KMS**: Server-side encryption with AWS Key Management Service (SSE-KMS). Provides additional control over encryption keys, including key management and auditing.
  - **SSE-C**: Server-side encryption with customer-provided keys (SSE-C). Allows you to manage your own encryption keys outside of AWS.
- **Encryption Process**: Objects are encrypted before being written to disks and decrypted when retrieved.
- **Management**: Encryption settings can be configured at the bucket level or applied to individual objects.
- **Benefits**: Enhances data security and compliance with encryption standards without requiring changes to applications.
- **Usage**: Managed via AWS Management Console, AWS CLI, or SDKs, providing flexibility in implementation and management.

Server-side encryption ensures that data stored in Amazon S3 remains protected against unauthorized access, providing a critical layer of security for sensitive information.

----

### Lab Session - Delete an S3 Bucket

1. **Sign in to AWS Management Console:**
   - Navigate to the S3 Dashboard at [AWS Management Console](https://s3.console.aws.amazon.com/s3/).

2. **Delete an S3 Bucket:**
   - Select the bucket you want to delete.
   - Click on "Actions > Delete bucket."
   - Confirm the deletion.
