import simple

def test_add_numbers():
    assert simple.add_numbers(3, 5) == 8
    assert simple.add_numbers(-1, 1) == 0
    assert simple.add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert simple.subtract_numbers(10, 5) == 5
    assert simple.subtract_numbers(-1, 1) == -2
    assert simple.subtract_numbers(0, 0) == 0