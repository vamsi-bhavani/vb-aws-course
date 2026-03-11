#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is AWS ACM?
- AWS ACM stands for AWS Certificate Manager.
- It is a service provided by Amazon Web Services (AWS) that makes it easier for you to provision, manage, and deploy Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources.

### Key Features of AWS ACM:

1. **Provisioning SSL/TLS Certificates**:
   - AWS ACM allows you to easily provision SSL/TLS certificates for use with AWS services such as Elastic Load Balancing (ELB), Amazon CloudFront, and Amazon API Gateway.

2. **Managed Renewals and Deployment**:
   - ACM manages the renewal of SSL/TLS certificates automatically, removing the need for manual intervention and ensuring certificates are always up to date.

3. **Integration with AWS Services**:
   - ACM integrates seamlessly with other AWS services, making it straightforward to deploy SSL/TLS certificates to resources like ELB, CloudFront distributions, and API Gateway APIs.

4. **Global Infrastructure and Scaling**:
   - ACM is designed to scale automatically and operates across multiple AWS regions, allowing you to use the same SSL/TLS certificate across your global infrastructure.

5. **Private Certificate Authority (CA)**:
   - ACM Private CA allows you to create and manage a private certificate authority, enabling you to issue private certificates for internal resources securely.

6. **Security and Compliance**:
   - ACM helps you maintain a secure environment by providing managed certificates that adhere to industry standards and best practices for encryption and security.

### Benefits of AWS ACM:

- **Simplified Management**: ACM automates the process of certificate management, reducing the complexity and operational overhead associated with SSL/TLS certificate deployment and renewal.

- **Cost-effective**: ACM provides SSL/TLS certificates at no additional cost beyond what you pay for the AWS resources using the certificates, making it cost-effective compared to third-party certificate authorities.

- **Integrated with AWS**: ACM integrates seamlessly with other AWS services, ensuring that SSL/TLS certificates are easily deployed and managed across your AWS infrastructure.

- **Highly Available and Secure**: ACM leverages AWS's global infrastructure and security best practices to ensure high availability and secure management of SSL/TLS certificates.
----
### Lab Session - Creating AWS ACM

1. **Sign in to AWS Management Console:**
   - Navigate to the AWS ACM Dashboard at [AWS Management Console](https://console.aws.amazon.com/acm/).

2. **Request a Certificate:**
   - Click on "Request a certificate."
   - Enter the domain names (e.g., example.com, *.example.com) for which you want to request the certificate.
   - Choose validation method (email validation or DNS validation).
   - Click "Next" to review and confirm the certificate request.
   - Complete the validation process based on the chosen method.
----
### Lab Session - Integrating AWS ACM with an Application Load Balancer

1. **Sign in to AWS Management Console:**
   - Navigate to the AWS ACM Dashboard at [AWS Management Console](https://console.aws.amazon.com/acm/).

2. **Retrieve ACM Certificate:**
   - Find and select the ACM certificate you want to use.
   - Click on "Actions" -> "Edit in Amazon EC2 Console."
   - Copy the Amazon Resource Name (ARN) of the ACM certificate.

3. **Associate ACM Certificate with ALB:**
   - Navigate to the Amazon EC2 Console at [AWS Management Console](https://console.aws.amazon.com/ec2/).
   - Select "Load Balancers" from the navigation pane.
   - Choose the Application Load Balancer (ALB) where you want to associate the ACM certificate.
   - Click on "Listeners" tab, then "View/edit rules" for HTTPS listener.
   - Edit the listener to select the ACM certificate ARN for HTTPS traffic.
   - Save the changes to associate the ACM certificate with the ALB.
----
### Lab Session - Deletion of AWS ACM

1. **Sign in to AWS Management Console:**
   - Navigate to the AWS ACM Dashboard at [AWS Management Console](https://console.aws.amazon.com/acm/).

2. **Select Certificate:**
   - Choose the ACM certificate you want to delete.

3. **Delete ACM Certificate:**
   - Click on "Actions" -> "Delete."
   - Confirm the deletion when prompted.
