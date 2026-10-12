#!/usr/bin/python3
"""This module defines the FileStorage class for JSON-based persistence."""
import json


class FileStorage:
    """FileStorage class that serializes/deserializes objects to/from JSON."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns dictionary of stored objects, optionally filtered by class."""
        if cls is None:
            return self.__objects
        cls_name = cls.__name__ if not isinstance(cls, str) else cls
        return {k: v for k, v in self.__objects.items()
                if type(v).__name__ == cls_name}

    def new(self, obj):
        """Adds obj to __objects with key <classname>.<id>."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        data = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'State': State,
            'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for obj_dict in data.values():
                cls_name = obj_dict.get('__class__')
                if cls_name in classes:
                    self.__objects[
                        "{}.{}".format(cls_name, obj_dict['id'])
                    ] = classes[cls_name](**obj_dict)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if present."""
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects.pop(key, None)

    def close(self):
        """Calls reload to deserialize JSON file."""
        self.reload()
