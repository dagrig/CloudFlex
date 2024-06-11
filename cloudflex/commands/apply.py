import os
from cloudflex.providers.aws import AWSProvider
from cloudflex.providers.gcp import GCPProvider
from cloudflex.providers.azure import AzureProvider

def get_provider(config):
    provider = config.get('provider')

    if provider == 'aws':
        access_key = config.get('access_key') or os.getenv('AWS_ACCESS_KEY_ID')
        secret_key = config.get('secret_key') or os.getenv('AWS_SECRET_ACCESS_KEY')
        region = config.get('region') or os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

        if not access_key or not secret_key:
            raise ValueError("AWS access key and secret key must be provided either in the configuration file or as environment variables")

        return AWSProvider(access_key, secret_key, region)

    elif provider == 'gcp':
        project = config.get('project')
        credentials_file = config.get('credentials_file')
        zone = config.get('zone')

        if not project or not credentials_file or not zone:
            raise ValueError("GCP project, credentials file and zone must be provided in the configuration file")

        return GCPProvider(project, credentials_file, zone)

    elif provider == 'azure':
        subscription_id = config.get('subscription_id')
        resource_group = config.get('resource_group')
        region = config.get('region')

        if not subscription_id or not resource_group or not region:
            raise ValueError("Azure subscription ID, resource group, and region must be provided in the configuration file")

        return AzureProvider(subscription_id, resource_group, region)

    else:
        raise ValueError(f"Unsupported provider: {provider}")