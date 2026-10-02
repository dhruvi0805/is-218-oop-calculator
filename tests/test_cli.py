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