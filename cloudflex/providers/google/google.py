from google.cloud import compute_v1
from cloudflex.utils.logger import get_logger

logger = get_logger(__name__)

class GCPProvider:
    def __init__(self, project, credentials_file, zone):
        self.project = project
        self.credentials_file = credentials_file
        self.zone = zone
        self.client = compute_v1.InstancesClient.from_service_account_json(credentials_file)
        logger.info(f"GCP Provider initialized for project {self.project} in zone {self.zone}")

    def create_instance(self, name, machine_type, source_image):
        logger.info(f"Creating GCP instance: {name}")
        instance = compute_v1.Instance()
        instance.name = name
        instance.machine_type = f"zones/{self.zone}/machineTypes/{machine_type}"
        instance.disks = [
            compute_v1.AttachedDisk(
                boot=True,
                auto_delete=True,
                initialize_params=compute_v1.AttachedDiskInitializeParams(
                    source_image=source_image
                )
            )
        ]

        instance.network_interfaces = [
            compute_v1.NetworkInterface(
                name="global/networks/default"
            )
        ]

        operation = self.client.insert(project=self.project, zone=self.zone, instance_resource=instance)
        operation.result()  # Wait for the operation to complete
        logger.info(f"Instance {name} created")
        return instance.id

    def terminate_instance(self, instance_id):
        logger.info(f"Terminating GCP instance: {instance_id}")
        operation = self.client.delete(project=self.project, zone=self.zone, instance=instance_id)
        operation.result()  # Wait for the operation to complete
        logger.info(f"Instance {instance_id} terminated")