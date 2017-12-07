from src.gorila import banana


def test_peel():
    assert banana.peel() is 'delicious'

def test_failure():
    assert 'you are a failure' == True
