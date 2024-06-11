import click
from cloudflex.core.parser import parse_config
from cloudflex.core.state import load_state, save_state
from cloudflex.utils.cloud_api import get_provider

@click.command()
def destroy():
    click.echo("Destroying infrastructure...")
    
    config = parse_config()
    provider = get_provider(config)
    state = load_state()
    
    # Example of destroying resources for an AWS EC2 instance
    for resource_name, instance_id in state.items():
        provider.terminate_instance(instance_id)
        del state[resource_name]
    
    save_state(state)
    click.echo("Infrastructure destroyed successfully.")