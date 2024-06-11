from setuptools import setup, find_packages

setup(
    name='cloudflex',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'azure-mgmt-resource',
        'google-cloud',
        'pyyaml',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'cloudflex=cloudflex.cli:main',
        ],
    },
)