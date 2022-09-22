from app import *


def test_hello():
    result = get_hello()
    assert result == "hello"


def test_add():
    result = add(10, 5)
    assert result == 15
