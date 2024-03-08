#!/usr/bin/python3
"""defines a class for the HBNB console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Handles the HBNB command-line interface."""
    
    prompt="(hbnb)"

    def do_quit(self, arg):
        """ quite the console"""
        return True
    
    def do_EOF(self, arg):
        """Exit on End Of File."""
        print("")
        return True
    
    
    
    
    
    
if __name__ =="__main__":
    HBNBCommand().cmdloop()
    


