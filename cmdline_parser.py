import argparse

def cmdline_args():
    parser = argparse.ArgumentParser(description='Translate a Python config file.')
    parser.add_argument('file', type=str, help='Python config file to translate')
    parser.add_argument('f', type=str, nargs='+',choices=['php', 'json', 'yaml'], help='Choose which languages to translate to.')
    args = parser.parse_args()
    #print(f"Parsed arguments: {args}")  # Add this line
    return args
