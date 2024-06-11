import click
import os
import yaml

@click.command()
def init():
    click.echo("Initializing CloudFlex project...")
    
    if not os.path.exists('cloudflex.yaml'):
        provider = click.prompt('Enter cloud provider (e.g., aws, gcp, azure)', type=str)
        access_key = click.prompt('Enter your access key', hide_input=True)
        secret_key = click.prompt('Enter your secret key', hide_input=True)
        region = click.prompt('Enter your region', type=str)
        
        example_config = {
            'provider': provider,
            'access_key': access_key,
            'secret_key': secret_key,
            'region': region,
            'resources': []
        }
        
        with open('cloudflex.yaml', 'w') as file:
            yaml.dump(example_config, file)
        click.echo("Configuration file created: cloudflex.yaml")
    else:
        click.echo("Configuration file already exists: cloudflex.yaml")