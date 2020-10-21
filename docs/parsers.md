# `contact.parsers`

This package contains the concrete implementations of different types of file
reader and writer.

-----

## `contact.parsers.JsonParser`

For reading and writing .json format.

### `contact.parsers.JsonParser.write(contact, file_path)`

Given a contact list and an output path, write the context as a .json file in
the specified output path.

### `contact.parsers.JsonParser.read(file_path)`

Given the file_path, read the content and return as a `Contact` object.

-----

## `contact.parsers.YamlParser`

For reading and writing .yml format.

### `contact.parsers.YamlParser.write(contact, file_path)`

Given a contact list and an output path, write the context as a .yml file in
the specified output path.

### `contact.parsers.YamlParser.read(file_path)`

Given the file_path, read the content and return as a `Contact` object.
