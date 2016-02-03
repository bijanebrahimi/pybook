import os
import logging
import argparse

from pybook.book.pybook import PyBook
from pybook.utils import logger


def pybook_init(root=None):
    if not root:
        root = os.getcwd()
    if not os.path.isabs(root):
        root = os.path.abspath(root)
    pybook = PyBook(root)
    pybook.read_config()
    pybook.init()

def main():
    parser = argparse.ArgumentParser(description='PyBook')

    command = parser.add_subparsers(dest="command")
    init_parser = command.add_parser('init')
    init_parser.add_argument('-r', '--root',
                             help='root directory')
    init_parser.add_argument('-v', '--verbose',
                             action='store_true',
                             help='Be verbose')

    build_parser = command.add_parser('build')
    build_parser.add_argument('-v', '--verbose',
                              action='store_true',
                              help='Be verbose')

    build_parser.add_argument('-b', '--build',
                             help='build directory')

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    if args.command == 'init':
        pybook_init(args.root)
