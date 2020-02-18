from setuptools import setup

setup(
    name='pytest_nice',
    version='1.0.0',
    description='A new PLugin',
    url="https://immortalp.com/",
    author="zyj",
    license='',
    py_modules=['pytest_nice'],
    install_requires=['pytest'],
    entry_points={
        'pytest11':[
            'nice = pytest_nice',
        ],
    },
)
