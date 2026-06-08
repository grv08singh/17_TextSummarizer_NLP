# End to end Text Summarization Project

## Process to run on local machine:
### STEP 01: Clone the repository
```bash
git clone https://github.com/grv08singh/17_TextSummarizer_NLP
```
### STEP 02: Create a conda environment and activate it
```bash
conda create -n env_txt_summarizer python=3.12.13 -y
conda activate env_txt_summarizer
```
### STEP 03: install the requirements and run the app
```bash
pip install -r requirements.txt
python app.py
```

### STEP 04: open url in browser - http://localhost:8080/






Author: Gaurav Singh
Data Scientist
Email: grv08singh@gmail.com









## Project Development Workflow:
1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update entity
5. Update the configuration manager in src/config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update dvc.yaml [optional]
10. Update app.py

## Description about the deployment - High Level Understanding
1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2 
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2

## Docker
1. Write code in Dockerfile
2. Write code in .github/workflows/main.yaml

## Deploy on AWS cloud using CI/CD-Deployment with Github-Actions and Docker Image
### 1. Login to AWS console.
### 2. Create IAM user with below two Policies:
	- AmazonEC2ContainerRegistryFullAccess
	- AmazonEC2FullAccess
### 3. Create ECR repo to store/save docker image
    - Save the URI: 676206921654.dkr.ecr.us-east-1.amazonaws.com/text-s
### 4. Create EC2 machine (Ubuntu)
	- use a PyTorch GPU machine for faster training
	- keep RAM at least 16 GB and Disk space at least 30GB
	- Create Key and save it
	- Tick all HTTP, HTTPS links
### 5. Open EC2 and Install docker in EC2 Machine:
	# optinal (update package installer)
		sudo apt-get update -y
		sudo apt-get upgrade
	# required (install and run docker)
		curl -fsSL https://get.docker.com -o get-docker.sh
		sudo sh get-docker.sh
		sudo usermod -aG docker ubuntu
		newgrp docker
### 6. Configure EC2 as self-hosted runner:
    GitHub Repo>setting>actions>runner>new self hosted runner> choose os>
	Run commands on EC2 terminal one by one
### 7. Setup github secrets:
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_REGION = us-east-1
    AWS_ECR_LOGIN_URI = 676206921654.dkr.ecr.us-east-1.amazonaws.com
    ECR_REPOSITORY_NAME = text-s
### 8. Push code from local to Github (CI CD pipeline will work automatically)




## AWS terminology explanation:
1. EC2: It is virtual machine
2. ECR: Elastic Container registry to save your docker image in aws
