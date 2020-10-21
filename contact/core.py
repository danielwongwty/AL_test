"""
This module defines the basic structure of data.
"""

from abc import ABC, abstractmethod


class BaseRecord(ABC):
    """
    Abstract of a personal record.
    """

    @abstractmethod
    def get_value(self):
        """
        Given a field name, return its value.
        """
        raise NotImplementedError

    @abstractmethod
    def set_value(self):
        """
        Set the given field with its given value.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def all_fields(cls):
        """
        Return the names of all fields.
        """
        raise NotImplementedError


class BaseContact(ABC):
    """
    Abstract of a contact.
    """

    @classmethod
    @abstractmethod
    def all_fields(cls):
        """
        Return the names of all fields.
        """
        raise NotImplementedError

    @abstractmethod
    def create(self):
        """
        Given the required data, add a new record into this contact.
        """
        raise NotImplementedError

    @abstractmethod
    def read(self):
        """
        Return a collection of records satisfying the given search query
        """
        raise NotImplementedError

    @abstractmethod
    def update(self):
        """
        Update a collection of records satisfying the given search query with
        specified values.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        """
        Remove a collection of records satisfying the given search query from
        this contact.
        """
        raise NotImplementedError


class BaseParser(ABC):
    """
    Abstract of a file parser.
    """

    @abstractmethod
    def write(self):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError
