#!/usr/bin/env python
from setuptools import setup


setup(
    name='nameko_test',
    packages=['nameko_test'],
    install_requires=[
        'nameko',
        'click',
    ],
)
