import click
from cloudflex.core.parser import parse_config
from cloudflex.core.state import save_state, load_state
from cloudflex.utils.cloud_api import get_provider

@click.command()
def destroy():
    click.echo("Destroying infrastructure...")
    
    config = parse_config()
    provider = get_provider(config)
    state = load_state()
    
    for resource_name, resource_id in state.items():
        provider.terminate_instance(resource_id)
        click.echo(f"Instance {resource_name} with ID {resource_id} terminated")
    
    state.clear()
    save_state(state)