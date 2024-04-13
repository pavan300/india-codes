from tel_eng_dict import eng2tel, tel2eng
import re
import argparse


def translate_code(code, dict_):
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


def translate_python_script(script_path, eng2tel):
    code = open(script_path, "r").read()
    # print(code)
    return translate_code(code, eng2tel)


def test_function():
    eng_sample_code = [
        """
variable= 5
condition = True
if condition:
    print("Variable:", variable)
    print("Condition:", condition)
else:
    print("False: incorrect")""",

        """
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
    print("Sum of numbers:", total)""",

        """
count = 10
for num in range(count):
    print(num)
    count += 1
    """,

        """
class MyClass:
    message= "This is a class"
    def print_message(self):
        print(self.message)""",

        """
path = "/class/example/path/file.txt"
try:
    with open(path) as file:
        pass
except:
    print("File not found")""",
    ]

    tel_sample_code = [
        """
చెల్లు = 5
సందర్భం = నిజం
ఐతే సందర్భం:
    ముద్రించు("చెల్లు:", చెల్లు)
    ముద్రించు("సందర్భం:", సందర్భం)
లేదా:
    ముద్రించు("అబద్ధం: తప్పు")
""",
        """
సంఖ్యలు = [1, 2, 3, 4, 5]
మొత్తం = 0
ప్రతి సంఖ్య లో సంఖ్యలు:
    మొత్తం += సంఖ్య
ముద్రించు("సంఖ్యల మొత్తం:", మొత్తం)
""",
        """
కౌంట్ = 10
ప్రతి సంఖ్య లో శ్రేణి(కౌంట్):
    ముద్రించు(కౌంట్)
    కౌంట్ += 1
""",
        """
వర్గం నావర్గము:
    సందేశం = "ఇది ఒక వర్గం"
    నిర్వచనం ముద్రించు_సందేశం(సందేశం):
        ముద్రించు(సందేశం)
""",
        """
పథం = "/వర్గం/ఉదాహరణ/పథం/ఫైల్.టెక్స్ట్"
ప్రయత్నించు:
    తో open(పథం) లా ఫైల్:
        కానివ్వు
తప్ప:
    ముద్రించు("ఫైల్ కనుగొనబడలేదు")
"""
    ]

    with open('output.txt', 'w') as f:
        for each in tel_sample_code:
            print(translate_code(each, tel2eng), file=f)

        for each in eng_sample_code:
            print(translate_code(each, eng2tel), file=f)

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert python code across languages.')
    parser.add_argument('--script_file', type=str,
                        help='File with the script')
    parser.add_argument('--lang', type=str,
                        help='Language to convert it into')
    parser.add_argument('--out_file', type=str, default="converted_code", required=False,
                        help='Output file')

    args = parser.parse_args()

    extension = args.script_file.split(".")[-1]
    if extension == "converted_code":
        args.out_file += "." + extension

    if args.lang == "Telugu":
        dict_ = eng2tel
    elif args.lang == "English":
        dict_ = tel2eng

    # print(dict_)

    with open(args.out_file, "w") as f:
        f.write(translate_python_script(args.script_file, dict_))
