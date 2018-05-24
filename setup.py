from setuptools import setup

long_description = open('README.rst').read()

setup(
    name='microbitdongle',
    decription='allows you to be able to communicate with a microbit over serial',
    version='0.3.11',
    author='Luke Spademan',
    author_email='info@lukespademan.com',
    packages=['microbitdongle'],
    install_requires=[package for package in open('requirements.txt').read().split("\n")],
    long_description = long_description,
    url='https://github.com/lukespademan/microbitdongle',
    download_url ='https://github.com/lukespademan/microbitdongle/archive/0.1.tar.gz'
)
