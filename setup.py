import sys

from distutils.core import setup
from distutils.extension import Extension

if sys.version_info[0] != 3:
    print("This module is only compatible with python 3!")
    sys.exit()

setup(
    name='cobs',
    version='1',
    description='A fixed version of Craigs MqQueen\'s COBS module',
    author='Frédéric St-Pierre, Philippe Babin',
    author_email='frederic.st-pierre.7@ulaval.ca, philippe.babin.1@ulaval.ca',
    url='https://github.com/RobocupUlavalEmbedded/Robocobs',
    install_requires=[],
    packages=['cobs'],
    package_dir={
        'cobs': './cobs',
    }
)

