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