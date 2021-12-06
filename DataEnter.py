import json

import datetime



class JSONEditor:
    def __init__(self, jsonFilePath):

        """Constructor"""

        self.file = jsonFilePath

        with open(jsonFilePath, "r+") as fp:

            texts = fp.read()

            try:

                json.loads(texts)

            except json.decoder.JSONDecodeError:

                self.__clear_and_write({})

    def read(self) -> dict:

        """Read Datas of the json file."""

        with open(self.file, "r") as fp:

            try:

                return json.loads(fp.read())

            except json.decoder.JSONDecodeError:

                return {}

    def __clear_and_write(self, dictionary: dict):

        """Private method for other functionalities. If you are core developer change the source code and make it public but it can make it unusable"""

        with open(self.file, "w") as fp:

            fp.write(json.dumps(dictionary))

    def add_items(self, dictionary: dict):

        """Add key and value"""

        new_dict = self.read()

        for key, value in dictionary.items():

            new_dict[key] = value

        self.__clear_and_write(new_dict)

    def remove_items(self, keys: list):

        """Remove key and value"""

        newdict = self.read()

        for key in keys:

            newdict.pop(key)

        self.__clear_and_write(newdict)

    def set_value(self, key, value):

        """Set value of a key."""

        self.remove_items([key])

        self.add_items({key: value})

    def get_value(self, key):

        """Get value of a key."""

        return self.read()[key]

    def flush(self):

        """Empty the json database."""

        self.__clear_and_write({})


class DataEnterProcess:
    def __init__(self, data_enterer: dict):
        self.editor = JSONEditor("database.json")
        self.name = data_enterer["name"]
        self.time = datetime.datetime.now().strftime("%H:%M:%S")
        self.text = data_enterer["text"] if "text" in data_enterer.keys() else ""
        self.imgOrVdo = (
            data_enterer["imgOrVdo"] if "imgOrVdo" in data_enterer.keys() else None
        )

    def save(self):
        n = (
            int(list(self.editor.read().keys())[-1]) + 1
            if list(self.editor.read().keys()) != []
            else 1
        )
        self.editor.add_items(
            {
                n: {
                    "name": self.name,
                    "time": self.time,
                    "text": self.text,
                    "imgOrVdo": self.imgOrVdo,
                }
            }
        )
