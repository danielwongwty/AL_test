from contact.records.basic_record import BasicRecord


class TestBasicRecord:

    def test_all_fields(self):
        assert (sorted(BasicRecord.all_fields()) ==
                ["address", "name", "phone_number"])

    def test_set_name(self):
        record = BasicRecord()
        record.set_name("Dan")
        assert record._name == "Dan"

    def test_set_address(self):
        record = BasicRecord()
        record.set_address("Address")
        assert record._address == "Address"

    def test_set_phone_number(self):
        record = BasicRecord()
        record.set_phone_number("123")
        assert record._phone_number == "123"

    def test_get_name(self):
        record = BasicRecord()
        record._name = "Dan"
        assert record.get_name() == "Dan"

    def test_get_address(self):
        record = BasicRecord()
        record._address = "Address"
        assert record.get_address() == "Address"

    def test_get_phone_number(self):
        record = BasicRecord()
        record._phone_number = "123"
        assert record.get_phone_number() == "123"

    def test_set_value(self):
        record = BasicRecord()
        record.set_value("name", "BBB")
        assert record._name == "BBB"
        record.set_value("address", "Location")
        assert record._address == "Location"
        record.set_value("phone_number", "456")
        assert record._phone_number == "456"

    def test_get_value(self):
        record = BasicRecord()
        record._name = "BBB"
        record._address = "Location"
        record._phone_number = "456"
        assert record.get_value("name") == "BBB"
        assert record.get_value("address") == "Location"
        assert record.get_value("phone_number") == "456"
