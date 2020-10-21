import os

from contact.contacts import BasicContact
from contact.parsers import YamlParser


class TestYamlParser:

    def test_yaml(self):
        contact = BasicContact()
        contact.create({"name": "AAA", "address": "Add", "phone_number": "12"})
        contact.create({"name": "Ass", "address": "Loc", "phone_number": "1"})
        contact.create({"name": "BBB", "address": "Loc", "phone_number": "2"})
        output_path = os.path.join(os.getcwd(), "test_out.yml")

        YamlParser().write(contact, output_path)
        contact_ = YamlParser().read(output_path)

        assert contact.__class__ == contact_.__class__
        assert contact.read() == contact_.read()
