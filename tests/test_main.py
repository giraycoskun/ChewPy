from typer.testing import CliRunner

from chewpy import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app=app, args=["hello"])
    assert result.exit_code == 0
    assert result.output == "Hello giraycoskun.dev!\n"
