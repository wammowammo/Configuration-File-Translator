import json

#parse thru config file and store in dictionary
def parse_config(config_file):
    config = {}
    with open(config_file, "r") as file:
        for line in file:
            key, value = line.strip().split(" = ", 1)

            try:
                config[key] = json.loads(value)
            except json.JSONDecodeError:
                config[key] = value

    #print(f"Parsed config: {config}")  # Add this line
    return config
