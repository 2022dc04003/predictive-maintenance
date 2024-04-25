# predictive-maintenance

### MLFlow on AWS

1. Login to AWS console
2. Create IAM user with 'AdministratorAccess' policy
3. Export security credentials (CLI access keys) in AWS CLI and run 'aws configure'
4. Create S3 bucket to store artifacts
5. Create an EC2 machine (Ubuntu), add Security Groups and open Port 5000. Also attach an IAM Role that has S3 full access
6. Browse public IPV4 address of the EC2 machine on port 5000 (use http://)
7. Go to local terminal

#### -- Run the following commands on EC2 machine after Step 5 above:

`sudo apt update`

`sudo apt install python3-pip`

`sudo pip3 install pipenv`

`sudo pip3 install virtualenv`

`mkdir mlflow`

`cd mlflow`

`pipenv install mlflow`

`pipenv install awscli`

`pipenv install boto3`

`pipenv shell`

`aws configure`

`mlflow server --host 0.0.0.0 --default-artifact-root s3://mlflow-bucket-predictive-maintenance`

#### -- Run the following commands in local terminal at Step 7 above:

`pip install boto3`

#### -- For subsequent runs (without logging in to AWS Console)

`aws ec2 start-instances --instance-ids "<id>"`

`aws ec2 describe-instance-status --instance-ids "<id>" | jq '.InstanceStatuses[] | .InstanceState | .Name'`

SSH to EC2 machine and run the command:

`mlflow server --host 0.0.0.0 --default-artifact-root s3://mlflow-bucket-predictive-maintenance`

`aws ec2 stop-instances --instance-ids "<id>"`
