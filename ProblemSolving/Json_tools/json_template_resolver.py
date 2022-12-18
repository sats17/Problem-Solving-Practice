import json
import re
import os
import collections.abc
class JsonTemplateResolver:
    # -----------------------------------------------------------------------
    def __init__(self, path, values_dict):
        if not self.__is_dict(values_dict):
            raise ValueError("Provided Values are not Dict")
        self.values_dict = values_dict
        self.__load_template(path)
        self.__var_regex = re.compile("\{\{\ [a-zA-Z0-9_]+\ \}\}")
        self.__arr_regex = re.compile("\{\%\ [a-zA-Z0-9_]+\ \%\}")
        self.__cln_regex = re.compile("[a-zA-Z0-9_]+")
    def __is_dict(self, obj):
        return isinstance(obj, collections.abc.Mapping)
    def __is_iterable(self, obj):
        try:
            iter(obj)
            return True
        except:
            return False
    def __load_template(self, file_path):
        if os.path.isfile(file_path) and file_path.lower().endswith("json"):
            try:
                with open(file_path) as json_in:
                    self.__template = json.load(json_in)
            except Exception as ex:
                print(ex)
                raise ValueError("Unable to parse json! {}".format(ex))
        else:
            raise ValueError("{} is not JSON file".format(file_path))
    def generate(self):
        try:
            result = self.__scan_json_nodes(dict(self.__template), self.values_dict)
        except Exception as ex:
            print(ex)
            raise ValueError("Error occurred while generating template")
        return result
    def __scan_json_nodes(self, nodes, replace_dict):
        if isinstance(nodes, dict):
            for key, value in nodes.items():
                if isinstance(value, dict):
                    self.__scan_json_nodes(value, replace_dict)
                elif isinstance(value, list):
                    self.__scan_json_nodes(value, replace_dict)
                else:
                    nodes[key] = self.__evaluate_value(value, replace_dict)
        elif isinstance(nodes, list):
            for index in range(0, len(nodes)):
                value = nodes[index]
                if isinstance(value, dict):
                    self.__scan_json_nodes(value, replace_dict)
                elif isinstance(value, list):
                    self.__scan_json_nodes(value, replace_dict)
                else:
                    nodes[index] = self.__evaluate_value(value, replace_dict)
        return nodes
    def __evaluate_value(self, value, replace_dict):
        if self.__var_regex.search(str(value)):
            for key in replace_dict.keys():
                updated_key = "{{ " + key + " }}"
                value = re.sub(updated_key, replace_dict[key], value)
        return value


if __name__ == "__main__":
    resolver = JsonTemplateResolver("test_json.json",
                                    {"update_me_1": "resolved first", "update_me_2": "resolved second"})
    result = resolver.generate()
    print(type(result))
    json_str = json.dumps(result, indent=4)
    print(type(json_str))
    print(json_str)
