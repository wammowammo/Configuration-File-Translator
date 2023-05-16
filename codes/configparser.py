import json
import os
import re

# maximum file size (in bytes)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

#parse through Python config file and store in dictionary
def parse_config(config_file):
    # check if file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"The file {config_file} does not exist.")
    
    # check if file is readable
    if not os.access(config_file, os.R_OK):
        raise PermissionError(f"The file {config_file} is not readable.")
    
    # check if file name is valid
    if not re.match(r'^[\w\-. ]+$', config_file):
        raise ValueError(f"The file name {config_file} contains invalid characters.")
    
    # check if directory exists
    dirname = os.path.dirname(config_file)
    if dirname and not os.path.exists(dirname):
        raise FileNotFoundError(f"The directory {dirname} does not exist.")
    
    # check if file is too large
    if os.path.getsize(config_file) > MAX_FILE_SIZE:
        raise ValueError(f"The file {config_file} is too large. Maximum size is {MAX_FILE_SIZE} bytes.")

    config = {}
    with open(config_file, "r") as file:
        lines = file.readlines()
        
    # check if file is empty
    if not lines:
        raise ValueError(f"The file {config_file} is empty.")
        
    for line in lines:
        line = line.strip()  # remove leading/trailing white spaces

        # skip blank lines and commented lines
        if not line or line.startswith('#'):
            continue

        # split the line into key and value parts
        parts = line.split(" = ", 1)

        # check if line was correctly split into two parts
        if len(parts) != 2:
            raise ValueError(f"Invalid format in {config_file}. Each line" 
                             " should be 'key = value'.")
        
        key, value = parts

        # remove leading/trailing white spaces from key and value
        key = key.strip()
        value = value.strip()

        # check if key contains special characters
        if not key.isidentifier():
            raise ValueError(f"Invalid key '{key}' in {config_file}."
                             "Keys should be valid Python identifiers" 
                             "(alphanumeric characters and underscores).")

        try:
            config[key] = json.loads(value)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid value '{value}' for key '{key}' in "
                             f"{config_file}. Values should be valid JSON.")

    return config
