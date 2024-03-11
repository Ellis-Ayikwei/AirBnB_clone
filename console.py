#!/usr/bin/python3
"""defines a class for the HBNB console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from shlex import split
import re

def arg_splitter(arg):
    square_brackets = re.search(r"\[(.*?)\]", arg)
    curly_braces = re.search(r"\{(.*?)\}", arg)
    if curly_braces is None:
        if square_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            tokens = split(arg[:square_brackets.span()[0]])
            final_list = [i.strip(",") for i in tokens]
            final_list.append(square_brackets.group())
            return final_list
    else:
        tokens = split(arg[:curly_braces.span()[0]])
        final_list = [i.strip(",") for i in tokens]
        final_list.append(curly_braces.group())
        return final_list

class HBNBCommand(cmd.Cmd):
    """Handles the HBNB command-line interface."""
    
    prompt="(hbnb) "
    classes = ["BaseModel",
                "User"]

    def do_quit(self, arg):
        """ quite the console"""
        return True
    
    def do_EOF(self, arg):
        """Exit on End Of File."""
        print("")
        return True
    
    def do_create(self, arg):
        """
        Creates a new instance of the specified class, saves it to the JSON file, and prints its ID.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)
    
    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and
        id.

        Args:
            arg (_type_): _description_
            
        Example:
            show BaseModel 1234-1234-1234.
        """
        args = arg_splitter(arg)
        object_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(args[0], args[1])])
            
            
            
    def do_destroy(self, arg):
        """
        Deletes an instance based on the
        class name and id (save the change
        into the JSON file).

        Args:
            arg (any): the cmd arguments
            
        Example: destroy BaseModel 1234-1234-1234
        """
        args = arg_splitter(arg)
        object_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in object_dict:
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            del object_dict[key]
            storage.save()
            
            
    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        
        Args:
            arg (any): the cmd arguments
        
        Example:
            all BaseModel or $ all
        """
        
        arg = arg_splitter(arg)
    
        
        object_dict = storage.all().values()
        if len(arg) > 0 and arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objlist = []
            for obj in object_dict:
                if len(arg) > 0 and arg[0] in HBNBCommand.classes:
                    objlist.append(obj.__str__())
                elif len(arg) == 0:
                    objlist.append(obj.__str__())
            print(objlist)
    
    def do_update(self, arg):
        """
        Updates an instance based on the class and ID.

        Args:
            arg (str): The arguments provided in the command-line string.
        
        Example:
            update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg_splitter(arg)
        if len(args) < 4:
            print("Usage: update <class name> <id> <attribute name> '<attribute value>'")
            return False
        
        object_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        attribute_name = args[2]
        attribute_value = args[3]

        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False

        if len(args) == 1:
            print("** instance id missing **")
            return False
        for  k in object_dict.keys():
            print(k)
        if key not in object_dict.keys():
            print("** no instance found **")
            return False

        if len(args) == 2:
            print("** attribute name missing **")
            return False

        if len(args) == 3:
            print("** value missing **")
            return False
        try:
            if attribute_value.isdigit():
                attribute_value = int(attribute_value)
            elif float(attribute_value):
                attribute_value = float(attribute_value)
        except ValueError:
            pass
        class_attr = type(object_dict[key]).__dict__
        if attribute_name in class_attr.keys():
            try:
                attribute_value = type(class_attr[attribute_name])(attribute_value)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(object_dict[key], attribute_name, attribute_value)
        storage.save()



        
        
if __name__ =="__main__":
    HBNBCommand().cmdloop()
    


