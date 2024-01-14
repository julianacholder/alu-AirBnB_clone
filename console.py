#!/usr/bin/python3
"""
console
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import cmd
from models.city import City
from models.place import Place
import re
from models.review import Review
from models.state import State
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Main class
    """
    prompt = "(hbnb) "

    classes = {"Amenity": Amenity, "BaseModel": BaseModel,
               "City": City, "Place": Place, "Review": Review,
               "State": State, "User": User}

    def _formatter(self, args):
        """
        format the args
        """
        if "." in args:
            my_dict = re.findall(r'\{.*?\}', args)
            quotted = re.findall(r'"([^"]*)"', args)
            if my_dict:
                iD = re.findall(r'"([^"]*)"', args)[0]
                args = args.split('.')
                cls = args[0]
                func = args[1].split('(')[0]
                my_dict = (my_dict[0])
                res = [func, cls, iD, my_dict]
                return " ".join(res)
            elif len(quotted) == 0:
                args = args.split('.')
                cls = args[0]
                func = args[1].split('(')[0]
                return " ".join([func, cls])
            elif len(quotted) == 1:
                iD = re.findall(r'"([^"]*)"', args)[0]
                args = args.split('.')
                cls = args[0]
                func = args[1].split('(')[0]
                return " ".join([func, cls, iD])
            else:
                res = []
                double_quotted = re.findall(r'"([^"]*)"', args)
                number = re.search(r'(?<!\S)(\d+)\b', args)
                values = {"id": None, "attr_name": None, "attr_value": None}
                for i in range(len(double_quotted)):
                    values[list(values.keys())[i]] = double_quotted[i]
                if number is None:
                    values["attr_value"] = '"' + values.get("attr_value") + '"'
                else:
                    values["attr_value"] = number.group(0)
                to_del = []
                for k, v in values.items():
                    if v is None:
                        to_del.append(k)
                for ele in to_del:
                    del values[ele]
                args = args.split('.')
                cls = args[0]
                res.append(args[1].split('(')[0])
                res.append(cls)
                for v in values.values():
                    res.append(v)
                return " ".join(res)
        else:
            return args

    def do_quit(self, args):
        """
        exiting the console
        """
        return True

    def emptyline(self):
        """
        do nothing
        """
        pass

    def do_EOF(self, args):
        """
        keyboard interruption
        """
        return True

    def precmd(self, args):
        """
        preprocess the arg
        """
        return (self._formatter(args))

    def do_create(self, args):
        """
        create and save a new object
        ex: create BaseModel
        """
        if len(args) < 1:
            print("** class name missing **")
        else:
            cls = HBNBCommand.classes.get(args)
            if cls is None:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        """
        show the dict representation of an object
        ex: show BaseModel 12345
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, args):
        """
        delete and object
        based on its class and id
        ex: destroy BaseModel 1234567
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """
        show all objects in storage or all objects of a certain class
        ex: all
        or
        ex: all BaseModel
a        """
        res = []
        args = args.split()
        if len(args) < 1:
            for k, v in storage.all().items():
                res.append(str(v))
            print(res)
        else:
            cls = args[0]
            if cls not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if k.startswith(cls):
                        res.append(str(v))
                print(res)

    def do_update(self, arg):
        """
        update an object by add or updating an attribute
        ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        floats = ['longitude', 'latitude']
        args = arg.split()
        try:
            cls = args[0]
            if cls not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        except Exception:
            print("** class name missing **")
            return
        try:
            iD = args[1]
            key = cls + "." + iD.strip('"')
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
                return
        except Exception:
            print("** instance id missing **")
            return
        try:
            my_dict = re.findall(r'\{.*?\}', arg)
            if len(my_dict) != 0:
                if isinstance(eval(my_dict[0]), dict):
                    for k, v in eval(my_dict[0]).items():
                        setattr(obj, k, v)
                    return
            else:
                attr_name = args[2]
        except Exception as e:
            print("** attribute name missing **")
            return
        try:
            value = args[3]
            if '"' in value:
                value = value.strip('"')
            else:
                value = int(value) if attr_name not in floats else float(value)
        except Exception:
            print("** value missing **")
            return
        setattr(obj, attr_name, value)
        obj.save()

    def do_count(self, args):
        """
        return the number of instance of a class
        """
        count = 0
        cls = HBNBCommand.classes.get(args)
        if cls is None:
            print("** class doesn't exist **")
        else:
            for obj in storage.all():
                if obj.startswith(cls.__name__):
                    count += 1
            print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
