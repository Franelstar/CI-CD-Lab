from click.testing import CliRunner
from main import cli


def test_add_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ["add-cmd", "3", "4"])
    assert result.exit_code == 0
    assert result.output.strip() == "7"


def test_div_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "10", "0"])
    assert result.exit_code == 0
    assert "Division by zero" in result.output
