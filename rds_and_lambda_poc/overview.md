First, we need to launch an RDS instance. We can use any type of database as long as it is easily interfaced with via the coding language we use to define our Lambda function. In general, the concept of letting AWS call RDS or any other AWS service falls under the domain of a `VPC`. There is more information on VPCs here: https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html. Basically, we need to add aws resources to the same VPC to allow them to interface with one another. Then, as long as the virtual private cloud is running, the resources that exist within it can talk to one another.

When we create an RDS instance, we assign it to a VPC. So that serves as the foundation for the rest of the steps we must take. From here, we need to create a lambda function that also exists within the same VPC. After this, we can write a script that connects to the instance and performs any needed operations. This tutorial is a really good one: https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html.

In this folder I'll write some code for the lambda function. We can create the RDS instance and Lambda function within the default subnets from the AWS console, and we can also create the appropriate role for the lambda function (VPCFullAccess) within IAM.

# steps
1. Create RDS instance, take note of VPC and subnet groups, username, password, and database name
2. Write Code for Lambda function
3. Create lambda function, be sure to assign it the `AWSLambdaVPCAccessExecutionRole` permission. This allows it to call other services within the same VPC.
4. Upload code to lambda (https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)
5. Test the lambda function in the console or via the CLI
