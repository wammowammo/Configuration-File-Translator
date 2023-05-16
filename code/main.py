from conparser import parse_config
import translators
from cmdline_parser import cmdline_args

def main():
    args = cmdline_args()

    try:
        config = parse_config(args.file)
    except Exception as e:
        print(f"Error: {e}")
        return

    if not args.f:
        raise ValueError("You must specify at least one output format."
                          "Options are 'php', 'json', 'yaml', 'ini', 'xml'," 
                          "'toml', 'bash', 'perl'.")

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
        elif format == 'bash':
            translators.translate_bash(config)
        elif format == 'perl':
            translators.translate_perl(config)

if __name__ == '__main__':
    main()
