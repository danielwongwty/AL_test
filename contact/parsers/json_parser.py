import json
import importlib

from ..core import BaseParser


class JsonParser(BaseParser):

    def write(self, contact, file_path):
        data = {
            "module": f"{contact.__module__}",
            "class": f"{contact.__class__.__name__}",
            "entries": [
                {f: entry.get_value(f) for f in contact.all_fields()}
                for entry in contact.read()
            ]
        }
        with open(file_path, "w") as f:
            f.write(json.dumps(data, sort_keys=True, indent=4))

    def read(self, file_path):
        with open(file_path, "r") as f:
            data = json.load(f)

        mod = importlib.import_module(data["module"])
        contact = mod.__getattribute__(data["class"])()
        for entry in data["entries"]:
            contact.create(entry)

        return contact
