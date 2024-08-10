#!/usr/bin/python3
"""
console.py

This module contains the entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Implementation of commands fo interpreter

    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        - Creates a new instance of BaseModel
        - Saves it (to the JSON file)
        - Prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if  class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.classes[class_name]()
        storage.save()
        print(instance.id)

    def do_show(self, arg):
        """
        - Prints the string representation of an instance.
        - Based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        - Deletes an instance.
        - Based on class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key ="{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        - Prints all string representation of all instances.
        - Based or not on the class name.
        """

        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in storage.all(self.classes[args[0]]).values()])

    def do_update(self, arg):
        """
        - Updates an instance based on the class name and id.
        - by adding or updating attribute.
        """

        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in  objects:
                print("** no instance found **")
                return
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                elif len(args) < 4:
                    print("** value missing **")
                    return
                else:
                    obj = objects[key]
                    attr_name = args[2]
                    attr_value = args[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)
                    obj.save()

    def do_count(self, arg):
        """ Method that retrieve the number of instances of a class """
        count = 0
        for obj in storage.all(self.classes[arg]).values():
            count += 1
        print(count)



    def default(self, arg):
        """ Overide default method """
        args = arg.split(".")
        if len(args) == 2:
            class_name = args[0]
            method_call = args[1]

        if method_call == "all()":
            self.do_all(class_name)

        if method_call == "count()":
            self.do_count(class_name)

        pass




















if __name__ == '__main__':
    HBNBCommand().cmdloop()

