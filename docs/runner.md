# `contact.runner`

Command Line Interface of doing different operations on contact list files.

call with `-h` in order to print all the arguments.

    $ python -m contact.runner -h
    usage: runner.py [-h] [-n [contact_list_type]] [-c key value]
                    [-r [key [query ...]]] [-uq key query] [-uv key value]
                    [-d [key [query ...]]]
                    file_path

    Command Line Interface of querying contact list

    positional arguments:
    file_path

    optional arguments:
    -h, --help            show this help message and exit
    -n [contact_list_type], --newfile [contact_list_type]
                            Create an empty contact list of specified type
    -c key value, --create key value
                            Add a new contact to existing contact list
    -r [key [query ...]], --read [key [query ...]]
                            Search for contacts from an existing contact list
    -uq key query, --update_query key query
                            Update the fields of the contacts satisfying the
                            search criteria. Should be used together with -uv
    -uv key value, --update_value key value
                            Update the fields with the values specified. Should be
                            used together with -uq
    -d [key [query ...]], --delete [key [query ...]]
                            Delete the contacts satisfying the given search
                            criteria
    $

We'll directly call the CLI to demonstrate how to use.

-----

## Create new contact list

To create a new contact list, use -n flag.

    $ python -m contact.runner -n BasicContact test_cli.yml

This will create an empty contact list. You need to specify the class of Contact
you would like to create (Any class in `contact.contacts`). The file extension
defines the file format to be used.

## Add record

To add record, use -c flag consecutively.

    $ python -m contact.runner -c name Daniel -c address Add -c phone_number 123 test_cli.yml
    $ python -m contact.runner -c name Ben -c address Add -c phone_number 456 test_cli.yml
    $ python -m contact.runner -c name Charles -c address AAA -c phone_number 12 test_cli.yml

## Read records

To read records, use -r flag with searching criteria.

    $ python -m contact.runner -r address Add  test_cli.yml
    ----------------------------------------
    address             : Add
    name                : Daniel
    phone_number        : 123
    ----------------------------------------
    address             : Add
    name                : Ben
    phone_number        : 456
    ----------------------------------------

To read all records, use -ra flag.

    $ python -m contact.runner -ra test_cli.yml
    ----------------------------------------
    address             : Add
    name                : Daniel
    phone_number        : 123
    ----------------------------------------
    address             : Add
    name                : Ben
    phone_number        : 456
    ----------------------------------------
    address             : AAA
    name                : Charles
    phone_number        : 12
    ----------------------------------------

## Update records

To update record, use -uq for specifying searching criteria and -uv for
defining the value.

    $ python -m contact.runner -uq address Add -uv address Loc test_cli.yml

## Delete records

To delete record, use -d flag and specify the search criteria.

    $ python -m contact.runner -d name Daniel test_cli.yml

To delete all records, use -da flag.

    $ python -m contact.runner -da test_cli.yml
