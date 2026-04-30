#### INSTRUCTOR DETAILS

|  Information             | Details                                                                      |
|----------------------    |------------------------------------------------------------------------------|
| **Name**                 | Moole Muralidhara Reddy                                                      |
| **Website**              | https://www.vamsibhavani.in              |

### What is RDS?

**Amazon Relational Database Service (RDS):** A managed database service provided by AWS that makes it easier to set up, operate, and scale a relational database in the cloud.

### Features of RDS

1. **Managed Service:** AWS manages database tasks such as patching, backups, and replication.
2. **Multiple Database Engines:** Supports popular database engines like MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB.
3. **Automated Backups:** Automatic backups with point-in-time recovery.
4. **Scalability:** Easily scale compute and storage resources as needed.
5. **High Availability:** Multi-AZ deployments for automatic failover and reliability.
----
### RDS Subnet Group

- **Purpose:** Defines the subnets where RDS DB instances can be created.
- **Usage:** Ensures instances are launched in a specific VPC and subnet configuration.
----
### Parameter Groups

- **Purpose:** Manage engine configurations and runtime parameters.
- **Usage:** Customize database settings for performance and behavior.
----
### Option Groups

- **Purpose:** Manage features and functionalities specific to database engines.
- **Usage:** Enable features like encryption, performance enhancements, and additional capabilities.
----
### Amazon RDS Storage Types

- **General Purpose (SSD):** Balanced performance for a wide range of database workloads.
- **Provisioned IOPS (SSD):** High-performance storage for I/O-intensive database workloads.
- **Magnetic:** Cost-effective storage for workloads with low I/O requirements.
----
### Lab Session - Creating a MySQL Database in AWS RDS

1. **Sign in to AWS Management Console:**
   - Navigate to the RDS Dashboard at [AWS Management Console](https://console.aws.amazon.com/rds/).

2. **Launch RDS Instance:**
   - Click on "Create database."
   - Select MySQL as the engine type.
   - Choose the instance type, storage, and other configuration details.
   - Set up database credentials and specify other settings.
   - Click "Create database" to launch the instance.
----
### Lab Session - Connecting to the RDS MySQL from an AWS EC2 Instance

1. **Launch an EC2 Instance:**
   - Launch an EC2 instance in the same VPC and subnet as your RDS instance.

2. **Install MySQL Client:**
   - SSH into the EC2 instance.
   - Install MySQL client using `sudo sudo dnf install mariadb105-server -y` for Amazon Linux 2023 or `sudo apt-get install mysql-client` for Ubuntu.

3. **Connect to RDS MySQL:**
   - Use `mysql` command-line tool to connect to your RDS MySQL instance:
     ```bash
     mysql -h <endpoint> -u <username> -p
     ```
     Replace `<endpoint>` with your RDS endpoint and `<username>` with your database username.
----
### Lab Session - Installation of MySQL Workbench

1. **Download MySQL Workbench:**
   - Download MySQL Workbench from the official MySQL website: [MySQL Workbench Download](https://dev.mysql.com/downloads/workbench/).

2. **Install MySQL Workbench:**
   - Follow the installation instructions for your operating system.
----
### Lab Session - Connecting to the RDS MySQL from MySQL Workbench

1. **Open MySQL Workbench:**
   - Launch MySQL Workbench after installation.

2. **Configure Connection:**
   - Click on the "+" icon next to "MySQL Connections."
   - Enter connection details: hostname (RDS endpoint), port, username, and password.
   - Click "Test Connection" to verify connectivity.
   - Click "OK" to save the connection.
----
### Lab Session - Deletion of RDS MySQL Version

1. **Sign in to AWS Management Console:**
   - Navigate to the RDS Dashboard at [AWS Management Console](https://console.aws.amazon.com/rds/).

2. **Delete RDS Instance:**
   - Select the MySQL instance you want to delete.
   - Click on "Actions" -> "Delete."
   - Follow the prompts to confirm and delete the instance.
