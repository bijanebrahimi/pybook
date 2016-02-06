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
    pybook.init()

def pybook_build(root=None, build='build'):
    if not root:
        root = os.getcwd()
    if not os.path.isabs(root):
        root = os.path.abspath(root)

    # TODO: check for specific renderer
    pybook = PyBook(root, build)
    pybook.build()

def main():
    parser = argparse.ArgumentParser(description='PyBook')

    command = parser.add_subparsers(dest="command")
    init_parser = command.add_parser('init')
    init_parser.add_argument('-r', '--root',
                             help='root directory')
    init_parser.add_argument('-v', '--verbose',
                             action='count',
                             help='Be verbose')

    build_parser = command.add_parser('build')
    build_parser.add_argument('-v', '--verbose',
                              action='count',
                              help='Be verbose')

    build_parser.add_argument('-b', '--build',
                             help='build directory')

    args = parser.parse_args()
    if args.verbose:
        verbosity_levels = [logging.INFO, logging.DEBUG]
        verbosity_level = args.verbose-1
        logging.basicConfig(level=verbosity_levels[verbosity_level])
        logger.setLevel(verbosity_levels[verbosity_level])

    if args.command == 'init':
        pybook_init(args.root)
    elif args.command == 'build':
        pybook_build(args.build)
