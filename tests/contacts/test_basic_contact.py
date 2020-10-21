from contact.contacts import BasicContact
from contact.records import BasicRecord


class TestBasicContact:

    def test_create(self):
        contact = BasicContact()
        contact.create({
            "name": "AAA", "address": "Address", "phone_number": "12"
            })
        assert len(contact._entries) == 1
        assert isinstance(contact._entries[0], BasicRecord)
        assert contact._entries[0].get_name() == "AAA"
        assert contact._entries[0].get_address() == "Address"
        assert contact._entries[0].get_phone_number() == "12"

    def test_read(self):
        contact = BasicContact()
        contact.create({"name": "AAA", "address": "Add", "phone_number": "12"})
        contact.create({"name": "Ass", "address": "Loc", "phone_number": "1"})
        contact.create({"name": "BBB", "address": "Loc", "phone_number": "2"})

        assert contact.read({"name": "A*"}) == [
            contact._entries[0], contact._entries[1]]
        assert contact.read({"address": "?oc"}) == [
            contact._entries[1], contact._entries[2]]
        assert contact.read({"phone_number": "[12]"}) == [
            contact._entries[1], contact._entries[2]]

    def test_update(self):
        contact = BasicContact()
        contact.create({"name": "AAA", "address": "Add", "phone_number": "12"})
        contact.create({"name": "Ass", "address": "Loc", "phone_number": "1"})
        contact.create({"name": "BBB", "address": "Loc", "phone_number": "2"})

        contact.update({"name": "A*"}, {"phone_number": "456"})
        assert contact._entries[0].get_value("phone_number") == "456"
        assert contact._entries[1].get_value("phone_number") == "456"

    def test_delete(self):
        contact = BasicContact()
        contact.create({"name": "AAA", "address": "Add", "phone_number": "12"})
        contact.create({"name": "Ass", "address": "Loc", "phone_number": "1"})
        contact.create({"name": "BBB", "address": "Loc", "phone_number": "2"})

        contact.delete({"name": "Ass"})

        assert len(contact._entries) == 2
        assert contact._entries[0].get_name() == "AAA"
        assert contact._entries[1].get_name() == "BBB"
