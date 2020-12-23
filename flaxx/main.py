import typer
from typer import style, echo

from generate_project import generate_project_structure, app_name

app = typer.Typer()


@app.command()
def generate_project(name: str = app_name):
    echo(style("Generating files/folders...", fg=typer.colors.GREEN, bold=True))
    generate_project_structure(name)


@app.command()
def goodbye(name: str, lastname: str = "", formal: bool = False):
    if formal:
        typer.echo(f"Goodbye {name} {lastname}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()