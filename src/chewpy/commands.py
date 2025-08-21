from chewpy.translator import app as translator_app
from typer import Typer

app = Typer()
app.add_typer(translator_app, name="translator", help="Translator utility")


@app.command()
def hello(name: str = "giraycoskun.dev"):
    print(f"Hello {name}!")


@app.command()
def goodbye(name: str = "giraycoskun.dev"):
    print(f"Goodbye {name}!")
