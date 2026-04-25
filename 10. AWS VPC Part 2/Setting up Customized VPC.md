# Setting up Customized VPC.
![Lab - Setting up Customized VPC in telugu - Moole Muralidhara Reddy ](https://github.com/vamsi-bhavani/vb-aws-course/blob/main/10.%20AWS%20VPC%20Part%202/images/Day%20%2013-%20Lab%20-%20Setting%20up%20Customized%20VPC%20-%20Moole%20Muralidhara%20Reddy%20-%20vamsibhavani.png)

## Step 1: Create the AWS VPC
```xml
Name: Dev-VPC in US East (N. Virginia) us-east-1
CIDR : 10.100.0.0/16
```
## Step 2: Create a 2 public subnets with
```xml
CIDR :10.100.8.0/21
Name: Dev-public-subnet-1a

CIDR :10.100.16.0/21
Name: Dev-public-subnet-1b

```
## Step 3: Create a 2 private subnets with
```xml
CIDR :10.100.80.0/21
Name: Dev-private-subnet-1a

CIDR :10.100.88.0/21
Name: Dev-private-subnet-1b

```

## Step 4: Create a 2 app subnets with
```xml
CIDR :10.100.144.0/21
Name: Dev-app-subnet-1a

CIDR :10.100.162.0/21
Name: Dev-app-subnet-1b

```
## Step 4: Create a 2 data subnets with
```xml
CIDR :10.100.168.0/21
Name: Dev-data-subnet-1a

CIDR :10.100.176.0/21
Name: Dev-data-subnet-1b

```

## Step 5: Create an internet gateway and attach to Dev-VPC
```xml
Name: Dev-VPC-IGW
```
## Step 6: Create a route table and name it Dev-VPC-Public-RouteTable and attach the public subnets to this RouteTable.
```xml
Name: Dev-VPC-Public-RouteTable
```

## Step 7: Create a route table and name it Dev-VPC-Private-RouteTable and attach the private,app,data subnets to this RouteTable.

```xml
Name: Dev-VPC-Private-RouteTable
```

## Step 8: Add the Internet Gateway route to the Public RouteTable.

```xml
Route Entry

Destination : 0.0.0.0/0
Target : Internet Gateway ID
```

## Step 9: Launch the Linux EC2 instance in the Public Subnet.
## Step 10: Connect to the Linux EC2 instance through Putty or SSH command.

#### Congratulations! You have successfully set up the VPC.
