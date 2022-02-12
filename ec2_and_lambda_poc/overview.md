The goal for this POC is to write a lambda function that can start an EC2 instance and run some arbitrary code on that instance. Ideally, we would be able to 1) start an ec2 instance within lambda, 2) run some code on the instance, and 3) shut down the ec2 instance within the code from (2)

First, we'll write the lambda function that spins up an ec2 instance. Then, we'll figure out how to execute some code on that instance. Finally, we will figure out how to shut down that ec2 instance within the code being executed on that ec2 instance (this is important because the lambda can exit prior to the entire process executing on ec2).

# steps
1. create lambda function, assign full ec2 access to lambda
2. use boto3 in lambda function to interface with the instance

Good article about running code on ec2 instance: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
