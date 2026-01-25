from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment

ml_client = MLClient.from_config(credential=DefaultAzureCredential())

env = Environment(
    name="research-env-custom",
    description="Custom reproducible ML research environment",
    conda_file="environments/azureml-env.yml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04"
)

ml_client.environments.create_or_update(env)

print("Environment registered successfully")
