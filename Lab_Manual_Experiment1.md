AIM

To set up a reproducible Machine Learning project environment using Git and Conda, and integrate it with Azure Machine Learning Workspace using Visual Studio Code for cloud-based experimentation.

OBJECTIVES

To install and configure Git for version control.

To create and manage isolated Python environments using Conda.

To install required Machine Learning and Azure SDK libraries.

To initialize a Git repository and track project files.

To connect the local development environment with Azure ML Workspace.

To verify successful cloud integration using Azure ML Python SDK.

REQUIREMENTS
Hardware Requirements

Computer with internet connectivity

Minimum 8 GB RAM (recommended)

Azure ML Compute Instance / Local Machine

Software Requirements

Visual Studio Code

Git

Anaconda / Miniconda

Python 3.10

Azure Account

Azure ML Workspace

Python Libraries

azureml-core

azure-ai-ml

numpy

pandas

scikit-learn

jupyter

THEORY

Modern Machine Learning workflows require reproducibility, version control, and cloud scalability.

Git Version Control

Git is a distributed version control system used to track changes in source code, manage collaboration, and maintain experiment history. It helps ensure code consistency and rollback capability.

Conda Environment

Conda is an environment management tool that creates isolated Python environments. This ensures consistent dependency versions and avoids conflicts between libraries.

Reproducibility is achieved by exporting environment dependencies into configuration files such as:

requirements.txt

environment.yml

Azure Machine Learning Workspace

Azure ML Workspace is a cloud platform that provides tools for:

Model training

Experiment tracking

Resource management

Deployment integration

Using the Azure ML Python SDK, developers can authenticate and interact with cloud resources directly from local development environments.

VS Code Integration

Visual Studio Code provides an integrated development environment that supports:

Terminal execution

Jupyter notebooks

Git integration

Azure ML extensions

This allows seamless offline and cloud-based ML development.

PROCEDURE
Step 1: Verify Git Installation
git --version

Step 2: Configure Git
git config --global user.name "YourName"
git config --global user.email "yourmail@gmail.com"
git config --list

Step 3: Verify Conda Installation
conda --version

Step 4: Create Conda Environment
conda create -n mlops_env python=3.10

Step 5: Activate Environment
conda activate mlops_env

Step 6: Install Required Packages
pip install azureml-core azure-ai-ml numpy pandas scikit-learn jupyter

Step 7: Initialize Git Repository
git init

Step 8: Commit Project Files
git add .
git commit -m "Initial MLOps environment setup"

Step 9: Verify Jupyter Installation
jupyter notebook

Step 10: Create Azure ML Workspace

Login to Azure Portal

Create Azure Machine Learning Workspace

Download config.json file

Step 11: Connect Workspace Using SDK
from azureml.core import Workspace
ws = Workspace.from_config()
print(ws.name)

OUTPUT
Git Verification Output
git version 2.50.1

Conda Environment Verification
mlops_env *

Package Installation Verification
azureml-core installed successfully
jupyter installed successfully

Workspace Connection Output
ml-workspace-ai


This confirms successful connection with Azure ML Workspace.

RESULT

The Machine Learning project environment was successfully created using Conda and Git.
Azure ML Workspace was integrated using Python SDK and verified through workspace authentication.

CONCLUSION

In this experiment, a reproducible ML development environment was successfully configured. Git ensured proper version control, Conda provided isolated dependency management, and Azure ML Workspace enabled cloud integration. This setup forms the foundation for scalable Machine Learning pipelines and cloud-based experimentation.