from azureml.core import Workspace, Environment

# Load workspace from config.json
ws = Workspace.from_config()

# Create environment from YAML
env = Environment.from_conda_specification(
    name="mlops-env",
    file_path="environments/azureml-env.yml"
)

# Register environment
env.register(workspace=ws)

print("Environment registered successfully")
