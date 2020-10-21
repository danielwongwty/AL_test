import os
import argparse

from .parsers import JsonParser
from .parsers import YamlParser

from .contacts import *


def get_parser():
    """
    Parser for resolving command line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Command Line Interface of querying contact list"
        )

    parser.add_argument(
        '-n', "--newfile", metavar="contact_list_type",
        help="Create an empty contact list of specified type",
        dest="newfile", nargs="?",
        default=argparse.SUPPRESS
        )

    parser.add_argument(
        '-c', "--create", metavar=("key", "value"),
        help="Add a new contact to existing contact list",
        dest="create", action="append", nargs=2,
        default=argparse.SUPPRESS
        )

    parser.add_argument(
        '-r', "--read", metavar=("key", "query"),
        help="Search for contacts from an existing contact list",
        dest="read", action="append", nargs=2,
        default=argparse.SUPPRESS
        )

    parser.add_argument(
        '-ra', "--read_all",
        help="Show all records in the contact list",
        dest="read", action="store_const", const=None,
        default=argparse.SUPPRESS
        )

    parser.add_argument(
        '-uq', "--update_query", metavar=("key", "query"),
        help=("Update the fields of the contacts satisfying the search "
              "criteria. Should be used together with -uv "),
        dest="update_query", action="append", nargs=2,
        default=argparse.SUPPRESS
        )

    parser.add_argument(
        '-uv', "--update_value", metavar=("key", "value"),
        help=("Update the fields with the values specified. Should be used "
              "together with -uq"),
        dest="update_value", action="append", nargs=2,
        default=argparse.SUPPRESS
        )

    parser.add_argument(
        '-d', "--delete", metavar=("key", "query"),
        help="Delete the contacts satisfying the given search criteria",
        dest="delete", action="append", nargs=2,
        default=argparse.SUPPRESS
        )

    parser.add_argument(
        '-da', "--delete_all",
        help="Delete all records in the contact list",
        dest="delete", action="store_const", const=None,
        default=argparse.SUPPRESS
        )

    parser.add_argument("file_path")

    return parser


def parse_and_run(args):
    """
    Parse the argument and do related actions.
    """

    kwargs = vars(args)
    file_path = kwargs["file_path"]
    ext = os.path.splitext(file_path)[-1]
    if ext.lower() == ".json":
        parser = JsonParser()
    if ext.lower() == ".yml":
        parser = YamlParser()

    if "newfile" in kwargs:
        contact_list_type = kwargs["newfile"]
        contact = eval(f"{contact_list_type}()")
        parser.write(contact, file_path)

    elif "create" in kwargs:
        key_value_pairs = dict(kwargs["create"])
        contact = parser.read(file_path)
        contact.create(key_value_pairs)
        parser.write(contact, file_path)

    elif "read" in kwargs:
        queries = None if kwargs["read"] is None else dict(kwargs["read"])
        contact = parser.read(file_path)
        print("-" * 40)
        entries = contact.read(queries)
        for entry in entries:
            for k in sorted(entry.all_fields()):
                print(f"{k:<20}: {entry.get_value(k)}")
            print("-" * 40)

    elif "update_query" in kwargs and "update_value" in kwargs:
        queries = dict(kwargs["update_query"])
        updates = dict(kwargs["update_value"])
        contact = parser.read(file_path)
        contact.update(queries, updates)
        parser.write(contact, file_path)

    elif "delete" in kwargs:
        queries = None if kwargs["delete"] is None else dict(kwargs["delete"])
        contact = parser.read(file_path)
        contact.delete(queries)
        parser.write(contact, file_path)


if __name__ == "__main__":
    args = get_parser().parse_args()
    parse_and_run(args)
