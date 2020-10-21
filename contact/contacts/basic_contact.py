import fnmatch

from ..records.basic_record import BasicRecord
from ..core import BaseContact


class BasicContact(BaseContact):
    """
    A very basic implementation of a contact list.
    """

    def __init__(self):
        self._entries = []

    def all_fields(self):
        return BasicRecord.all_fields()

    def create(self, key_value_pairs):
        """
        Create a new record given a `dict` of fields with their values.
        """

        # Check if all required fields are given
        if set(key_value_pairs) != set(self.all_fields()):
            raise RuntimeError("Incorrect arguments. You should provide the "
                               "following arguments: " +
                               repr(self.all_fields())
                               )
        record = BasicRecord()
        for k, v in key_value_pairs.items():
            record.set_value(k, v)
        self._entries.append(record)

    def read(self, queries=None):
        """
        Return a list of records satisfying the given `dict` of queries. If
        `None` is given to `queries`, return all records.
        """

        # Check if there is no recognizable field
        if (queries is not None and
                len(set(self.all_fields()) & set(queries)) == 0):
            raise RuntimeError("Incorrect arguments. You should provide the " +
                               "following arguments in `queries`: " +
                               repr(self.all_fields())
                               )

        if queries is None:
            return self._entries

        return [entry for entry in self._entries
                if all(fnmatch.fnmatch(entry.get_value(q), queries[q])
                       for q in set(self.all_fields()) & set(queries))
                ]

    def update(self, queries, updates):
        """
        Update a list of records satisfying the given `dict` of queries, with
        specified values defined in the given `dict` of updates.
        """

        # Check if there is no recognizable field
        if len(set(self.all_fields()) & set(queries)) == 0:
            raise RuntimeError("Incorrect arguments. You should provide the " +
                               "following arguments in `queries`: " +
                               repr(self.all_fields())
                               )

        for entry in self._entries:
            if all(fnmatch.fnmatch(entry.get_value(q), queries[q])
                    for q in set(self.all_fields()) & set(queries)):
                for u in set(self.all_fields()) & set(updates):
                    entry.set_value(u, updates[u])

    def delete(self, queries=None):
        """
        Remove a list of records satisfying the given search query from
        this contact. If `None` is given to `queries`, remove all records.
        """

        # Check if there is no recognizable field
        if (queries is not None and
                len(set(self.all_fields()) & set(queries)) == 0):
            raise RuntimeError("Incorrect arguments. You should provide the " +
                               "following arguments in `queries`: " +
                               repr(self.all_fields())
                               )

        keep = []
        if queries is not None:
            for entry in self._entries:
                if all(fnmatch.fnmatch(entry.get_value(q), queries[q])
                        for q in set(self.all_fields()) & set(queries)):
                    continue
                keep.append(entry)

        self._entries = keep
