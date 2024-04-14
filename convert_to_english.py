from dictionaries import python_,java_
import re
import argparse


def translate_code_one2one(code, dict_):
    # Extract code within single and double quotes
    quoted_code = re.findall(r"'(.*?)'|\"(.*?)\"", code)

    # Remove quoted code from the original code
    unquoted_code = re.sub(r"'(.*?)'|\"(.*?)\"", "{}", code)

    # Create a pattern to match keys from dict_
    pattern = re.compile(r'|'.join(re.escape(key) for key in dict_))

    # Use re.sub to replace all occurrences of keys with their values
    translated_code = pattern.sub(lambda m: dict_[m.group()], unquoted_code)

    # Put the quoted code back into the translated code
    for i, (quote, quoted_text) in enumerate(quoted_code):
        translated_code = translated_code.replace(
            "{}", '"' + quote + quoted_text + quote + '"', 1)

    return translated_code


def translate_script(script_path, eng2tel):
    code = open(script_path, "r",encoding="utf-8").read()
    return translate_code_one2one(code, eng2tel)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert code across programming and natural languages.')
    parser.add_argument('--script_file', type=str,
                        help='File with the script')
    parser.add_argument('--prog_lang', type=str,
                        help='The Programming Language to convert')
    parser.add_argument('--lang', type=str,
                        help='The Natural Language to convert it into')
    parser.add_argument('--out_file', type=str, default="converted_code", required=False,
                        help='Output file')

    args = parser.parse_args()

    extension = args.script_file.split(".")[-1]
    if extension == "converted_code":
        args.out_file += "." + extension

    if args.prog_lang == "python":
        dict_ = python_[args.lang]
    # print(dict_)
    if args.prog_lang == "java":
        dict_ = java_[args.lang]
    

    with open(args.out_file, "w") as f:
        f.write(translate_script(args.script_file, dict_))
