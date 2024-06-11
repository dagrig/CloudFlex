from cloudflex.providers.aws import AWSProvider
from cloudflex.providers.azure import AzureProvider
from cloudflex.providers.google import GoogleProvider

def get_provider(config):
    provider_type = config.get('provider')
    
    if provider_type == 'aws':
        return AWSProvider(
            access_key=config['aws_access_key'],
            secret_key=config['aws_secret_key'],
            region=config['region']
        )
    elif provider_type == 'azure':
        return AzureProvider(
            subscription_id=config['azure_subscription_id']
        )
    elif provider_type == 'google':
        return GoogleProvider(
            project_id=config['google_project_id'],
            credentials_path=config['google_credentials_path']
        )
    else:
        raise ValueError(f"Unsupported provider: {provider_type}")