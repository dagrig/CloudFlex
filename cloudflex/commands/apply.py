import click
from cloudflex.core.parser import parse_config
from cloudflex.core.state import save_state, load_state
from cloudflex.utils.cloud_api import get_provider

@click.command()
def apply():
    click.echo("Applying infrastructure changes...")
    
    config = parse_config()
    provider = get_provider(config)
    state = load_state()
    
    # Example of applying changes for an AWS EC2 instance
    for resource in config['resources']:
        if resource['type'] == 'ec2':
            instance_id = provider.create_instance(
                ami=resource['ami'],
                instance_type=resource['instance_type'],
                name=resource['name']
            )
            state[resource['name']] = instance_id
    
    save_state(state)
    click.echo("Infrastructure changes applied successfully.")