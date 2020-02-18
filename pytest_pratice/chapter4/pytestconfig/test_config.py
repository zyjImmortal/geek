

def test_option(pytestconfig):
    print("foo set to: ", pytestconfig.getoption('foo'))
    print("bar set to: ", pytestconfig.getoption('myopt'))