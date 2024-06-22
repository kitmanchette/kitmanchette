import pytest
from project import get
from project import ask
from project import convert


def test_get(monkeypatch):
    #using monkeypatch to mock correct user input
    monkeypatch.setattr('builtins.input', lambda _: "Ni")
    inp = input("Atomic symbol: ")
    assert inp == "Ni"
    #using monkeypatch to mock incorrect user input: invalid atomic symbol
    monkeypatch.setattr('builtins.input', lambda _: "cat")
    with pytest.raises(ValueError):
        get()


def test_ask(monkeypatch):
    #using monkeypatch to mock incorrect user input: invalid atomic percent
    monkeypatch.setattr('builtins.input', lambda _: "cat")
    with pytest.raises(ValueError):
        get()

#ensure calculations are done correctly to three decimal places
def test_convert():
    #given one element, no matter what 'a' is, weight percent returned should be 100
    e = ["Ni"]
    a = [90]
    assert convert(e,a) == ['100.000']
    e = ["Ni", "P"]
    a = [80, 20]
    assert convert(e,a) == ['88.346', '11.654']
    #program should prompt user if atomic percents sum to 0
    e = ["Ni"]
    a = [0]
    with pytest.raises(ZeroDivisionError):
        convert(e,a)
