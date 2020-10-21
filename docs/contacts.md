# `contact.contacts`

This package contains the concrete implementations of different types of
Contact.

-----

## `contact.core.BasicContact`

Implementation of a very basic Contact, storing `BasicRecord`.

### `contact.core.BasicContact.all_fields()`

Return the names of all fields.

### `contact.core.BasicContact.create(key_value_pairs)`

Given the required data, add a new record into this contact. Sample call:

    >>> contact = BasicContact()
    >>> contact.create({
    ...     "name": "AAA", "address": "Address", "phone_number": "12"
    ...     })

This creates a new record into the contact.

### `contact.core.BasicContact.read(queries)`

Return a collection of records satisfying the given search query `queries`.

Calling without argument will return all entries.

Sample call:

    >>> contact = BasicContact()
    >>> contact.create({"name": "Ass", "address": "Loc", "phone_number": "1"})
    >>> contact.create({"name": "BBB", "address": "Loc", "phone_number": "2"})
    >>> contact.create({"name": "AAA", "address": "Add", "phone_number": "12"})

    >>> contact.read({"name": "A*"})
    [contact.records.basic_record('name'='Ass', 'address'='Loc', 
    'phone_number'='1'), contact.records.basic_record('name'='AAA', 
    'address'='Add', 'phone_number'='12')]

A collection of search result is returned.

### `contact.core.BasicContact.update(queries, updates)`

Update a collection of records satisfying the given search query with specified
values.

    >>> contact = BasicContact()
    >>> contact.create({"name": "AAA", "address": "Add", "phone_number": "12"})
    >>> contact.create({"name": "Ass", "address": "Loc", "phone_number": "1"})
    >>> contact.create({"name": "BBB", "address": "Loc", "phone_number": "2"})
    >>> contact.update({"name": "A*"}, {"phone_number": "456"})

All records starting with "A" will have their `phone_number` attribute changed.

### `contact.core.BasicContact.delete(queries)`

Remove a collection of records satisfying the given search query `queries` from
this contact. Calling without the argument will remove all entries.
