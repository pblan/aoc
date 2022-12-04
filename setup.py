# setup py file for aoc
from setuptools import setup, find_packages

setup(
    name='aoc',
    version='0.1',
    packages=find_packages(),
    author='Patrick Gustav Blaneck',
    url='https://github.com/pblan/aoc',
    license='GPLv3',
    description='Advent of Code',
    long_description=open('README.md').read(),
)