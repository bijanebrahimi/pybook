import os
import re

from pybook.book.bookitem import Affix, Chapter
from pybook.utils import logger, BookError

def construct_bookitems(path, root=None):
    with open(path, 'r') as f:
        summary = f.read()
    items = parse_levels(summary.split('\n'),
                         current_level=0,
                         root=root)
    return items

def parse_levels(summary, root=None, current_level=0):
    # List of BookItem
    items = []
    while summary:
        line = summary[0]
        line_level = parse_level(line, spaces_in_tab=4)

        if line_level < current_level:
            break
        elif line_level > current_level:
            try:
                last_item = items.pop()
            except:
                raise Exception("There's Should be at least one Item since It's not Root")

            sub_items = parse_levels(summary, current_level=line_level, root=root)
            last_item.articles = sub_items
            items.append(last_item)
            continue
        else:
            #TODO: check for parse_line returned value
            item = parse_line(line, root=root)
            if item:
                items.append(item)
            summary.pop(0)
    return items

def parse_line(line, root=None):
    line = line.strip()
    chapter_regex = re.compile(" *[\*\-\+]? +\[(.*)\]\((.*)\)")
    affix_regex = re.compile(" *\[(.*)\]")

    if chapter_regex.match(line):
        title, path = re.match(" *[\*\-\+]? +\[(.*)\]\((.*)\)", line).groups()
        if line[0] in ['-', '*', '+']:
            return Chapter(title=title, path=path, root=root)
        else:
            logger.debug('Affix %s' % title)
            return Affix(title=title, path=path, root=root)
    elif affix_regex.match(line):
        # TODO: implement Affix
        pass
    else:
        logger.debug('Ignoring line: %s' % line)
    return None

def parse_level(line, spaces_in_tab=4):
    leading_spaces = len(line) - len(line.lstrip())
    if not leading_spaces % spaces_in_tab == 0:
        raise BookError("Indentation error")
    return leading_spaces / spaces_in_tab
