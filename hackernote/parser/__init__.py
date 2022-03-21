import os.path
import pathlib


__all__ = []


def parse(source, compact=False):
    """
    Parse a text or the text in a file, return a hackernote structure

    [parameters]
    - source: Source is either a text or a pathlib.Path object
    - compact: boolean to tell if whether you want empty lines to be stripped or not.
    By default, empty lines are kept.

    [return]
    Returns a hackernote structure. A hackernote structure is a dict.
    Each key represents a section title.
    The value of a key is the body of the section.
    The body is a list of string, each string represents a line of text without the newline at end.
    """
    """Source is either a text or a pathlib.Path object.
    Set compact to True to remove empty lines"""
    parser = Parser(compact=compact)
    if isinstance(source, pathlib.Path):
        filename = source.resolve()
        if not os.path.isfile(filename):
            return dict()
        with open(filename, "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.rstrip("\n")
                parser.feed(line)
    else:
        if isinstance(source, str):
            source = source.split("\n")
        parser = Parser(compact=compact)
        for line in source:
            parser.feed(line)
    return parser.get_structure()


class Parser:
    def __init__(self, compact=False):
        self._compact = compact
        self._structure = dict()
        self._header = ""
        self._body = None
        self._active = True

    def feed(self, line):
        if not self._active:
            return
        if self._compact and (not line or line.isspace()):
            return
        if line.startswith("[") and line.endswith("]") and " " not in line:
            line = line.strip("[]")
            # clean up
            self._cleanup()
            self._body = None
            # update
            self._header = line
        else:
            if self._body is None:
                self._body = list()
            self._body.append(line)

    def get_structure(self):
        if self._active:
            self._cleanup()
            if not self._structure[""]:
                del self._structure[""]
            self._active = False
        return self._structure

    def _cleanup(self):
        if self._header is not None:
            if self._header not in self._structure:
                self._structure[self._header] = list()
            if self._body is not None:
                self._structure[self._header].extend(self._body)
