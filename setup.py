from setuptools import setup, find_packages
from mytestpackage import __version__

setup(
    name='mytestpackage-gcampini',
    version=__version__,
    description='A small example package',
    author='Gil Campini',
    install_requires=['numpy'],
    packages=find_packages(),
)
