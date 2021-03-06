# pybook
![Build Status](https://travis-ci.org/bijanebrahimi/pybook.svg?branch=release)

python implementation of [Gitbook](https://github.com/gitbookio/gitbook). Currently PyBook only creates an **ODT** version of the book for now that can be viewed by libreoffice/openoffice. This could be easily then converted to a PDF version.

# Getting Started
For a starter, Clone [GitBook's Javascript Book](htpps://github.com/GitbookIO/javascript):

```
$ git clone git@github.com:GitbookIO/javascript.git gitbook-javascript
$ cd gitbook-javascript
$ pybook build --verbose
$ ls build/book.odt
```

Or you can start writing you own book from stratch:

```
$ mkdir pybook-example
$ cd pybook-example
$ pybook init --verbose
```

# Preview
Below is a preview of [Javascript Book](https://github/gitio/javascript): ![Book Preview](https://bijanebrahimi.github.io/pybook/images/javascript-odt-preview.png)

# Install
Using pip:

```
# pip install git+https://github.com/bijanebrahimi/pybook.git
```

Install manually:

```
$ git clone https://github.com/bijanebrahimi/pybook.git
$ cd pybook
# python setup install
```

# Getting help

```
$ pybook --help
```

# Book Design
## Format
A Book MUST contain at least a README and SUMMARY file and those are the only files PyBook currently supports:
- README.md: Introduction of the book
- SUMMARY.md: Chapters Structure
- LANGS.md: Multi-Languages book
- GLOSSAR.mdY: List of terms with descriptions

### README.md
According to wikipedia [Book Design](https://en.wikipedia.org/wiki/Book_design) this file contains an Introduction/Epigraph to the writing. the default

```
# Introduction

This is an Introduction to the book
```

### SUMMARY.md
PyBook uses a SUMMARY.md file to define the structure of chapters and subchapters of the book.

```
# Summary
- [An Introduction](intro.md)
    - [Who this book is for?](intro_who.md)
- [Getting Help](help.md)
[Appendix 1](appendix_1.md)
```

## Configuring Book
If there is a `book.json` at the root of your Book diectory, PyBook will uses it as a configuration file. A configuration file is used to change the Book's defaults.

```
{
    "title": "Book's Title",
    "author": "Author's Name",
    "description": "a short text to describe the writing",
    "language": "en",
    "direction": "ltr",
    "structure": {
       "readme": "README.md",
       "summary": "SUMMARY.md",
   },
   "variables": {
       "key": "value"
   }
}
```

## Templating
PyBook uses `jinja2` to render Book's chapters.

For more information please visit [GitBook Templating](http://help.gitbook.com/format/templating.html) and [Jinja2 Documentation](http://jinja.pocoo.org/).

# CHANGELOG
- **0.1.3**: Fixed creation of chapters at init
- **0.1.2**: removed python 2.6 support
- **0.1.1**: added python 2.7 support
- **0.1**: added odt renderer
