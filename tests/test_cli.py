"""A test conversation provides input and checks what the app prints."""

from calculator.cli import run


def session(monkeypatch, capsys, answers):
    # iter is a cursor; next takes one response for each input prompt.
    responses = iter(answers)

    def scripted_input(prompt):
        return next(responses)

    # pytest supplies these fixtures and restores input after the test.
    monkeypatch.setattr("builtins.input", scripted_input)

    run()

    return capsys.readouterr().out


def test_arithmetic_session(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     ["add", "10", "5", "subtract", "20", "7", "exit"])

    assert "Result: 15" in output
    assert "Result: 13" in output
    assert output.endswith("Exiting the calculator.\n")

def test_invalid_first_number_recovers(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["add", "hello", "history", "add", "2", "3", "exit"])
    assert "Invalid number." in output
    assert "No calculations in history." in output
    assert "Result: 5" in output 

def test_invalid_second_number_recovers(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["subtract", "10", "hello", "history", "subtract", "8", "3", "exit"])
    assert "Invalid number or result." in output 
    assert "No calculations in history." in output 
    assert "Result: 5" in output

def test_invalid_removal_number_preserves_history(monkeypatch,capsys):
    for invalid_number in ["0", "-1", "99"]:
        output = session(monkeypatch, capsys, ["add", "1", "2", "remove", invalid_number, "history", "exit"])
        assert "Calculation does not exist." in output
        assert output.count("1. Add: 1,2 =3") == 1, invalid_number