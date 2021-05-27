import click

@click.command()
@click.argument('name')
@click.option('--greeting', '-g')
def main(name, greeting):
	click.echo(f"{greeting},{name}")

if __name__== "__main__":
	main()
