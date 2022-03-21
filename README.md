<!-- Intro Text -->
# Hackernote
<b> Reference library to parse and render hackernotes </b>
    
This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/hackernote/tags) . [Documentation](https://github.com/pyrustic/hackernote/tree/master/docs/modules#readme)

## Table of contents
- [Overview](#overview)
- [File extension](#file-extension)
- [Example](#example)
- [API](#api)
- [Relationship with INI file and TOML](relationship-with-ini-file-and-toml)
- [Related project](#related-project)
- [Installation](#installation)

# Overview
**Hackernote** is a Python package which is the reference library to parse and render `hackernotes`.

`Hackernote` is a file format for the [hacker](https://en.wikipedia.org/wiki/Hacker_culture) notes. A `hackernote` is a text with **sections**. Each section has a **title** and a **body**. The title of a section is written on a separate line between two [square brackets](https://en.wikipedia.org/wiki/Bracket#square_bracket). A text produced by a hacker without a section title is still a `hackernote` since the `null title` exists.

A `hackernote` is so easy to parse that I dropped the first regex-based iteration.

> **Fun fact:** The codebase documentation for [Pyrustic](https://pyrustic.github.io) projects is generated with a tool that parses **docstrings** expressly written in the **hackernote** format.

# File extension
You can proudly add the `.hkn` file extension to your `hackernotes`.

# Example
Here is the contents of a fictitious `example.hkn` file:

```
This section has a 'null title' since the title is missing.

[section_1]
A title is a string surrounded with square brackets.
Do not put spaces in the title.

[todo-list]
item_1: 1
item_2: 2
# The library offers the 'get_key_value' function to split 
# a line into key-value parts.
# Am I writting comments ?
# If you think that this is a comment... so ok, this is a comment...
...
Hey, stop thinking about TOML or INI file, only two things matter here:
- a section title
- a section body

[section_1]
No exception will be raised. This is not a duplicate section.
This is simply a continuation of [section_1] (yes I can write it here !)

[]
This is the second time you've come across an empty title section in this hackernote.

[empty-body-section]
```

# API
Three functions are exposed by the **Hackernote** library:
- **parse:** This function takes as input a filename or a string and returns the `hackernote structure`. The hackernote structure is a dictionary. A key is a section title and the value is a list of strings that make up the body of the section. Each string represents a line. The order of the keys is the same as in the original hackernote.
- **render:** This function takes as input a `hackernote structure` and optionally a destination filename. The hackernote structure is then rendered, i.e. a text is output (optionally saved to a file).
- **get_key_value:** This function takes a string as input and then divides it into key and value parts. You can set the separator character. By default, the separator is `:`.

```python
import hackernote


# parse the content of the source file
SOURCE = "/path/to/note.hkn"
structure = hackernote.parse(SOURCE, compact=True)

# iterate over the hackernote structure
for title, body in structure.items():
    print("Section title: {}".format(title))
    print("Body: ")
    # body is a list of strings (lines)
    str_body = "\n".join(body)
    print(str_body)
    print()

# convert the structure into a compact plain text,
# then save the result in the destination file
DESTINATION = "/path/to/compact_note.hkn"
text = hackernote.render(structure, destination=DESTINATION)

# print the compact version of the content of the source file,
print(text)

```


# Relationship with INI file and TOML
Excerpt from the Wikipedia page of the [INI file](https://en.wikipedia.org/wiki/INI_file#History):

> The primary mechanism of software configuration in Windows was originally a text file format that comprised text lines with one key–value pair per line, organized into sections. This format was used for operating system components, such as device drivers, fonts, startup launchers. INI files were also generally used by applications to store individual settings.

Excerpt from the Wikipedia page of [TOML](https://en.wikipedia.org/wiki/TOML#Syntax):

> TOML's syntax primarily consists of key = "value" pairs, [section names], and # comments. TOML's syntax somewhat resembles that of .INI files, but it includes a formal specification, whereas the INI file format suffers from many competing variants.
>
> Its specification includes a list of supported data types: String, Integer, Float, Boolean, Datetime, Array, and Table. 

`Hackernote` shares with the **INI file** and **TOML** the square brackets and the concept of `section`. **And that's all**.

Also, `Hackernote` is topic agnostic. You can use it to save [Hacker News](https://news.ycombinator.com/) links, use it to save code snippets, or use it as a configuration file (like I did with [Backstage](https://github.com/pyrustic/backstage)). You can even decide to use it as a docstring format ([modules documentation](https://github.com/pyrustic/hackernote/tree/master/docs/modules#readme) are generated from these docstrings). Only you can decide what a comment is, what should be considered key-value, what should be treated as float, boolean, text, etc.

`Hackernote` solves [this](https://github.com/toml-lang/toml/issues/613) (**TOML**) and [this](https://stackoverflow.com/questions/335695/lists-in-configparser) (**INI file**) out of the box !

# Related project
**Backstage** is a **language-agnostic** command-line tool that allows the developer to define, coordinate and use the various resources at his disposal to create and manage a software project.

**Backstage** makes extensive use of **Hackernote**.

> **Discover [Backstage](https://github.com/pyrustic/backstage) !**


# Installation
**Hackernote** is **cross platform** and versions under **1.0.0** will be considered **Beta** at best. It is built on [Ubuntu](https://ubuntu.com/download/desktop) with [Python 3.8](https://www.python.org/downloads/) and should work on **Python 3.5** or **newer**.

## For the first time

```bash
$ pip install hackernote
```

## Upgrade
```bash
$ pip install hackernote --upgrade --upgrade-strategy eager

```

<br>
<br>
<br>

[Back to top](#readme)
