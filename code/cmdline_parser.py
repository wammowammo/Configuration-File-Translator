import argparse

def cmdline_args():
    parser = argparse.ArgumentParser(description='Translate a Python config file.')
    parser.add_argument('file', type=str, help='Python config file to translate')
    parser.add_argument('f', type=str, nargs='+',
                        choices=['php', 'json', 'yaml', 'ini', 'xml', 'toml', 'bash', 'perl'],
                        help='Choose which languages to translate to.')
    args, unknown = parser.parse_known_args()

    if unknown:
        print(f"Warning: Unknown arguments {unknown} were ignored.")

    if not args.f:
        parser.error("You must specify at least one output format. Options are 'php', 'json', 'yaml', 'ini', 'xml', 'toml', 'bash', 'perl'.")

    if len(args.file.split()) > 1:
        parser.error("Multiple data files provided. Please provide only one data file.")

    return args

