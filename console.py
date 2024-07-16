#!/usr/bin/python3
"""
console.py

This module contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Implementation of commands fo interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        print()
        return True

    def do_EOF(self, arg):
        print()
        return True
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

