# Command Line Tutorial

## Command Line Basics
1. Arguments: Required parameter. Example: `pip install django`
2. Options: Unrequired parameter. Example: `pip install django --cache-dir ./dir`
3. Flag: Enable or disable a certain feature. Example: `pip install django --verbose`

## Different Technologies Used
1. Argparse: Works, but is faily complicated and not very scalable.
2. Click: Good for simple, non-interactive CLIs.
3. PyInquirer: Necessary for interactive CLIs that are dynamic and easier to use.

## Click CLI Notes
1. `@click.command()`: The core command that is executed when the CLI is called.
2. `@click.group()`: Adding multiple commands to the CLI nested under one core CLI function.
3. `@click.option('--option_name', default=N, help='Details about option')`: Add an option to the CLI.
4. `@click.argument('argument_name')`: Add an argument to the CLI.

Learn more Click: https://click.palletsprojects.com/en/8.0.x/ 
