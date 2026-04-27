# Creating  a Network Access Control List (NACL)

![Lab - Setting up AWS NACL - Moole Muralidhara Reddy](https://github.com/techworldwithmurali/AWS-Networking-From-Zero-to-Hero/blob/main/AWS%20VPC/images/Setting%20up%20AWS%20NACL-%20Moole%20Muralidhara%20Reddy%20-%20Tech%20World%20with%20Murali.pn)

#### Step 1: Create the Public NACL
```xml
Name: Infra-Public-NACL
```
####  Step 2: Attach the Public Subnets to the Public NACL
####  Step 3: Create the Private NACL
```xml
Name: Infra-Private-NACL
```
####  Step 4: Attach the private , app and  data  Subnets to the Private  NACL
#### Step 5: Launch the Linux EC2 instance in the Public Subnet.
#### Step 6: Add the Inbound rules and test them
####  Congratulations! You have successfully set up and tested the AWS NACL.
