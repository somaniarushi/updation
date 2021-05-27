import click

@click.group()
def main():
	pass

@main.command()
@click.option('--a', prompt='Enter the first number', type=int, default=0)
@click.option('--b', prompt='Enter the second number', type=int, default=0)
def add(a, b):
	value = a + b
	click.echo(f"The added value: {value}")

if __name__ == "__main__":
	main()
