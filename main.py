from configparser import parse_config
import translators
from cmdline_parser import cmdline_args

#main function that gets called in the commandline
def main():
    args = cmdline_args()

    config = parse_config(args.file)

    if not args.f:
        raise ValueError("You must specify at least one output format. Options are 'php', 'json', 'yaml', 'ini', 'xml', 'toml'.")
    
    for format in args.f:
        if format=='php':
            translators.translate_php(config)
        elif format =='json':
            translators.translate_json(config)
        elif format =='yaml':
            translators.translate_yaml(config)
        elif format =='ini':
            translators.translate_ini(config)
        elif format =='xml':
            translators.translate_xml(config)
        elif format == 'toml':
            translators.translate_toml(config)
    return

#run main IF this module is being called as the main function.
if __name__ == '__main__':
    main()