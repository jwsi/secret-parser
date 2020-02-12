import os, re, argparse


def parser(filename, secrets):
    """
    Parse the UTF-8 file and replace secret references with values from secrets dictionary.
    """
    print("Attempting to parse file: " + filename)
    with open(filename, 'r') as fd:
        contents = fd.read()
    results = re.findall("(\${{ *secrets.\w+ *}})", contents)
    filtered = [re.findall("\${{ *secrets.(\w+) *}}", x)[0] for x in results]
    for name, secret in secrets.items():
        index = filtered.index(name)
        contents = secret.join(contents.split(results[index]))
    with open(filename, 'w') as fd:
        fd.write(contents)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser("Parse GitHub Actions secrets")
    argparser.add_argument('filename', help='file to parse')
    argparser.add_argument('secrets', help='dictionary of secrets')
    args = argparser.parse_args()
    parser(args.filename, args.secrets)