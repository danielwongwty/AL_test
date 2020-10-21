# `contact.core`

This module stores the abstract base classes of the whole program. Developers
should start the concrete implementation by inheriting the classes here.

-----

## `contact.core.BaseRecord`

Abstract class of a personal record.

### `BaseRecord.get_value()`

Given a field name, return the corresponding value.

### `BaseRecord.set_value()`

Assign the given value to the given field.

### `BaseRecord.all_fields()`

Return a collection of all the names the fields.

-----

## `contact.core.BaseContact`

Abstract class of a contact.

### `contact.core.BaseContact.all_fields()`

Return the names of all fields.

### `contact.core.BaseContact.create()`

Given the required data, add a new record into this contact.

### `contact.core.BaseContact.read()`

Return a collection of records satisfying the given search query.

### `contact.core.BaseContact.update()`

Update a collection of records satisfying the given search query with specified
values.

### `contact.core.BaseContact.delete()`

Remove a collection of records satisfying the given search query from this
contact.

-----

## `contact.core.BaseParser`

Abstract of a file parser.

### contact.core.BaseParser.write()`

Given a contact list and an output path, write the context as a file in the
specified output path.

### contact.core.BaseParser.read()`

Given a contact list and an output path, write the context as a file in the
specified output path.
