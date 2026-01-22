import typer

app = typer.Typer()

VERSION = "1.1.0"

CAT = r"""  \
   \
    /\_/\
   ( o.o )
    > ^ <"""


def make_bubble(message: str) -> str:
    lines = message.split("\n")
    max_len = max(len(line) for line in lines)
    border = "-" * (max_len + 2)

    bubble_lines = [f" {border} "]
    for line in lines:
        bubble_lines.append(f"| {line.ljust(max_len)} |")
    bubble_lines.append(f" {border} ")

    return "\n".join(bubble_lines)


def version_callback(value: bool):
    if value:
        print(f"pycatsay {VERSION}")
        raise typer.Exit()


@app.command()
def main(
    message: str = typer.Argument("Meow!", help="Message for the cat to say"),
    version: bool = typer.Option(False, "--version", "-v", callback=version_callback, is_eager=True),
):
    """A cat that says things in your terminal."""
    print(make_bubble(message))
    print(CAT)


if __name__ == "__main__":
    app()
