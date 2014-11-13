#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.0'

__build__ = ''

setup(name='callingcard',
      version=__version__ + __build__,
      description='twilio voice call forwarding',
      author='Eric Siegel',
      author_email='siegel.eric@gmail.com',
      url='http://www.esiegel.com',
      packages=find_packages(exclude=['*.tests']),
      setup_requires=[
          'nose>=1.0',
      ],
      install_requires=[
          'Flask>=0.8',
      ],
      tests_require=[
      ],
      test_suite='callingcard.tests',
      entry_points={
          'console_scripts': [
              'development = callingcard.development:main',
          ]
      },
      include_package_data=True,
      )
