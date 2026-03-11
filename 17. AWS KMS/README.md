#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is AWS KMS?

**AWS Key Management Service (KMS):** A managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. It integrates with other AWS services to help you protect your data.

### Features and Benefits of AWS KMS

1. **Centralized Key Management:** Create, rotate, and manage encryption keys used across AWS services and your applications.
2. **Integration with AWS Services:** Seamlessly integrates with services like S3, EBS, RDS, and more for encryption at rest.
3. **Secure:** Uses hardware security modules (HSMs) to protect the security and integrity of your keys.
4. **Auditable:** Logs API calls made to KMS keys, providing visibility and compliance.
5. **Cost-Effective:** Pay only for what you use, with no upfront costs.

### Different Types of Keys in AWS KMS

1. **Customer Master Keys (CMKs):** Used to encrypt and decrypt data. Can be either symmetric or asymmetric.
   - **Symmetric CMKs:** Used for encrypting and decrypting data.
   - **Asymmetric CMKs:** Used for signing and verifying data.

2. **AWS Managed Keys:** KMS-managed keys that AWS creates, owns, and manages on your behalf for specific AWS services (e.g., S3, EBS).
----
### Lab Session - Creating a KMS Key

1. **Sign in to AWS Management Console:**
   - Navigate to the KMS Dashboard at [AWS Management Console](https://console.aws.amazon.com/kms/).

2. **Create KMS Key:**
   - Click on "Create key."
   - Choose whether you want to create a symmetric or asymmetric key.
   - Configure key settings (e.g., key alias, description).
   - Click "Next" and then "Finish."

3. **Take Note of Key ARN:**
   - Make a note of the key ARN (Amazon Resource Name) for later use.
----
### Lab Session - Encrypting an EBS Volume Using AWS KMS

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Encrypt EBS Volume:**
   - Create or select an existing EBS volume.
   - Modify the volume to enable encryption and choose the KMS key created earlier.
   - Apply the changes.

3. **Verify Encryption:**
   - Verify that the EBS volume is now encrypted using the selected KMS key.
----
### Lab Session - Deletion of KMS

1. **Sign in to AWS Management Console:**
   - Navigate to the KMS Dashboard at [AWS Management Console](https://console.aws.amazon.com/kms/).

2. **Delete KMS Key:**
   - Select the KMS key you want to delete.
   - Click "Delete key."
   - Follow the confirmation steps to delete the key.
