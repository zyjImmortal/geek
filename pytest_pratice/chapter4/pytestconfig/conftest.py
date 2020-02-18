

def pytest_addoption(parser):
    parser.addoption('--myopt', action='store_true', help='a boolean option')
    parser.addoption('--foo', action='store', default='bar', help='foo: bar or baz')

