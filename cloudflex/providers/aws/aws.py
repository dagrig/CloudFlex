import boto3
from cloudflex.utils.logger import get_logger

logger = get_logger(__name__)

class AWSProvider:
    def __init__(self, access_key, secret_key, region):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.ec2 = boto3.resource(
            'ec2',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )
        logger.info(f"AWS Provider initialized for region {self.region}")

    def create_instance(self, ami, instance_type, name):
        logger.info(f"Creating EC2 instance: {name}")
        instance = self.ec2.create_instances(
            ImageId=ami,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': name}]
            }]
        )[0]
        instance.wait_until_running()
        logger.info(f"Instance {name} created with ID: {instance.id}")
        return instance.id

    def terminate_instance(self, instance_id):
        logger.info(f"Terminating EC2 instance: {instance_id}")
        instance = self.ec2.Instance(instance_id)
        instance.terminate()
        instance.wait_until_terminated()
        logger.info(f"Instance {instance_id} terminated")