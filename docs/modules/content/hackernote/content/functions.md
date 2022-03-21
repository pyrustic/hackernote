Back to [All Modules](https://github.com/pyrustic/hackernote/blob/master/docs/modules/README.md#readme)

# Module Overview

**hackernote**
 
This module exposes the API of this library

> **Classes:** &nbsp; None
>
> **Functions:** &nbsp; [get\_key\_value](#get_key_value) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [render](#render)
>
> **Constants:** &nbsp; None

# All Functions
[get\_key\_value](#get_key_value) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [render](#render)

## get\_key\_value
Split a string into key and value parts.
The string must have a separator defined as an argument.
By default, the separator is ":".
An example of a valid string is "name: John Doe ".
The result will be: ("name": "John Doe")




**Signature:** (line, sep=':', strip\_whitespace=True)

|Parameter|Description|
|---|---|
|line|the string to split|
|sep|the separator, by default it is ":"|
|strip\_whitespace|boolean to tell whether you want whitespace to be stripped out or not. By default, the value is True. |





**Return Value:** ["Always returns a tuple. If the key doesn't exist, it will be an empty string"]

[Back to Top](#module-overview)


## parse
Parse a text or the text in a file, return a hackernote structure




**Signature:** (source, compact=False)

|Parameter|Description|
|---|---|
|source|Source is either a text or a pathlib.Path object|
|compact|boolean to tell if whether you want empty lines to be stripped or not. By default, empty lines are kept. |





**Return Value:** ['Returns a hackernote structure. A hackernote structure is a dict.', 'Each key represents a section title.', 'The value of a key is the body of the section.', 'The body is a list of string, each string represents a line of text without the newline at end.']

[Back to Top](#module-overview)


## render
Convert a hackernote structure into plain text




**Signature:** (structure, destination=None)

|Parameter|Description|
|---|---|
|structure|dict, hackernote structure. Each key represents a section title. The value of a key is the body of the section. The body is either a string (with newlines or none), or a list of strings|
|destination|str, the path to a file in which the rendered hackernote text can be saved. |



|Exception|Description|
|---|---|
|hackernote.error.StructureError|raised if the structure isn't valid |



**Return Value:** ['Return the text']

[Back to Top](#module-overview)


