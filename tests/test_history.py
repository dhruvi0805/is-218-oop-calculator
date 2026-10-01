import pytest

from calculator.history import history

def test_add():
    history = history()
    history.add(Add(10, 5))
    assert len(history.get_history()) == 1

