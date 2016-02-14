#!/usr/bin/env python
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='pybook',
      version='0.1.3',
      description='Book Creator Platform (python implementation og GitBook)',
      url='http://github.com/bijanebrahimi/pybook',
      author='Bijan Ebrahimi',
      author_email='bijanebrahimi@riseup.net',
      license='GPLv3',
      packages=['pybook'],
      install_requires=['argparse', 'secretary==0.3.5'],
      dependency_links = [
        'https://github.com/bijanebrahimi/secretary/tarball/master#egg=secretary-0.3.5'
      ],
      test_suite='tests',
      entry_points="""
      [console_scripts]
      pybook = pybook.cli:main
      """,
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      extras_require={
          'testing': ['pytest', 'setuptools']
      })
