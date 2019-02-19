# coding: utf-8

import sys

from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

NAME = "urllib_s3"
VERSION = '0.0.5'

REQUIRES = [
    'setuptools >= 21.0.0',
    'six >= 1.12.0',
    'boto3 == 1.9.97'
]
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []
setup(
    name=NAME,
    version=VERSION,
    description="S3 handler for urllib",
    author='Carlo Bertini',
    author_email="waydotnet@gmail.com",
    url='https://github.com/WaYdotNET/urllib_s3',
    license='MIT License',
    keywords=["urllib", "s3", "urllib handler", 'minio', "aws", "boto3"],
    package_dir={'': 'lib'},
    install_requires=REQUIRES,
    packages=find_packages('lib'),
    long_description=long_description,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    setup_requires=pytest_runner,
    tests_require=[
        'pytest',
        'pytest-mock',
        'pytest-cov',
        'pytest-flake8',
        'pytest-isort',
        'pytest-runner'
    ],

)
