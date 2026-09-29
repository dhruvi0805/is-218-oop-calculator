from calculator.calculation import Add, Subtract, Multiply, Divide

def test_add():
    add = Add(10, 5)
    result = add.get_result()
    assert result == 15
    assert add.a == 10
    assert add.b == 5

def test_Subtract():
    subtract = Subtract(10, 3)
    result = subtract.get_result()
    assert result == 7
    assert subtract.a == 10
    assert subtract.b == 3

def test_Multiply():
    multiply = Multiply(4, 6)
    result = multiply.get_result()
    assert result == 24
    assert multiply.a == 4
    assert multiply.b == 6

def test_Divide():
    divide = Divide(30, 5)
    result = divide.get_result()
    assert result == 6
    assert divide.a == 30 
    assert divide.b == 5
