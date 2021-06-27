#!/usr/bin/python3
'''file that defines the console'''

import cmd
import models

classes = {'BaseModel': models.base_model.BaseModel()}

class HBNBCommand(cmd.Cmd):
    '''Console Logic? jajaja XD'''

    prompt = '(hbnb) '

    def do_EOF(self, line):
        'End of the file'
        return True
    
    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def do_create(self, arg):
        '''Create the instance of a class'''
        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                new_instance = classes[arg]
                models.storage.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        '''Print a instance'''
        if len(arg) == 0:
            print('** class name missing **')

        splitted = arg.split()

        if len(splitted) != 2:
            print('** instance id missing **')
        else:
            try:
                '''new_instance = classes[arg]'''
                objects = models.storage.all()
        
                name = splitted[0] + '.' + splitted[1]
                try:
                    obj_show = objects[name]
                    print(obj_show)
                except:
                    print("** no instance found **")

            except:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
