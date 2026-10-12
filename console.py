#!/usr/bin/python3
"""This module defines the HBnB console (command interpreter)."""
import cmd
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

CLASSES = {
    'BaseModel': BaseModel, 'User': User, 'State': State,
    'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review
}


class HBnBCommand(cmd.Cmd):
    """HBnBCommand class - the AirBnB clone command interpreter."""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits the console on EOF signal."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Does nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates a new instance with optional key=value parameters."""
        if not arg:
            print("** class name missing **")
            return
        parts = arg.split()
        class_name = parts[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        kwargs = {}
        for param in parts[1:]:
            match = re.match(r'^(\w+)=(".*"|[0-9]+\.[0-9]+|-?[0-9]+)$', param)
            if not match:
                continue
            key, value = match.group(1), match.group(2)
            if value.startswith('"'):
                value = value[1:-1].replace('\\"', '"').replace('_', ' ')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue
            kwargs[key] = value
        obj = CLASSES[class_name](**kwargs)
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        parts = arg.split()
        if not parts:
            print("** class name missing **")
            return
        if parts[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(parts[0], parts[1])
        obj = models.storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        parts = arg.split()
        if not parts:
            print("** class name missing **")
            return
        if parts[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(parts[0], parts[1])
        obj = models.storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        models.storage.delete(obj)
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances."""
        if arg and arg not in CLASSES:
            print("** class doesn't exist **")
            return
        cls = CLASSES.get(arg) if arg else None
        objs = models.storage.all(cls)
        print([str(v) for v in objs.values()])

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute."""
        parts = arg.split()
        if not parts:
            print("** class name missing **")
            return
        if parts[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(parts[0], parts[1])
        obj = models.storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(parts) < 3:
            print("** attribute name missing **")
            return
        if len(parts) < 4:
            print("** value missing **")
            return
        setattr(obj, parts[2], parts[3].strip('"'))
        obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        cls = CLASSES.get(arg)
        if cls is None:
            print("** class doesn't exist **")
            return
        print(len(models.storage.all(cls)))

    def default(self, arg):
        """Handles <class>.<command>(<args>) syntax."""
        match = re.match(r'^(\w+)\.(\w+)\((.*)\)$', arg)
        if not match:
            print("*** Unknown syntax: {}".format(arg))
            return
        cls, cmd_name, args = match.group(1), match.group(2), match.group(3)
        dispatch = {
            'all': self.do_all, 'count': self.do_count,
            'show': self.do_show, 'destroy': self.do_destroy,
            'update': self.do_update
        }
        if cmd_name in dispatch:
            dispatch[cmd_name]("{} {}".format(cls, args).strip())
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBnBCommand().cmdloop()
