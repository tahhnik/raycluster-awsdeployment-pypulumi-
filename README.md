# Automated Cloud Architecture Deployment with Pulumi

## Overview

This repository provides infrastructure-as-code (IaC) template to deploy the cloud architecture needed to set up Ray Cluster described in the diagram. 
We'll use Pulumi to automate the provisioning of resources which are needed to set up a multi-node Ray Cluster in your AWS environment.
![diagram-export-6-22-2024-11_17_40-PM](https://github.com/tahhnik/raycluster-awsdeployment-pypulumi/assets/25973761/df25f489-329a-447a-af2e-bfb26c870cb3)

## Prerequisites

1. **Pulumi CLI**: Install the Pulumi CLI on your local machine.
2. **AWS Account**: Ensure you have an AWS account set up.
3. **AWS Credentials**: Configure your AWS credentials (access key and secret key) locally.

## Deployment Steps

# Setting up the Infrastructure for Model Training:

## What is Pulumi?

Pulumi is an open-source infrastructure-as-code software that allows users to manage cloud infrastructure resources using programming languages such as Go, JavaScript, TypeScript, Python, Java, C#, and YAML. It supports deployment to various cloud providers like AWS, Azure, Google Cloud, and Kubernetes

![image](https://github.com/tahhnik/raycluster-awsdeployment-pypulumi/assets/25973761/1cb23ef6-a0f6-4005-8bc0-caeabd496780)


## **Step 1: Install Pulumi**

1. **Open a terminal on your machine**.
2. **Install Pulumi using the installation script**: This command will download and install the latest version of Pulumi. If you want to install a specific version, replace **`v3.120.0`** with your desired version.
    
    `bash$ curl -fsSL https://get.pulumi.com | sh -s -- --version dev`
    

## **Step 2: Verify Installation**

1. **Run the `pulumi` CLI**: This command should display the version of Pulumi installed on your machine.
    
    `bash$ pulumi version
    v3.120.0`
    

## Step 3: Set up Your Pulumi Cloud Account and Connect to Pulumi CLI:

To set up a Pulumi Cloud account and log in to the CLI, follow these steps:

### 3.1: Create a Pulumi Cloud Account

1. **Navigate to the Pulumi Cloud Console**:  [***https://app.pulumi.com***](https://app.pulumi.com)
2. **Create an account** if you don't already have one.
3. **Create and copy the personal access token**
    
    You can find your account’s personal access tokens on the below section,
    

![image](https://github.com/tahhnik/raycluster-awsdeployment-pypulumi/assets/25973761/057794aa-46a2-479f-9412-71e45af90f32)


### 3.2: Configure Your Pulumi CLI

1. **Run `pulumi login`**:
    
    ```bash
    $ pulumi login
    ```
    
    This command will prompt you to log in to your Pulumi Cloud account.
    
2. **Enter your access token**:
    
    `bash$ Enter your access token from https://app.pulumi.com/account/tokens`
    

### 3.3: Verify the Login

1. **Run `pulumi about`**:
    
    ```bash
    **$ pulumi about**
    ```
    
    This command will display information about your Pulumi CLI, including your backend, user, and organizations.

# Follow rest of the instructions on the Lab Prompt to Finish setting up the Infrastructure Deployment


