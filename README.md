# ssm-simple-cli

[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=shield)](https://circleci.com/gh/circleci/circleci-docs)

A Python based CLI that works with [AWS Systems Manager Parameter Store] in the simplest way possible.
Powered by [Boto3] & [Click]!

## Main Features
- Simple, intuitive and easy to use CLI to use as password managemant tool!
- Levraging AWS password managemant capabilities and without cost! Free of charge!
- Quick installation & lightweight
- Duality - Allows using both as CLI for developer to utilize and as also as a Python client to run in CI
- Hight test coverage for a reltively simple CLI

> The ssm-simple-cli is designated to act primarily as a CLI but it also allows using it as a Python client.
> Most of the instructions below will help you setup & use the ssm-simple-cli as a plain CLI.
> If you are interested in using it as a client within Python code you can read more in the [Development](#development) section. 

## Installation
### Please make sure:
- You have Python 3 version installed.
- You are NOT on any virtualenv
- You have configured AWS credentials with the neccessary user profile permissions. See [AWS Permissions section](#aws-permissions--credentials) for more information.

```sh
$ pip install ssm-simple-cli
```
## Initial Setup

> Since ssm-simple-cli uses [AWS Systems Manager Parameter Store] behind the scenes, you must have a valid AWS account with crednetials set up. See [AWS Permissions section](#aws-permissions--credentials) for more info.

After a fresh install, you will have to configure you cli for the first time:

```sh
$ ssm configure
```

This will require you to enter you AWS account credentials. You can also configure the ssm-simple-cli to point to a specific named AWS profile:

```sh
$ ssm configure -p <my-desired-aws-profile-name>
```

> To read more about multiple AWS profiles support [click here](#multiple-aws-profile-support).

## Usage

Once ssm-siple-cli was configure, simply type `ssm` in you desired shell to show the main help menu:

```console
$ ssm

Usage: ssm [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  configure  Setup an initial configuration for this cli
  describe   Retrieve a list of available secrets
  get        Retrieve a specific secret.
  put        Submit a new secret to the SSM store
```

You can also use the `--help` flag on a specific command to find our more about it and its parameters:

```sh
$ ssm describe --help

Usage: ssm describe [OPTIONS]

  Retrieve a list of available secrets

Options:
  -c, --copy       Copies the selected secret value to your clipboard
  -g, --get        Give you a prompt to choose which secret to get
  -p, --path TEXT  Describe only parameters located in a specific path (must start with "/")

  --help           Show this message and exit.

```

## AWS permissions & credentials 

In order to run the ssm-simple-cli you must have a valid AWS account, AWS credentials and basic permissions to the [AWS Systems Manager Parameter Store]. Please read below in order to get more details.

### AWS Account
Just go to the [AWS homepage](https://aws.amazon.com/) and create an account. No initial sum requied!

### Credentials

AWS credentials are usually configured using the [aws-cli]. you should install the cli and then configure your AWS credentials using this command:

```sh
$ aws configure
```

[Click here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration-creds) for more information on how to obtain such credentials

Once you have these credentials in place you will be able to [setup](#initial-setup) the ssm-simple-cli.

##### Multiple AWS Profile Support!
When you setup the [aws-cli], credentials are stored in a default AWS profile however if you use multiple [named AWS profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) the ssm-simple-cli totally supports this!

> By default the ssm-simple-cli uses the "default" AWS profile

To view what current AWS profile I'm using simply run

```sh
$ ssm configure -s
```

This will print the curent AWS named profile the ssm-simple-cli is using.

If you wish to configure a different named AWS profile:

```sh
$ ssm configure -p <my-desired-aws-profile-name>
```

This will direct the ssm-simple-cli to use crednetials for this specific named AWS profile

### Permissions

Your user must have the proper permissions in AWS Systems Manager Parameter Store. See [this example](examples/aws/policy) in this repo for more information.


## Development

### Running within Python code
> Can be run in CI!

The ssm-simple-cli also allows running the actual commands within Python code. This provides a more holistic use of the same password mangemant tool & code in both the developer terminal & the actual CI build. Highly recommended!

To import the Python client code simply import the following classes:
```python
from cli.src.ssm_cli import CliConfiguration
from cli.src.ssm_client import SSMClient
```

To initialize the client simply configure a `CLIConfiguration` and provide it to the client

```python
 # by default the ssm-simple-cli configuration file sits at '~/.ssm/config' but can be anywhere
config = CliConfiguration('<configuration-file-path>')
client = SSMClient(config)
```

### Testing

ssm-simple-cli utilizes [PyTest], [PyTest Fixtures] and [Moto] to run Unit + Integration Tests.

To run the tests simply type the following in main folder:

```bash
$ pip install -r requirements.txt
$ pytest

```

### Todos

 - Add MORE Tests
 - Add Test coverage and codecov
 - Consider adding "delete" capability (Did not do it since it may be harmful)


### Enhancements & Ideas

I'm open to both! Contact me via the details in Github

License
----

MIT

[//]: #
   [Boto3]: <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>
   [Click]: <https://click.palletsprojects.com>
   [aws-cli]: <https://aws.amazon.com/cli>
   [AWS Systems Manager Parameter Store]: <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [PyTest]: <https://docs.pytest.org>
   [PyTest Fixtures]: <https://docs.pytest.org/en/latest/fixture.html#fixture>
   [Moto]: <http://docs.getmoto.org/en/latest>
