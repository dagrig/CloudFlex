import click
import os
from cloudflex.core.parser import parse_config

@click.command()
def init():
    click.echo("Initializing CloudFlex project...")
    
    if not os.path.exists('cloudflex.yaml'):
        example_config = {
            'provider': 'aws',
            'aws_access_key': 'YOUR_ACCESS_KEY',
            'aws_secret_key': 'YOUR_SECRET_KEY',
            'region': 'us-east-1',
            'resources': [
                {
                    'type': 'ec2',
                    'name': 'my-instance',
                    'ami': 'ami-12345678',
                    'instance_type': 't2.micro'
                }
            ]
        }
        with open('cloudflex.yaml', 'w') as file:
            yaml.dump(example_config, file)
        click.echo("Example configuration file created: cloudflex.yaml")
    else:
        click.echo("Configuration file already exists: cloudflex.yaml")