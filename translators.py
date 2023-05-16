import json
import yaml
import configparser
import xml.etree.ElementTree as ET
import toml

#translate the config to php format
def translate_php(config):
    with open("config.php", "w") as file:
        file.write("<?php\n")
        file.write("$config = [\n")

        for key, value in config.items():
            if isinstance(value, str):
                php_value = f'"{value}"'
            elif isinstance(value, list):
                php_value = "array(" + ", ".join(f'"{item}"' for item in value) + ")"
            elif isinstance(value, dict):
                php_value = "array(" + ", ".join(f'"{item_key}" => "{item_value}"' for item_key, item_value in value.items()) + ")"
            else:
                php_value = value

            file.write(f"    '{key}' => {php_value},\n")

        file.write("];\n")
        file.write("?>\n")
        
    print("PHP config file has been written")  # Add this line

#translate the config to json format
def translate_json(config):
    with open("config.json", "w") as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
    print("JSON config file has been written")

#translate the config to yaml format
def translate_yaml(config):
    with open("config.yaml", "w") as file:
        yaml.dump(config, file)
    print("YAML config file has been written")

#translate the config to ini format
def translate_ini(config):
    cfg = configparser.ConfigParser()
    cfg.read_dict(config)

    with open("config.ini", "w") as file:
        cfg.write(file)
    
    print("INI config file has been written")

#translate the config to xml format
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
    config_xml = dict_to_xml('config', config)

    tree = ET.ElementTree(config_xml)
    with open("config.xml", "wb") as file:
        tree.write(file)
    
    print("XML config file has been written")

#translate the config to toml format
def translate_toml(config):
    with open("config.toml", "w") as file:
        toml.dump(config, file)
    
    print("TOML config file has been written")