"""A test conversation provides input and checks what the app prints."""

from calculator.cli import run
import runpy


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

def test_invalid_removal_number(monkeypatch, capsys):
    output = session(
        monkeypatch,
        capsys,
        ["remove", "hello", "exit"]
    )

    assert "Invalid removal number." in output

def test_invalid_removal_number_preserves_history(monkeypatch,capsys):
    for invalid_number in ["0", "-1", "99"]:
        output = session(monkeypatch, capsys, ["add", "1", "2", "remove", invalid_number, "history", "exit"])
        assert "Calculation does not exist." in output
        assert output.count("1. Add: 1,2 =3") == 1, invalid_number

def test_finite_first_number_rejects(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["add", "nan", "5","history", "exit"])
    assert "Number must be finite." in output
    assert "No calculations in history." in output

def test_finite_second_number_rejects(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["add", "5", "inf", "history", "exit"])
    assert "Number must be finite." in output
    assert "No calculations in history." in output

def test_keyboard_interrupt_exits(monkeypatch, capsys):
    def interrupting_input(prompt):
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", interrupting_input)

    run()

    output = capsys.readouterr().out
    assert "Exiting the calculator." in output

def test_remove_from_empty_history(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["remove", "1", "exit"])
    assert "Calculation does not exist." in output

def test_remove_middle_calculation(monkeypatch, capsys):
    output = session(monkeypatch, capsys, 
                     [
                         "add", "1", "2",
                         "subtract", "10", "3",
                         "multiply", "4", "5",
                         "remove", "2",
                        "history",
                        "exit"
                     ])
    assert "1. Add: 1,2 =3" in output
    assert "2. Multiply: 4,5 =20" in output
    assert "3. Subtract: 10,3 =7" not in output

def test_remove_last_calculation(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     [
                        "add", "1", "2",
                        "subtract", "10", "3",
                        "multiply", "4", "5",
                        "remove", "3",
                        "history",
                        "exit"
                     ])
    assert "1. Add: 1,2 =3" in output 
    assert "2. Subtract: 10,3 =7" in output

def test_remove_only_entry(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     [
                         "add", "1", "2",
                         "remove", "1",
                         "history",
                         "exit"
                     ])
    assert "No calculations in history." in output

def test_package_entry_point(monkeypatch, capsys):
    # runpy runs the package's __main__.py as if it were a script.
    inputs = iter(["exit"])

    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    runpy.run_module("calculator", run_name="__main__")

    output = capsys.readouterr().out
    assert "Exiting the calculator." in output

def test_decimal_inputs(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["add", "3.5", "2.1", "exit"])
    assert "Result: 5.6" in output

def test_negative_inputs(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["subtract", "-5", "-3", "exit"])
    assert "Result: -2" in output

def test_help_command(monkeypatch,capsys):
    output = session(monkeypatch, capsys, ["help", "exit"])
    assert "Available commands: add, subtract, multiply, divide, help, exit" in output
    assert "Exiting the calculator." in output

def test_main_module_imported():
    import runpy
    runpy.run_module("calculator.__main__", run_name="calculator.__main__")