# predictive-maintenance

# MLFlow on AWS

1. Login to AWS console
2. Create IAM user with 'AdministratorAccess' policy
3. Export security credentials (CLI access keys) in AWS CLI and run 'aws configure'
4. Create S3 bucket to store artifacts
5. Create an EC2 machine (Ubuntu), add Security Groups and open Port 5000

## Run the following commands on EC2 machine:

sudo apt update
sudo apt install python3-pip
sudo pip3 install pipenv
sudo pip3 install virtualenv

mkdir mlflow
cd mlflow

pipenv install mlflow
pipenv install awscli
pipenv install boto3
pipenv shell

aws configure

mlflow server --host 0.0.0.0 --default-artifact-root s3://mlflow-bucket-predictive-maintenance

6. Open public IPV4 address of the EC2 machine on port 5000

7. In the local terminal:
pip install boto3

# Set MLflow tracking URI in the local terminal and code
export MLFLOW_TRACKING_URL=http://ec2-3-110-32-142.ap-south-1.compute.amazonaws.com:5000

