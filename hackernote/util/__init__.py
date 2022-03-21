from hackernote import error


__all__ = []


def render(structure, destination=None):
    """
    Convert a hackernote structure into plain text

    [parameters]
    - structure: dict, hackernote structure. Each key represents a section title.
    The value of a key is the body of the section.
    The body is either a string (with newlines or none), or a list of strings
    - destination: str, the path to a file in which the rendered hackernote text can be saved.

    [exceptions]
    - hackernote.error.StructureError: raised if the structure isn't valid

    [return]
    Return the text
    """
    try:
        data = _render(structure)
    except Exception as e:
        raise error.StructureError from None
    if destination:
        with open(destination, "w") as file:
            file.write(data)
    return data


def get_key_value(line, sep=":", strip_whitespace=True):
    """
    Split a string into key and value parts.
    The string must have a separator defined as an argument.
    By default, the separator is ":".
    An example of a valid string is "name: John Doe ".
    The result will be: ("name": "John Doe")

    [parameters]
    - line: the string to split
    - sep: the separator, by default it is ":"
    - strip_whitespace: boolean to tell whether you want whitespace to be stripped out or not.
    By default, the value is True.

    [return]
    Always returns a tuple. If the key doesn't exist, it will be an empty string
    """

    cache = line.split(sep, maxsplit=1)
    if len(cache) == 2:
        key, value = cache
    else:
        key, value = "", cache[0]
    if strip_whitespace:
        return key.strip(), value.strip()
    return key, value


def _render(structure):
    text = []
    for header, body in structure.items():
        if header:
            header = "[{}]".format(header)
            text.append(header)
        if not isinstance(body, str):
            body = "\n".join(body)
        #if body:
        text.append(body)
    return "\n".join(text)
