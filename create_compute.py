from azureml.core import Workspace
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config()

cluster_name = "cpu-cluster"

try:
    compute_target = ComputeTarget(workspace=ws, name=cluster_name)
    print("Compute already exists:", cluster_name)

except ComputeTargetException:
    print("Creating new compute cluster...")

    compute_config = AmlCompute.provisioning_configuration(
        vm_size="STANDARD_DS3_V2",
        min_nodes=0,
        max_nodes=2
    )

    compute_target = ComputeTarget.create(ws, cluster_name, compute_config)
    compute_target.wait_for_completion(show_output=True)

print("Compute Ready:", compute_target.name)
