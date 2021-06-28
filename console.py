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

    def do_update(self, arg):
        '''Update an instance of a Class'''
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
                    if not name in objects:
                        print("** no instance found **")
                    else:
                        if len(splitted) == 2:
                            print("** attribute name missing **")
                        else:
                            if len(splitted) == 3:
                                print("** value missing **")
                            else:
                                instance = objects[name].__dict__
                                attribute = splitted[2]
                                value = splitted[3]
                                if type(value) == str:
                                    value = value[1:-1]
                                print(value)

                                if attribute in instance:
                                    tipo = type(instance[attribute])
                                    print(tipo)
                                    casted = tipo(value)
                                    temp_dir = {attribute: casted}
                                    setattr(objects[name], attribute, value)
                                else:
                                    tipo = type(value)
                                    casted = tipo(value)
                                    temp_dir = {attribute: casted}
                                    setattr(objects[name], attribute, value)
                                    print(objects[name])

if __name__ == '__main__':
    HBNBCommand().cmdloop()