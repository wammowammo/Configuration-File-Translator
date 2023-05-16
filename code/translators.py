import json
import yaml
import configparser
import xml.etree.ElementTree as ET
import toml
import shlex

# handling different data types for php
def php_value_repr(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, (int, float)):
        return str(value)
    # elif isinstance(value, str):
    #     return f'"{value.replace(\'"\', \'\"\')}"'
    elif isinstance(value, list):
        return "array(" + ", ".join(php_value_repr(item) for item in value) + ")"
    elif isinstance(value, dict):
        return "array(" + ", ".join(f'"{key}" => {php_value_repr(val)}' for key, val in value.items()) + ")"
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")

# translate the config to php format
def translate_php(config):
    try:
        with open("config.php", "w") as file:
            file.write("<?php\n")
            file.write("$config = [\n")

            for key, value in config.items():
                php_value = php_value_repr(value)
                file.write(f"    '{key}' => {php_value},\n")

            file.write("];\n")
            file.write("?>\n")

            print("PHP config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to PHP file")

# translate the config to json format
def translate_json(config):
    try:
        with open("config.json", "w") as file:
            json.dump(config, file, ensure_ascii=False, indent=4)
        print("JSON config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to JSON file")

# translate the config to yaml format
def translate_yaml(config):
    try:
        with open("config.yaml", "w") as file:
            yaml.dump(config, file)
        print("YAML config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to YAML file")

# translate the config to ini format
def translate_ini(config):
    try:
        cfg = configparser.ConfigParser()
        cfg.read_dict(config)

        with open("config.ini", "w") as file:
            cfg.write(file)
        
        print("INI config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to INI file")

# translate the config to xml format
def dict_to_xml(tag, d):
    '''
    Convert a dictionary to an XML Element.
    '''
    element = ET.Element(tag)
    for key, val in d.items():
        child = ET.Element(key)
        child.text = str(val)
        element.append(child)
    return element

def translate_xml(config):
    try:
        config_xml = dict_to_xml('config', config)

        tree = ET.ElementTree(config_xml)
        with open("config.xml", "wb") as file:
            tree.write(file)
        
        print("XML config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to XML file")

# translate the config to toml format
def translate_toml(config):
    try:
        with open("config.toml", "w") as file:
            toml.dump(config, file)
        
        print("TOML config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to TOML file")

# check for reserved words in bash and perl
def is_reserved_word(word, reserved_words):
    return word in reserved_words

bash_reserved_words = {"if", "then", "else", "elif", "fi", "case", "esac", "for", "select", "while", "until", "do", "done", "in", "function", "time"}
perl_reserved_words = {"if", "else", "elsif", "unless", "while", "until", "for", "foreach", "continue", "do", "goto", "next", "last", "redo", "return", "package", "require", "use"}


# translate the config to bash format
def translate_bash(config):
    try:
        with open("config.sh", "w") as file:
            for key, value in config.items():
                file.write(f"export {key}={shlex.quote(str(value))}\n")
        print("Bash config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to BASH file")

# translate the config to perl format
def translate_perl(config):
    try:
        with open("config.pl", "w") as file:
            file.write("%config = (\n")
            for key, value in config.items():
                file.write(f"    {key} => {value},\n")
            file.write(");\n")
        print("Perl config file has been written")
    except PermissionError:
        print("Permission denied when trying to write to BASH file")
