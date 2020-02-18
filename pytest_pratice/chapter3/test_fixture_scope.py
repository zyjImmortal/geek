import pytest

@pytest.fixture(scope='function')
def func_scope():
    """function scope fixture"""


@pytest.fixture(scope='class')
def class_scope():
    """class scope fixture"""

@pytest.fixture(scope='module')
def module_scope():
    """function scope fixture"""

@pytest.fixture(scope='session')
def session_scope():
    """function scope fixture"""


def test_1( module_scope, func_scope):
    """test use session_scope, module_scope, func_scope"""

def test_2(module_scope, func_scope):
    """mul fuction"""


@pytest.mark.usefixtures('class_scope')
class TestDemo:

    def test_3(self):
        """use class scope fixture"""

    def test_4(self):
        """test mul class method"""