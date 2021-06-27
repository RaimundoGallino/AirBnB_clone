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
        '''Print a instance of a class'''
        splitted = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
        else:
            if not splitted[0] in classes:
                print("** class doesn't exist **")
            else:
                if len(splitted) == 1:
                    print('** instance id missing **')
                else:
                    '''new_instance = classes[arg]'''
                    objects = models.storage.all()
        
                    name = splitted[0] + '.' + splitted[1]
                    try:
                        obj_show = objects[name]
                        print(obj_show)
                    except:
                        print("** no instance found **")


    def do_destroy(self, arg):
        '''Destroy an Instance of a class'''
        splitted = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
        else:
            if not splitted[0] in classes:
                print("** class doesn't exist **")
            else:
                if len(splitted) == 1:
                    print('** instance id missing **')
                else:
                    '''new_instance = classes[arg]'''
                    objects = models.storage.all()
        
                    name = splitted[0] + '.' + splitted[1]
                    try:
                        objects.pop(name)
                        models.storage.save()
                    except:
                        print("** no instance found **")

    def do_all(self, arg):
        '''Display all instances of a class or all instances in total'''
        list = []
        splitted = arg.split()
        objects = models.storage.all()
        if len(arg) == 0:
            for k,v in objects.items():
                list.append(v.__str__())
            print(list)
        else:
            if not splitted[0] in classes:
                print("** class doesn't exist **")
            else:
                for k,v in objects.items():
                    if v["__class__"] == splitted[0]:
                        list.append(v.__str__())
                print(list)

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
