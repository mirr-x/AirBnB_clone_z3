#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import json
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import ast
from re import split
from sqlalchemy.exc import IntegrityError


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, content):
        """Exit the prompt."""
        return (True)

    def do_EOF(self, content):
        """Exit the prompt. using ctrl + d """
        return (True)

    def do_create(self, content):
        '''
        - Creates a new instance of class .

            - Usage => create [className]
        '''

        listx = split(" ", content)
        classe_nm = listx[0]
        ln = len(content)

        if ln == 0:
            print("** class name missing **")
        elif classe_nm not in self.classes:
            print("** class doesn't exist **")
        else:
            listx.remove(listx[0])

            dictx = self.args_to_dict(listx)

            try:
                instance = self.classes[classe_nm](**dictx)
                instance.save()
                print(instance.id)
            except IntegrityError as e:
                print(e)
                return


    def do_show(self, content):
        """
        - Display instance based on the class name and id .

            - Usage =>  show [className] [id]
        """

        ln = len(content)
        lis = content.split(" ")
        lis_ln = len(lis)

        if ln == 0:
            print("** class name missing **")
        elif lis[0] not in globals():
            print("** class doesn't exist **")
        elif lis_ln == 1:
            print("** instance id missing **")
        else:
            json_dict = storage.all().copy()
            key = "{:s}.{:s}".format(lis[0], lis[1])

            x = False
            for i in json_dict.keys():
                if i == key:
                    x = True
                    break

            if x == True:
                value = json_dict[key]
                full_format = "[{:s}] ({:s}) {:s}".format(lis[0], lis[1], str(value))
                print(full_format)
            else:
                print("** no instance found **")

    def do_destroy(self, content):
        '''
        - Deletes an instance based on the class name and id .

            - Usage => destroy [className] [id]
        '''

        lis = content.split(" ")
        ln = len(content)
        lis_ln = len(lis)
        bol = None

        if ln == 0:
            print("class name missing")
        elif lis[0] not in globals():
            print("** class doesn't exist **")
        elif lis_ln == 1:
            print("** instance id missing **")
        else:
            json_dict = storage.all()
            key_form = "{:s}.{:s}".format(lis[0], lis[1])

            for i in json_dict.keys():
                if key_form == i:
                    del json_dict[i]

                    with open("file.json", "w") as f:
                        json.dump(json_dict, f, indent=2)

                    bol = True
                    break
            if bol != True:
                print("** no instance found **")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        listx = []

        if args != "":
            args = split(' ', args)[0]  # remove possible trailing args
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            objects = storage.all(self.classes[args])
            for k, v in objects.items():
                listx.append(str(v))
        else:
            for k, v in storage.all().items():
                listx.append(str(v))
        print(listx)

    def do_update(self, content):
        '''
        - Updates an instance based on the class name and id by adding or updating attribute

            - Usage => update <class name> <id> <attribute name> "<attribute value>"
        '''

        lis = content.split(" ")
        ln = len(content)
        lis_ln = len(lis)

        not_allowed = ["id", "created_at", "updated_at"]
        bol = 0

        if lis_ln > 4:
            print("!! to many argument")
            return
        elif lis_ln < 4:
            print("!! less argument")
            return

        if ln == 0:
            print("** class name missing **")
        elif lis[0] not in globals():
            print("** class doesn't exist **")
        elif lis_ln == 1:
            print("** instance id missing **")
        elif self.id_checker(lis[1]) == 0:
            print("** no instance found **")
        elif lis_ln == 2:
            print("** attribute name missing **")
        elif lis_ln == 3:
            print("** value missing **")
        elif lis[2] not in not_allowed:  # !! update to searching on classe attrebuit not json file
            dic = storage.all()

            if lis[0] == User.__name__:  # ? User
                attrbutes = [x for x in User.__dict__ if not x.startswith('__')]
            elif lis[0] == BaseModel.__name__:  # ? BaseModel
                attrbutes = [x for x in BaseModel.__dict__ if not x.startswith('__')]
            elif lis[0] == State.__name__:  # ? State
                attrbutes = [x for x in State.__dict__ if not x.startswith('__')]
            elif lis[0] == City.__name__:  # ? City
                attrbutes = [x for x in City.__dict__ if not x.startswith('__')]
            elif lis[0] == Amenity.__name__:  # ? Amenity
                attrbutes = [x for x in Amenity.__dict__ if not x.startswith('__')]
            elif lis[0] == Place.__name__:  # ? Place
                attrbutes = [x for x in Place.__dict__ if not x.startswith('__')]
            elif lis[0] == Review.__name__:  # ? Place
                attrbutes = [x for x in Review.__dict__ if not x.startswith('__')]

            for x in dic.keys():
                if lis[1] == dic[x]["id"]:
                    user_dic = dic[x]
                    for x2 in attrbutes:

                        if lis[2] == x2:
                            #! castinggggggggg
                            if lis[3].isdigit():
                                user_dic[x2] = int(lis[3])
                            elif type(lis[3]) == str:
                                user_dic[x2] = str(lis[3])
                            elif type(lis[3]) == float:
                                user_dic[x2] = float(lis[3])
                            dic[x]["updated_at"] = datetime.now().isoformat()
                            bol = 1
                            break
                    if bol == 1:
                        break
            if bol == 1:
                with open("file.json", "w") as f:
                    json.dump(dic, f, indent=2)
            else:
                print("** no attribute found **")
        elif lis[2] in not_allowed:
            print("** You do not have the permesions to do this **")

    #! my methods------------------------
    ''' formating the string '''

    def formating(self, g):
        dic = g
        tm_fmt = "%Y-%m-%dT%H:%M:%S.%f"

        parsed_datetime1 = datetime.strptime(dic["created_at"], tm_fmt)
        parsed_datetime2 = datetime.strptime(dic["updated_at"], tm_fmt)

        dic["created_at"] = parsed_datetime1
        dic["updated_at"] = parsed_datetime2

        return (dic)

    def id_checker(self, id_z):
        base_data_json = storage.all().copy()

        for i in base_data_json.keys():
            chk_id = base_data_json[i]["id"]
            if chk_id == id_z:
                return (1)
        return (0)

    def time_to_obgect(self, time_z):

        # Convert the string to a datetime object
        dt_object = datetime.fromisoformat(time_z.replace('T', ' '))

        # Format the datetime object as a string
        formatted_date = repr(dt_object)

        # return the formatted string
        return (formatted_date)

    def full_format(self, dictnery):

        dic = dictnery

        # change create_at and update_at foramt to an opject
        z_create_at = self.time_to_obgect(dic["created_at"])
        z_update_at = self.time_to_obgect(dic["updated_at"])
        dic["created_at"] = z_create_at
        dic["updated_at"] = z_update_at

        # formating

        instance_class_name = dic["__class__"]
        instance_id = dic["id"]
        instance_key_dic = str(dic)
        full_format = "[{:s}] ({:s}) {:s}".format(instance_class_name, instance_id, instance_key_dic)

        return (full_format)

    def attrebute_checker(self, class_name):

        #!attrbute list
        if class_name == User.__name__:  # ? User
            attrbutes = [x for x in User.__dict__ if not x.startswith('__')]
        elif class_name == BaseModel.__name__:  # ? BaseModel
            attrbutes = [x for x in BaseModel.__dict__ if not x.startswith('__')]
        elif class_name == State.__name__:  # ? State
            attrbutes = [x for x in State.__dict__ if not x.startswith('__')]
        elif class_name == City.__name__:  # ? City
            attrbutes = [x for x in City.__dict__ if not x.startswith('__')]
        elif class_name == Amenity.__name__:  # ? Amenity
            attrbutes = [x for x in Amenity.__dict__ if not x.startswith('__')]
        elif class_name == Place.__name__:  # ? Place
            attrbutes = [x for x in Place.__dict__ if not x.startswith('__')]
        elif class_name == Review.__name__:  # ? Place
            attrbutes = [x for x in Review.__dict__ if not x.startswith('__')]
        #!attrbute list

        return (attrbutes)

    def args_to_dict(self, args):
        dict = {}
        for param in args:
            key_value = split("=", param)
            if len(key_value) == 2:
                dict[key_value[0]] = self.process_value(key_value[1])
        return dict

    def process_value(self, value):

        # Handle strings that start and end with double quotes
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]  # Remove the first and last characters
            value = value.replace('_', ' ')  # Replace underscores with spaces
            value = value.replace(r'\"', '"')  # Unescape any escaped double quotes
            return value

        # Handle floats (contains a dot)
        if '.' in value:
            try:
                return float(value)
            except ValueError:
                return None

        # Handle integers (default case)
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            try:
                return int(value)
            except ValueError:
                return None

        # Skip unrecognized input
        return None

    #! my methods------------------------

    #! Built-in methods in CMD-module----------------

    def emptyline(self):
        pass

    # todo
    def default(self, content):

        lis = content.split(".")
        if len(lis) >= 2:
            method = lis[1].split("(")
        else:
            print("*** Unknown syntax: {:s}".format(content))
        lis_len = len(lis)
        bol = 0

        if lis_len == 1:
            # print("*** Unknown syntax: {:s}".format(content))
            pass
        elif lis[1] == "all()":

            if lis[0] in globals():
                dic = storage.all().copy()
                instance_list = []

                for i in dic.keys():
                    if dic[i]["__class__"] == lis[0]:

                        full_format = self.full_format(dic[i])

                        instance_list += [full_format]
                        bol = 1

                if bol == 1:
                    print(instance_list)
                elif bol == 0:
                    print("*** class not found in json-file: {:s}".format(content))
            else:
                print("*** Unknown classe: {:s}".format(content))
        elif lis[1] == "count()":

            if lis[0] in globals():
                dic = storage.all().copy()
                counting = 0

                for x in dic.keys():
                    if dic[x]["__class__"] == lis[0]:
                        counting = counting + 1
                print(counting)

            else:
                print("*** Unknown classe: {:s}".format(content))
        elif method[0] == "show":

            if lis[0] in globals():
                dic = storage.all().copy()
                method_parameter = method[1].split(")")
                instance_id = method_parameter[0].replace('"', '')
                ruse_dic = None

                for x in dic.keys():
                    if dic[x]["id"] == instance_id and dic[x]["__class__"] == lis[0]:
                        ruse_dic = self.full_format(dic[x].copy())
                        bol = 1
                        break

                if bol == 1:
                    print(ruse_dic)
                elif bol == 0:
                    print("** no instance found **")
            else:
                print("*** Unknown classe: {:s}".format(content))
        elif method[0] == "destroy":

            if lis[0] in globals():
                dic = storage.all()
                method_parameter = method[1].split(")")
                instance_id = method_parameter[0].replace('"', '')

                for x in dic.keys():
                    if dic[x]["id"] == instance_id and dic[x]["__class__"] == lis[0]:
                        del dic[x]
                        bol = 1
                        break

                if bol == 1:
                    with open("file.json", "w") as f:
                        json.dump(dic, f, indent=2)

                elif bol == 0:
                    print("** no instance found **")
            else:
                print("*** Unknown classe: {:s}".format(content))
        elif method[0] == "update":

            if lis[0] in globals():
                dic = storage.all().copy()

                #!! if user updating multi elements
                # Todo
                if '{' in lis[1] and '}' in lis[1]:
                    # Todo zzzzzzzzzzzz

                    z_bool = False
                    cn = 0
                    zzz_id = ""
                    # ? get the id
                    for z in method[1]:
                        if z == "'" or z == '"':
                            if cn == 1:
                                break
                            z_bool = True
                            cn += 1
                        elif z_bool:
                            zzz_id += z
                    # ? get the id

                    str_z = lis[1]
                    v = ""

                    brace_found = False

                    for x in str_z:
                        if x == '}':
                            v += x
                            brace_found = False
                        if brace_found:
                            v += x
                        elif x == '{':
                            brace_found = True
                            v += x

                    dictionary = ast.literal_eval(v)

                    if type(dictionary) == dict:

                        #!attrbute list
                        attrbutes_z = self.attrebute_checker(lis[0])
                        #!attrbute list

                        for z in dictionary.keys():
                            if z not in attrbutes_z:
                                bol_z = 1
                                print("** invalid attrebute in dict")
                                return
                        vo_z = 0
                        for z in dic.keys():
                            if dic[z]["id"] == zzz_id and dic[z]["__class__"] == lis[0]:
                                for z_1 in dictionary.keys():
                                    dic[z][z_1] = dictionary[z_1]
                                    vo_z = 1
                            if vo_z == 1:
                                dic[z]["updated_at"] = datetime.now().isoformat()
                                break

                        with open("file.json", "w")as f:
                            json.dump(dic, f, indent=2)

                        return

            #!! if user updating just one element
                method_parameter = method[1].split(")")
                full_paramater = method_parameter[0].replace('"', '')
                param_lis1 = full_paramater.replace(" ", "")
                param_lis = param_lis1.split(",")

                not_allowed = ["id", "created_at", "updated_at"]
                if param_lis[1] not in not_allowed:

                    #!attrbute list
                    attrbutes = self.attrebute_checker(lis[0])
                    #!attrbute list

                    if param_lis[1] in attrbutes:
                        for x in dic.keys():
                            if dic[x]["id"] == param_lis[0] and dic[x]["__class__"] == lis[0]:

                                #! castinggggggggg
                                if param_lis[2].isdigit():
                                    dic[x][param_lis[1]] = int(param_lis[2])
                                elif type(param_lis[2]) == str:
                                    dic[x][param_lis[1]] = str(param_lis[2])
                                elif type(param_lis[2]) == float:
                                    dic[x][param_lis[1]] = float(param_lis[2])
                                dic[x]["updated_at"] = datetime.now().isoformat()
                                bol = 1
                                break
                        if bol == 1:
                            with open("file.json", "w")as f:
                                json.dump(dic, f, indent=2)
                        elif bol == 0:
                            print("** no instance found **")
                    else:
                        print("** no attribute found **")
                else:
                    print("** You do not have the permesions to do this **")
            else:
                print("*** Unknown classe: {:s}".format(content))
        else:
            print("*** Unknown syntax: {:s}".format(content))

    #! Built-in methods in CMD-module----------------
    #!!!!!!!!!!!!!!!
if __name__ == '__main__':
    HBNBCommand().cmdloop()
