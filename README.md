# Configuration-File-Translator

Python command line program that reads in a config file and translates it to a config file in another language.

## Table of Contents
1. [Overview](#overview)
   * [Description](#description)
   * [Modules](#modules)
2. [Getting Started](#getting-started)
   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
3. [Usage](#usage)
   * [Command-line Options](#command-line-options)
4. [Usage Examples](#usage-examples)
5. [Directory](#directory)
   * [Included Files](#included-files)
   * [License](#license)
   * [Security Considerations](#security-considerations)
6. [System Administration](#system-administration)
   * [Supported Platforms](#supported-platforms)
   * [Compiling and Installing](#compiling-and-installing)
7. [Developer](#developer)
   * [Algorithm Description](#algorithm-description)
   * [Continuing and Extending the Work](#continuing-and-extending-the-work)


## Overview
### Description
The Configuration-File-Translator is a Python command-line program that provides a convenient tool for translating config files to other languages. With its simple and intuitive interface, users can easily convert their config files to different formats.

### Modules
The application consists of the following main modules:

* `main.py`: The main script that is called from the command line and orchestrates the translation process.

* `cmdline_parser.py`: Parses and stores the command-line arguments to be used later.

* `conparser.py`: Parses the config file and stores its data in a dictionary.

* `translators.py`: Translates the data stored in the dictionary into a config file of another language.

## Getting Started
Follow these steps to set up and run the Configuration-File-Translator program:

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.6 or higher
- `yaml` library
- `toml` library

### Installation
To install the required libraries, open a terminal and run the following command:
```bash
pip install pyyaml toml
```

## Usage
To run the application, open a terminal, navigate to the directory containing the Configuration-File-Translator files, and execute the following command:

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
 - `bash`
 - `perl`

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

For information regarding the data printed by the config translator program using the example data, view:
* ```translatorOutput.md```

### License
[MIT](https://choosealicense.com/licenses/mit/)

## Security Considerations
Please refer to the SECURITY.md file for important security considerations and instructions for reporting security issues.


## System Administration
### Supported Platforms
The Configuration-File-Translator is designed to run on any platform that supports Python 3.6 or higher.

### Compiling and Installing
As a Python-based application, there is no need for compilation. Simply follow the installation instructions provided earlier to set up the required dependencies.

## Developer
### Algorithm Description
The Configuration-File-Translator uses a modular approach to read and parse the config file, store the data in a dictionary, and translate it into various formats. The cmdline_parser.py module handles command-line argument parsing, while the translators.py module provides translation functions for different languages.

### Continuing and Extending the Work
To continue and extend the work on the Configuration-File-Translator, you can consider the following:

- Adding support for more languages by implementing translation functions in the translators.py module.
- Enhancing the error handling and validation in the cmdline_parser.py and configparser.py modules to provide better feedback and handle edge cases.
- Optimizing the translation process for large config files by implementing efficient algorithms and techniques.
- Writing unit tests to ensure the stability and correctness of the codebase.
- Improving the documentation, code comments, and code structure to enhance maintainability and readability.
- Adding support for additional communication protocols to facilitate seamless translation between systems. This can involve implementing new translation functions or modules to handle specific protocols such as REST API, MQTT, or SOAP.
- Expanding the language support by incorporating translation capabilities for any language. This can be achieved by enhancing the translators module to handle language-specific syntax, encoding, and formatting requirements. Consider leveraging existing translation libraries or services to enable translation to a wide range of languages.

By incorporating these features, you can enhance the flexibility and versatility of the Configuration-File-Translator, allowing users to translate config files across different communication protocols and language boundaries.

Please note that the implementation details and specific approaches may vary depending on the requirements and constraints of your project.









