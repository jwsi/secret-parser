import os, re, argparse


def parser(filename, secret_name, secret_value):
    """
    Parse the UTF-8 file and replace secret references with values from secrets dictionary.
    """
    print("Attempting to parse file: " + filename)
    with open(filename, 'r') as fd:
        contents = fd.read()
    results = re.findall("(\${{ *secrets.\w+ *}})", contents)
    filtered = [re.findall("\${{ *secrets.(\w+) *}}", x)[0] for x in results]
    index = filtered.index(secret_name)
    contents = secret_value.join(contents.split(results[index]))
    with open(filename, 'w') as fd:
        fd.write(contents)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser("Parse GitHub Actions secrets")
    argparser.add_argument('filename', help='file to parse')
    argparser.add_argument('secret_name', help='name of secret to search for')
    argparser.add_argument('secret_value', help='value of secret to replace name with')
    args = argparser.parse_args()
    parser(args.filename, args.secret_name, args.secret_value)