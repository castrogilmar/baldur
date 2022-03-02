# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from baldur import __version__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

__date__ = '20220302'

setup(
    name = 'baldur',
    version = __version__,
    description = 'BALDUR - A Python package for integration with api of control-mobile app',
    long_description = readme,
    author = 'Gilmar de Castro',
    author_email = 'castro.gilmar@hotmail.com',
    long_description = readme,
    url = 'https://',
    license = license,
    install_requires = requirements,
    packages = find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',        
    ],
    scripts=['bin/baldur'],
    data_files=[('/var/lib/baldur', ['config/conf.json'])],
)