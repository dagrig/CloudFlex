from google.cloud import compute_v1
from google.oauth2 import service_account
from cloudflex.utils.logger import get_logger

logger = get_logger(__name__)

class GoogleProvider:
    def __init__(self, project_id, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = compute_v1.InstancesClient(credentials=self.credentials)
        self.project_id = project_id

    def create_instance(self, zone, name, machine_type, source_image, network):
        logger.info(f"Creating GCP instance: {name}")
        instance = compute_v1.Instance()
        instance.name = name
        instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"

        disk = compute_v1.AttachedDisk()
        disk.initialize_params = compute_v1.AttachedDiskInitializeParams()
        disk.initialize_params.source_image = source_image
        instance.disks = [disk]

        network_interface = compute_v1.NetworkInterface()
        network_interface.name = network
        instance.network_interfaces = [network_interface]

        operation = self.client.insert(
            project=self.project_id, zone=zone, instance_resource=instance
        )
        operation.result()
        logger.info(f"Instance {name} created")

    def delete_instance(self, zone, instance_name):
        logger.info(f"Deleting GCP instance: {instance_name}")
        operation = self.client.delete(
            project=self.project_id, zone=zone, instance=instance_name
        )
        operation.result()
        logger.info(f"Instance {instance_name} deleted")