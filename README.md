```markdown
# CloudFlex

CloudFlex is a simple CLI tool for managing cloud infrastructure. It supports basic operations such as initializing a project, planning changes, applying changes, and destroying infrastructure.

## Features

- **Initialize**: Set up the initial configuration for your CloudFlex project.
- **Plan**: Generate and display an execution plan for infrastructure changes.
- **Apply**: Apply the planned changes to your cloud infrastructure.
- **Destroy**: Tear down and destroy the infrastructure managed by CloudFlex.

## Requirements

- Python 3.7+
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/dagrig/CloudFlex.git
    cd cloudflex
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Install the CloudFlex CLI tool:

    ```sh
    python setup.py install
    ```

## Usage

### Commands

#### `init`

Initialize the CloudFlex project.

```sh
cloudflex init
```

#### `plan`

Generate and display an execution plan for infrastructure changes.

```sh
cloudflex plan
```

#### `apply`

Apply the planned changes to your cloud infrastructure.

```sh
cloudflex apply
```

#### `destroy`

Tear down and destroy the infrastructure managed by CloudFlex.

```sh
cloudflex destroy
```

### Configuration

CloudFlex uses a configuration file named `cloudflex.yaml` to define the infrastructure details. Here is an example configuration file:

```yaml
provider: aws
aws_access_key: YOUR_ACCESS_KEY
aws_secret_key: YOUR_SECRET_KEY
region: us-east-1

resources:
  - type: ec2
    name: my-instance
    ami: ami-12345678
    instance_type: t2.micro
```

### State Management

CloudFlex maintains its state in a file named `cloudflex_state.json` to keep track of the current state of your infrastructure.

### Logging

Logs are output to the console to help you understand the operations being performed. You can find the logging configuration in the `cloudflex/utils/logger.py` file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE V3 - see the [LICENSE](LICENSE) file for details.
