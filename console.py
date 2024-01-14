#!/usr/bin/python3
<<<<<<< HEAD
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] is '{' and pline[-1] is'}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] is '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] is not ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] is '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
=======
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
>>>>>>> ddde616431886a41d6fa8a4c70a4b6214b4015a3
