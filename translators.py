import json
import yaml

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

def translate_json(config):
    with open("config.json", "w") as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
    print("JSON config file has been written")

def translate_yaml(config):
    with open("config.yaml", "w") as file:
        yaml.dump(config, file)
    print("YAML config file has been written")