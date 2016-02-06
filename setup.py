#!/usr/bin/env python
from setuptools import setup

setup(name='pybook',
      version='0.1',
      description='Book Creator Platform (python implementation)',
      url='http://github.com/bijanebrahimi/pypython',
      author='Bijan Ebrahimi',
      author_email='bijanebrahimi@riseup.net',
      license='GPLv3',
      packages=['pybook'],
      install_requires=['argparse'],
      entry_points="""
      [console_scripts]
      pybook = pybook.cli:main
      """,
      zip_safe=False)
