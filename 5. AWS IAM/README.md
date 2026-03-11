#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is AWS IAM?

- AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS services and resources for your users.
- IAM enables you to manage users, groups, roles, and permissions to securely access AWS resources.

### Features of AWS IAM

1. **Centralized Control:** Manage access centrally for AWS accounts.
2. **Shared Access:** Grant permissions to users, groups, or roles as needed.
3. **Granular Permissions:** Define fine-grained permissions using policies.
4. **Multi-Factor Authentication (MFA):** Add an extra layer of security.
5. **Identity Federation:** Integrate with existing corporate directories.
6. **Identity Information:** Manage user identities and their permissions.
----
### What is AWS IAM User

1. **Definition**: Represents an individual with unique credentials to access AWS services and resources.
2. **Credentials**: Assigned a username, password, access keys, or multi-factor authentication (MFA) device.
3. **Permissions**: Managed through policies that define allowed or denied actions on AWS resources.
4. **Access Management**: Permissions are specific to each user, allowing fine-grained control over access.
5. **Usage**: Typically used to grant access to AWS resources to individuals such as employees or contractors.
6. **Security**: Users can have their access credentials and permissions managed independently.

### Lab Session - AWS IAM Users

1. **Sign in to AWS Management Console:**
   - Navigate to the IAM Dashboard at [AWS Management Console](https://console.aws.amazon.com/iam/).

2. **Create IAM User:**
   - Click on "Users" in the left sidebar and then "Add user."
   - Enter a username and select access type (programmatic access, AWS Management Console access, or both).
   - Set permissions by adding the user to groups or attaching policies directly.
   - Complete the user creation and note down the access credentials.
----
### AWS IAM User Groups

1. **Definition**: A collection of IAM users for easier permission management.
2. **Permissions**: Permissions are assigned to groups rather than to individual users.
3. **Simplifies Management**: Users can be added to or removed from groups, inheriting permissions automatically.
4. **Efficiency**: Reduces administrative overhead by applying permissions at the group level.
5. **Flexibility**: Users can belong to multiple groups, inheriting permissions from all groups they are part of.
6. **Scalability**: Ideal for organizations managing access for multiple users with similar roles or permissions needs.

### Lab Session - AWS IAM User Groups

1. **Sign in to AWS Management Console:**
   - Navigate to the IAM Dashboard at [AWS Management Console](https://console.aws.amazon.com/iam/).

2. **Create IAM Group:**
   - Click on "Groups" in the left sidebar and then "Create group."
   - Enter a group name and attach policies to define permissions for the group.
   - Add IAM users to the group to inherit the group's permissions.
----
### What are AWS IAM Policies?

IAM policies are JSON documents that define permissions allowing or denying actions on AWS resources. They are attached to IAM identities (users, groups, roles) and control what actions these identities can perform.

### Types of AWS IAM Policies

1. **Managed Policies:** AWS-managed policies created and managed by AWS.
2. **Inline Policies:** Policies that you create and manage directly within an IAM identity (user, group, role).
3. **Custom Policies:** Policies tailored to specific needs and attached to IAM identities.
----
### Lab Session - Configuring AWS CLI

Configuring the AWS CLI involves setting up authentication credentials and default settings to interact with AWS services from the command line. Here’s a step-by-step guide to configuring the AWS CLI:

### Prerequisites
Before configuring the AWS CLI, ensure you have:
- An AWS account.
- AWS CLI installed on your local machine. If not installed, you can download it from [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

### Steps to Configure AWS CLI

1. **Open a Terminal or Command Prompt:**
   - Depending on your operating system, open Terminal (for macOS/Linux) or Command Prompt (for Windows).

2. **Run `aws configure` Command:**
   - Type the following command and press Enter:
     ```
     aws configure
     ```

3. **Enter AWS Access Key ID:**
   - You will be prompted to enter your AWS Access Key ID. This is a key credential for accessing AWS services programmatically. It looks like `AKIAIOSFODNN7EXAMPLE`.

4. **Enter AWS Secret Access Key:**
   - Next, you will be prompted to enter your AWS Secret Access Key, which is paired with the Access Key ID to authenticate requests. It looks like `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

5. **Specify Default Region Name:**
   - Enter the AWS region code that you want to use by default. For example, `us-east-1` or `eu-west-1`. This specifies the region where your AWS resources will be created and accessed unless overridden by specific commands.

6. **Specify Default Output Format (Optional):**
   - Optionally, specify the default output format. The output can be formatted as `json`, `text`, `table`, etc. If you don't specify, it defaults to `json`.

7. **Verification:**
   - Once you’ve entered all the required information, AWS CLI will store these configurations in the `~/.aws/credentials` and `~/.aws/config` files on macOS/Linux or `%UserProfile%\.aws\credentials` and `%UserProfile%\.aws\config` files on Windows.

8. **Test Configuration:**
   - To verify that your configuration works, you can run a simple AWS CLI command, such as:
     ```
     aws s3 ls
     ```
   - This command lists all your S3 buckets. If configured correctly, it will list the buckets accessible with the provided credentials.

----
### Lab Session - Named Profiles for the AWS CLI

To configure a named profile named `dev` for the AWS CLI, you would typically use the `aws configure` command with the `--profile` option. Here's how you can do it:

1. Open your terminal or command prompt.

2. Enter the following command:
   ```
   aws configure --profile dev
   ```

3. You will be prompted to enter the following information:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region name
   - Default output format (optional)

4. After entering the required information, press Enter.

5. AWS CLI will store these configurations under the profile name `dev` in the AWS credentials and config files located in your user's home directory (`~/.aws/`).

6. You can verify the configuration by using the `--profile` option with AWS CLI commands, for example:
   ```
   aws ec2 describe-instances --profile dev
   ```
----
### What is an IAM Role?

- In AWS IAM, a role is a set of permissions that define which actions an AWS service or user can perform on AWS resources. Unlike users and groups, roles are not associated with a specific identity.
- Instead, roles can be assumed by users, AWS services, or AWS resources to grant temporary permissions to access AWS resources.

**Key Points:**
- **Permissions:** Roles contain permissions that determine what actions are allowed on AWS resources.
- **Temporary Access:** Roles can be assumed to grant temporary permissions.
- **No Specific Identity:** Roles are not tied to a specific user or group.
- **Use Cases:** Roles are useful for granting permissions to AWS services, applications, or users that need temporary access.

**Examples of Role Usage:**
1. **EC2 Instances:** An EC2 instance can assume a role to gain temporary access to S3 buckets, allowing it to read or write data.
2. **Lambda Functions:** A Lambda function can assume a role to access other AWS services, such as DynamoDB or SQS, during its execution.
3. **Cross-Account Access:** A role can be created to allow users from one AWS account to access resources in another AWS account.
4. **AWS Services:** AWS services like CodeBuild or CodePipeline can assume roles to interact with other AWS resources on behalf of the user.

----
### Steps to Create an IAM Role with Full S3 Access Policy

1. **Sign in to the AWS Management Console:**
   - Go to [AWS Management Console](https://aws.amazon.com/console/) and sign in with your credentials.

2. **Navigate to the IAM Console:**
   - In the AWS Management Console, search for and select "IAM" under "Services", or directly go to the [IAM Dashboard](https://console.aws.amazon.com/iam/).

3. **Create a New Role:**
   - In the IAM dashboard, click on "Roles" in the left-hand navigation pane.
   - Click on the "Create role" button to start creating a new IAM role.

4. **Choose the Type of Trusted Entity:**
   - Select "AWS service" as the type of trusted entity.
   - Choose the service that will use this role. For S3 access, you can select "S3" from the list of services.

5. **Attach Permissions Policies:**
   - In the "Permissions" step, select "AmazonS3FullAccess" policy. This policy grants full access to all actions on all resources in S3.
   - You can use the search box to find the policy quickly by typing "AmazonS3FullAccess".

6. **Add Tags (Optional):**
   - You can optionally add tags to categorize and manage your IAM resources. Tags are key-value pairs.

7. **Review and Name the Role:**
   - Review the details of the role configuration.
   - Provide a name for your role, e.g., "S3FullAccessRole".

8. **Create the Role:**
   - Click on "Create role" to create the IAM role with full S3 access.
----
### Lab Session - How to Attach the IAM Role to an EC2 Instance?

   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).
   - Select the EC2 instance you want to attach the IAM role to.
   - Click on "Actions > Security > Modify IAM role" and select the IAM role you created.
   - Apply the changes to attach the IAM role to the EC2 instance.

----
### Root Account vs IAM User

| Feature                | Root Account                                    | IAM User                                      |
|------------------------|-------------------------------------------------|-----------------------------------------------|
| **Creation**           | Created automatically upon AWS account signup.  | Created within AWS account by an administrator. |
| **Permissions**        | Full administrative access by default.          | Permissions defined by policies attached to the user. |
| **Access Keys**        | Root account has access keys for API access.    | IAM users can have access keys for API access. Access keys can be rotated regularly. |
| **Access Control**     | No restrictions; has access to all resources.   | Permissions can be granularly defined using IAM policies. |
| **Security**           | Should not be used for everyday tasks due to security risks. | Enhanced security with defined permissions and monitoring. |
| **Audit and Logging**  | Limited logging and auditing capabilities.      | Actions are logged and audited through AWS CloudTrail. |
| **Multi-factor Authentication (MFA)** | MFA is available but not enforced by default. | MFA can be enabled for increased security. |
| **Best Practices**     | Securely store credentials. Use for account management tasks only. | Follow least privilege principle. Rotate access keys regularly. Use for day-to-day operations. |

----

### Lab Session - AWS IAM Password Policy
The AWS IAM Password Policy allows you to set rules and requirements for the passwords used by IAM users in your AWS account. Here's an outline of the typical parameters you can configure in an AWS IAM Password Policy:

| Parameter                          | Description                                                                                      |
|------------------------------------|--------------------------------------------------------------------------------------------------|
| **Minimum Password Length**         | Specifies the minimum number of characters that must be present in an IAM user password.          |
| **Require Lowercase Characters**    | Ensures that passwords contain at least one lowercase letter.                                      |
| **Require Uppercase Characters**    | Ensures that passwords contain at least one uppercase letter.                                      |
| **Require Numbers**                 | Ensures that passwords contain at least one numeric digit (0-9).                                   |
| **Require Symbols**                 | Ensures that passwords contain at least one non-alphanumeric character (e.g., !, @, #, $, %).      |
| **Allow Users to Change Password**  | Determines whether IAM users are allowed to change their own passwords.                            |
| **Expire Passwords**                | Specifies the number of days after which IAM user passwords expire and must be reset.              |
| **Password Expiration Warning**     | Specifies the number of days before password expiration that IAM users receive a warning.          |
| **Prevent Reuse of Last N Passwords** | Restricts IAM users from reusing the specified number of previous passwords.                      |

### Configuring IAM Password Policy in AWS Console

To configure the IAM Password Policy in AWS:

1. **Sign in to the AWS Management Console**: Go to [AWS Management Console](https://aws.amazon.com/console/) and sign in with your credentials.

2. **Navigate to IAM**: Under "Services", select "IAM" to open the IAM dashboard.

3. **Set Password Policy**:
   - In the left navigation pane of the IAM dashboard, click on "Account settings".
   - Click on "Change password policy".
   - Configure the desired parameters for your password policy, such as minimum length, character requirements, password expiration settings, and password reuse prevention.
   - Click on "Apply password policy" to save your changes.

### Best Practices

- **Complexity**: Ensure passwords are sufficiently complex to resist brute-force attacks.
- **Rotation**: Regularly rotate passwords to reduce the risk of compromise.
- **MFA**: Encourage or enforce the use of Multi-Factor Authentication (MFA) for added security.
- **Monitoring**: Monitor AWS CloudTrail logs for password-related events to detect and respond to unauthorized access attempts.

----
### Lab Session - Multi-Factor Authentication (MFA) for AWS IAM

1. **Sign in to AWS Management Console:**
   - Navigate to the IAM Dashboard at [AWS Management Console](https://console.aws.amazon.com/iam/).

2. **Enable MFA:**
   - Click on "Users" in the left sidebar and select the IAM user.
   - Click on the "Security credentials" tab and locate "Assigned MFA device."
   - Follow the instructions to configure and activate MFA using a hardware device or virtual MFA app.

----
### IAM Best Practices

1. **Implement Least Privilege**: Grant minimal permissions necessary for tasks, avoiding excessive access.

2. **Enable MFA**: Require multi-factor authentication for all IAM users to enhance login security.

3. **Secure Root Account**: Use it sparingly, secure with strong passwords and MFA.

4. **Use IAM Roles for EC2**: Assign roles instead of access keys to EC2 instances for secure AWS resource access.

5. **Monitor IAM Activity**: Enable CloudTrail for logging and CloudWatch for alarms on IAM events.

6. **Rotate Credentials**: Regularly update access keys, passwords, and MFA devices to mitigate risks.

7. **Use IAM Policy Conditions**: Apply conditions (e.g., IP, time) in policies to enforce stricter access controls.

8. **Centralize Identity Management**: Use AWS Organizations and SSO for streamlined account management and security integration.
