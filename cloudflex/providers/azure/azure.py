from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
from cloudflex.utils.logger import get_logger

logger = get_logger(__name__)

class AzureProvider:
    def __init__(self, subscription_id):
        self.credential = DefaultAzureCredential()
        self.client = ResourceManagementClient(self.credential, subscription_id)

    def create_resource_group(self, resource_group_name, location):
        logger.info(f"Creating resource group: {resource_group_name}")
        resource_group_params = {'location': location}
        resource_group = self.client.resource_groups.create_or_update(
            resource_group_name, resource_group_params
        )
        logger.info(f"Resource group {resource_group_name} created")
        return resource_group

    def delete_resource_group(self, resource_group_name):
        logger.info(f"Deleting resource group: {resource_group_name}")
        delete_async_operation = self.client.resource_groups.begin_delete(resource_group_name)
        delete_async_operation.wait()
        logger.info(f"Resource group {resource_group_name} deleted")