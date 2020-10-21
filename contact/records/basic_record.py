from ..core import BaseRecord


class BasicRecord(BaseRecord):
    """
    A very basic implementation of a personal record.
    """

    def __init__(self):
        self._name = None
        self._address = None
        self._phone_number = None

    def __repr__(self):
        return (f"{__name__}(" +
                f"'name'={repr(self.name)}, " +
                f"'address'={repr(self.address)}, " +
                f"'phone_number'={repr(self.phone_number)}" +
                ")")

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                all(self.get_value(k) == other.get_value(k)
                    for k in self.all_fields()))

    @classmethod
    def all_fields(cls):
        return ["name", "address", "phone_number"]

    def get_value(self, field):
        if field not in self.all_fields():
            raise RuntimeError("Unknown Field")
        return self.__getattribute__("get_" + field)()

    def set_value(self, field, value):
        if field not in self.all_fields():
            raise RuntimeError("Unknown Field")
        self.__getattribute__("set_" + field)(value)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    name = property(get_name, set_name)
    address = property(get_address, set_address)
    phone_number = property(get_phone_number, set_phone_number)
