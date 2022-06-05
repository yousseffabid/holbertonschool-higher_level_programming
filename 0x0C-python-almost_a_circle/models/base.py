#!/usr/bin/python3
"""Base Class"""
import json
import csv


class Base:
    """Base Class
    manage id attribute in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initiallize the object attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON serialization method
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON serialization to file method
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                my_list = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """JSON deserialization method
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an object
        """
        class_name = cls.__name__
        if class_name == 'Rectangle':
            c = cls(1, 1)
        elif class_name == 'Square':
            c = cls(1)
        c.update(**dictionary)
        return c

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json', 'r') as a_file:
                my_list = []
                s = cls.from_json_string(a_file.read())
                for i in s:
                    my_list.append(cls.create(**i))
                return my_list

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        my_list = []

        with open(cls.__name__ + '.csv', 'w') as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                my_list = [obj.to_dictionary() for obj in list_objs]
                fieldnames = my_list[0].keys()
                write_csv = csv.DictWriter(csv_file, fieldnames=fieldnames)
                write_csv.writeheader()
                write_csv.writerows(my_list)

    @classmethod
    def load_from_file_csv(cls):
        """CSV deserialization from file method
        """
        try:

            with open(cls.__name__ + '.csv', 'r') as csv_file:
                my_list = []
                reader_csv = csv.DictReader(csv_file)
                for element in reader_csv:
                    temp_d = {}
                    for k, v in dict(element).items():
                        temp_d[k] = int(v)
                    my_list.append(cls.create(**temp_d))
                return my_list

        except FileNotFoundError:
            return []
