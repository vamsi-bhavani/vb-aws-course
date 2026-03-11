#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is an Auto Scaling Group?

An Auto Scaling Group (ASG) is a feature of AWS that automatically adjusts the number of EC2 instances in a group based on specified conditions. It helps ensure that you have the right number of instances available to handle the load for your application at any given time.

### Benefits of an Auto Scaling Group

1. **High Availability:** Automatically replaces unhealthy instances.
2. **Cost Efficiency:** Scales in or out based on demand, optimizing costs.
3. **Fault Tolerance:** Ensures applications can handle instance failures.
4. **Elasticity:** Scales capacity up or down to maintain steady performance.
5. **Easy Management:** Simplifies deployment and management of EC2 instances.
----
### What is a Launch Configuration?

- An AWS Launch Configuration is a template containing essential information required to launch instances in your AWS Auto Scaling Group.
- It includes details such as the instance type, AMI ID, security groups, and other launch parameters.

#### Example Scenario:

**Web Application Scaling During Peak Hours**

Let's say you have a web application that needs to handle a large number of user requests during peak hours. To ensure the application can manage the increased load, you want to create an AWS Auto Scaling Group with a Launch Configuration.

### Benefits of a Launch Configuration

1. **Standardization**:
   - Launch Configurations enable you to define a standard set of configuration settings for launching instances in your Auto Scaling Group.
   - Ensures instances are consistent and correctly configured.

2. **Simplified Scaling**:
   - Makes it easy to launch new instances when scaling out to meet demand.
   - Once created, a Launch Configuration can be used repeatedly to quickly and easily launch new instances.

3. **Automation**:
   - Can be used with AWS Auto Scaling Groups to automate the scaling of your infrastructure.
   - As demand grows or shrinks, your infrastructure can automatically scale up or down to meet the demand.

4. **Increased Reliability**:
   - Ensures all instances launched in your Auto Scaling Group are configured correctly and have the same software and security updates.
   - Increases the reliability of your infrastructure and reduces the risk of failures.

5. **Cost Savings**:
   - By using Launch Configurations with AWS Auto Scaling, you can save money by only running the instances needed to handle your application's demand.
   - Helps to reduce costs and optimize your infrastructure spending.

### Drawbacks of a Launch Configuration

1. **Limited Flexibility**:
   - Once a Launch Configuration is created, it cannot be modified.
   - Any changes require creating a new Launch Configuration.

2. **Configuration Drift**:
   - Over time, Launch Configurations may become outdated as new software or security updates are released.
   - This can result in configuration drift, where instances launched using an old Launch Configuration are not up-to-date and may not function as intended.

3. **Time-Consuming Setup**:
   - Creating a Launch Configuration can be time-consuming, especially if you have complex requirements for your instances.
   - This can be a challenge if you need to quickly launch a new instance or update your configuration.
----
### Lab Session - Creation of an AWS Launch Configuration

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Launch Configuration:**
   - Click on "Launch Configurations" in the left sidebar under "Auto Scaling."
   - Click on "Create launch configuration" and follow the wizard:
     - Choose an AMI.
     - Select an instance type.
     - Configure details like IAM role, security groups, and storage.
     - Review and create the launch configuration.
----
### What is an AWS Launch Template?

An AWS Launch Template is a newer version of Launch Configuration that provides more features and flexibility. It allows you to define configurations for launching EC2 instances, including instance type, AMI, security groups, and more.

### Benefits of an AWS Launch Template

1. **Standardization**:
   - **Consistency**: Launch Templates enable you to define a standard set of configuration settings to launch instances in your infrastructure, ensuring that all instances are consistent and correctly configured.

2. **Flexibility**:
   - **Versioning**: Unlike Launch Configurations, Launch Templates allow for multiple versions, providing the ability to update templates as requirements change over time.
   - **Custom Scripts**: You can use custom scripts to configure your instances.
   - **Multiple Instance Types**: Specify various instance types and sizes to meet different application needs.

3. **Automation**:
   - **Auto Scaling Integration**: Launch Templates can be used with AWS Auto Scaling Groups to automate the scaling of your infrastructure. This ensures that as demand grows or shrinks, your infrastructure can automatically scale up or down accordingly.

4. **Cost Savings**:
   - **Optimized Spending**: By using Launch Templates with AWS Auto Scaling, you only run the instances needed to handle your application's demand, reducing costs and optimizing infrastructure spending.
----
### Lab Session - Creation of an AWS Launch Template

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Launch Template:**
   - Click on "Launch Templates" in the left sidebar under "Auto Scaling."
   - Click on "Create launch template" and follow the wizard:
     - Specify template details like AMI, instance type, security groups, etc.
     - Configure advanced settings as needed (e.g., instance market options, tags).
     - Review and create the launch template.
----
### Difference between a Launch Template and a Launch Configuration


| Feature              | Launch Template                              | Launch Configuration                        |
|----------------------|----------------------------------------------|---------------------------------------------|
| **Standardization**  | Ensures instances are consistent and correctly configured | Ensures instances are consistent and correctly configured |
| **Flexibility**      | - Supports multiple versions<br>- Can be updated over time<br>- Allows custom scripts<br>- Supports multiple instance types and sizes | - Once created, cannot be modified<br>- No support for custom scripts or multiple instance types and sizes |
| **Automation**       | Can be used with AWS Auto Scaling Groups for automatic scaling | Can be used with AWS Auto Scaling Groups for automatic scaling |
| **Cost Savings**     | Optimizes infrastructure spending by running only necessary instances | Optimizes infrastructure spending by running only necessary instances |
| **Versioning**       | Supports multiple versions for updates       | Does not support versioning                 |
| **Custom Scripts**   | Allows use of custom scripts for instance configuration | Does not support custom scripts             |
| **Instance Types**   | Allows specification of multiple instance types and sizes | Does not allow multiple instance types and sizes |


----
### Lab Session - Creation of an ASG through an AWS Launch Configuration

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Auto Scaling Group (ASG):**
   - Click on "Auto Scaling Groups" in the left sidebar under "Auto Scaling."
   - Click on "Create Auto Scaling group" and follow the wizard:
     - Select a launch configuration.
     - Configure scaling policies, network settings, and tags.
     - Review and create the Auto Scaling group.
----
### Lab Session - Creation of an ASG through an AWS Launch Template

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Create Auto Scaling Group (ASG):**
   - Click on "Auto Scaling Groups" in the left sidebar under "Auto Scaling."
   - Click on "Create Auto Scaling group" and follow the wizard:
     - Select a launch template.
     - Configure scaling policies, network settings, and tags.
     - Review and create the Auto Scaling group.
----
### Lab Session - Enabling CloudWatch Monitoring in an ASG

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Configure Auto Scaling Group:**
   - Click on "Auto Scaling Groups" in the left sidebar under "Auto Scaling."
   - Select the Auto Scaling group.
   - Click on "Activity" tab, then "Instance management," then "Edit," then "Monitoring."
   - Enable CloudWatch detailed monitoring.
----
### Lab Session - Deletion of an ASG

1. **Sign in to AWS Management Console:**
   - Navigate to the EC2 Dashboard at [AWS Management Console](https://console.aws.amazon.com/ec2/).

2. **Delete Auto Scaling Group:**
   - Click on "Auto Scaling Groups" in the left sidebar under "Auto Scaling."
   - Select the Auto Scaling group you want to delete.
   - Click on "Actions > Delete" and confirm the deletion.
