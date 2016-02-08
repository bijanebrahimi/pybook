#!/usr/bin/env python
from setuptools import setup

setup(name='pybook',
      version='0.1',
      description='Book Creator Platform (python implementation og GitBook)',
      url='http://github.com/bijanebrahimi/pybook',
      author='Bijan Ebrahimi',
      author_email='bijanebrahimi@riseup.net',
      license='GPLv3',
      packages=['pybook'],
      install_requires=['argparse', 'secretary'],
      entry_points="""
      [console_scripts]
      pybook = pybook.cli:main
      """,
      zip_safe=False)
