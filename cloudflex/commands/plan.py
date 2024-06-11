import click
from cloudflex.core.parser import parse_config
from cloudflex.core.state import load_state
from cloudflex.utils.cloud_api import get_provider

@click.command()
def plan():
    click.echo("Planning infrastructure changes...")
    
    config = parse_config()
    provider = get_provider(config)
    current_state = load_state()
    desired_state = config['resources']
    
    # Determine the actions required to achieve the desired state
    actions = determine_actions(provider, current_state, desired_state)
    
    # Print the plan
    for action in actions:
        click.echo(action)
    
    click.echo("Plan complete.")

def determine_actions(provider, current_state, desired_state):
    actions = []
    
    # Convert current state and desired state into dictionaries keyed by resource name
    current_resources = {resource['name']: resource for resource in current_state}
    desired_resources = {resource['name']: resource for resource in desired_state}
    
    # Determine resources to create, update, or delete
    for name, resource in desired_resources.items():
        if name not in current_resources:
            actions.append(f"Create {resource['type']} resource '{name}' with configuration: {resource}")
        elif current_resources[name] != resource:
            actions.append(f"Update {resource['type']} resource '{name}' with new configuration: {resource}")
    
    for name, resource in current_resources.items():
        if name not in desired_resources:
            actions.append(f"Delete {resource['type']} resource '{name}'")
    
    return actions