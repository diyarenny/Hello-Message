def hello(name):
     return"Hello " + name

def test_hello():
    assert "Hello Frank" == hello("Frank")  