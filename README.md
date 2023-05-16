# Configuration-File-Translator
Python command line program which reads in a config file and translates it to a config file in another language.

## Table of Contents
1. [Overview](#overview)
   * [Description](#description)
   * [Modules](#modules)
2. [Getting Started](#getting-started)
   * [Prerequisites](#prerequisites)
   * [Installing Required Libraries](#installing-required-libraries)
3. [Running the Code](#running-the-code)
   * [Command-line Options](#command-line-options)
4. [Usage Examples](#usage-examples)
5. [Directory](#directory)
   * [Included Files](included-files)
   * [License](#license)

## Overview
### Description
Python command line program which reads in a config file and translates it to a config file in another language.

With its simple and intuitive command-line interface, the config translator program provides a convenient tool for users who need to quickly translate config files to other languages.

### Modules
The application has 4 main modules:

* `showTable.py` - This module is the main script that is called in the command-line.

* `cmdline_parser.py` - This module parses and stores the command-line arguments to be used later.

* `configparser.py` - This module parses the config file and stores its data in a dictionary.

* `translators.py` - This module translates the data stored in the dictionary into a config file of another language.

## Getting Started
Follow these steps to set up and run the Config Translator program:

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.6 or higher
- `yaml` library
- `toml` library

### Installing Required Libraries

To install the required libraries, open a terminal and run the following command:

```bash
pip install pyyaml toml
```

## Running the Code

To run the application, open a terminal and use ls and cd to navigate to the directory containing the Configuration File Translator files. Then, run the following command:

```bash
python3 main.py <config_file> [languages]
```

Where `<config file>` is the path to the config file, and `[languages]` are the languages you wish to translate the original config file to.

### Command-line Options
Languages to translate to:
 - `php`
 - `json`
 - `yaml`
 - `ini`
 - `xml`
 - `toml`

## Usage Examples
Please visit `translatorOutput.md` for a demonstration on what all of the following output

1. One language:
```bash
python3 main.py config.txt php
```

2. Multiple languages:
```bash
python3 main.py config.txt php json yaml ini xml toml
```

## Directory
### Included Files
To see a test example containing a sample config file, view: 
* ```config.txt```

For information regarding the API used by the config translator program modules, view:
* ```api_description.md```

For information regarding the dependencies used in the config translator program, view:
* ```dependencies.md```

For information regarding the data printed by the config translator program using the example data, view:
* ```translatorOutput.md```

### License
[MIT](https://choosealicense.com/licenses/mit/)