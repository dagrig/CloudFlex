from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption
from cloudflex.utils.logger import get_logger
from azure.mgmt.network import NetworkManagementClient

logger = get_logger(__name__)

class AzureProvider:
    def __init__(self, subscription_id, resource_group, region):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.region = region
        self.credentials = DefaultAzureCredential()
        self.client = ComputeManagementClient(self.credentials, self.subscription_id)
        logger.info(f"Azure Provider initialized for subscription {self.subscription_id} in region {self.region}")

    def create_instance(self, name, vm_size, image_reference):
        logger.info(f"Creating Azure VM: {name}")

        nic_parameters = {
            'location': self.region,
            'ip_configurations': [{
                'name': f'{name}-ipconfig',
                'subnet': {
                    'id': f'/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}/providers/Microsoft.Network/virtualNetworks/myVnet/subnets/mySubnet'
                }
            }]
        }
        
        network_client = NetworkManagementClient(self.credentials, self.subscription_id)
        nic = network_client.network_interfaces.begin_create_or_update(
            self.resource_group,
            f'{name}-nic',
            nic_parameters
        ).result()

        vm_parameters = {
            'location': self.region,
            'hardware_profile': {
                'vm_size': vm_size
            },
            'storage_profile': {
                'image_reference': image_reference,
                'os_disk': {
                    'caching': 'ReadWrite',
                    'managed_disk': {
                        'storage_account_type': 'Standard_LRS'
                    },
                    'name': f'{name}-osdisk',
                    'create_option': DiskCreateOption.from_image
                },
            },
            'os_profile': {
                'admin_username': 'azureuser',
                'computer_name': name,
                'admin_password': 'Password1234!'  # Replace with a secure password
            },
            'network_profile': {
                'network_interfaces': [{
                    'id': nic.id,
                    'primary': True
                }]
            }
        }

        async_vm_creation = self.client.virtual_machines.begin_create_or_update(
            self.resource_group, name, vm_parameters)
        vm = async_vm_creation.result()

        logger.info(f"VM {name} created with ID: {vm.id}")
        return vm.id

    def terminate_instance(self, instance_id):
        logger.info(f"Terminating Azure VM: {instance_id}")
        async_vm_deletion = self.client.virtual_machines.begin_delete(
            self.resource_group, instance_id)
        async_vm_deletion.result()
        logger.info(f"VM {instance_id} terminated")