from azureml.core import Workspace

ws = Workspace.from_config()
print("CONNECTED TO:", ws.name)
