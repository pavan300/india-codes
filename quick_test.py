from dictionaries import python_
from convert_to_english import translate_code_one2one


def test_python_function():
    sample_codes = {
        "English": [
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
        ],
        "Telugu": [
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
    }

    with open('test_scripts/output.txt', 'w') as f:
        for lang in sample_codes:
            if lang != "English":
                for each in sample_codes[lang]:
                    print(translate_code_one2one(each, python_[lang]), file=f)
            else:
                dict_ = {v: k for k, v in python_["Telugu"].items()}
                for each in sample_codes[lang]:
                    print(translate_code_one2one(each, dict_), file=f)

    return None


test_python_function()
