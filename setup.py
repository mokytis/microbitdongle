from setuptools import setup

setup(
    name='microbitdongle',
    decription='allows you to be able to communicate with a microbit over serial',
    author='Luke Spademan',
    author_email='info@lukespademan.com',
    packages=['microbitdongle'],
    install_requires=[package for package in open('requirements.txt').read().split("\n")],
    zip_safe=False
)
