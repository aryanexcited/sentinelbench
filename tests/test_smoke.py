import sentinelbench, math

def test_sqrt_of_nine():
    assert math.sqrt(9) == 3

def test_version():
    assert sentinelbench.__version__ == "0.1.0"