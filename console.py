#!/usr/bin/python3
'''file that defines the console'''

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

classes = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
           'Place': Place, 'Review': Review, 'State': State, 'User': User}


class HBNBCommand(cmd.Cmd):
    '''Console Logic? jajaja XD'''

    prompt = '(hbnb) '

    """def __init__(self):
        '''init function'''
        cmd.Cmd.__init__(self)
        self.aliases = {'.all()': self.do_all,
                        '.count()': self.do_count}"""

    def emptyline(self):
        '''Empty line handeling'''
        return False

    def do_EOF(self, line):
        '''End of the file'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    """def default(self, line):
        '''default documentation'''
        cmd, arg, line = self.parseline(line)
        if arg in self.aliases:
            self.aliases[arg](cmd)
        else:
            print("*** Unknown syntax: {}".format(line))"""

    def do_create(self, arg):
        '''Create an instance of a class Ex: create "ClassName"'''
        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                new_instance = classes[arg]()
                print(new_instance.id)
                new_instance.save()
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
                    objects = storage.all()

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
                    objects = storage.all()

                    name = splitted[0] + '.' + splitted[1]
                    try:
                        objects.pop(name)
                        storage.save()
                    except:
                        print("** no instance found **")

    def do_all(self, arg):
        '''Display all instances of a class or all instances in total'''
        list = []
        splitted = arg.split()
        objects = storage.all()
        if len(arg) == 0:
            for k, v in objects.items():
                list.append(v.__str__())
            print(list)
        else:
            if not splitted[0] in classes:
                print("** class doesn't exist **")
            else:
                for k, v in objects.items():
                    class_name = v.__class__.__name__
                    if class_name == splitted[0]:
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
                    objects = storage.all()

                    name = splitted[0] + '.' + splitted[1]
                    if name not in objects:
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
                                if value.isnumeric():
                                    value = int(value)
                                elif "." in value:
                                    split_value = value.split(".")
                                    if (split_value[0].isnumeric() and
                                            split_value[1].isnumeric()):
                                        value = float(value)
                                elif type(value) == str:
                                    value = value[1:-1]

                                if attribute in instance:
                                    tipo = type(instance[attribute])
                                    casted = tipo(value)
                                    temp_dir = {attribute: casted}
                                    setattr(objects[name], attribute, casted)
                                    storage.save()
                                else:
                                    tipo = type(value)
                                    casted = tipo(value)
                                    temp_dir = {attribute: casted}
                                    setattr(objects[name], attribute, casted)
                                    storage.save()

    """def do_count(self, line):
        '''Count documentation '''
        objects = storage.all()
        pichu = 0
        for k, v in objects.items():
            class_name = v.__class__.__name__
            if class_name == line:
                pichu += 1
        print(pichu)"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
