from install_here.hello import hello


def test_hello():
    actual = hello()
    assert actual == "hi"
