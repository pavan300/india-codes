# India codes

This repository targets individuals in India who lack English proficiency and programming experience. The tools here allow writing and executing code solely in one's native language, eliminating the English language barrier. Our vision is to support all Indian languages and programming languages, enabling a diverse population to learn coding without linguistic constraints.

## Features

- Translate individual code snippets or entire script files
- Support for multiple programming languages
- Support for multiple natural languages
- Currently supported languages:
  - Programming languages
    - Python
  - Natural languages
    - Telugu 

1. Clone the repository:

```
bash
git clone https://github.com/Posterior-AI/india-codes.git
```

2. Navigate to the project directory:

```
bash
cd india-codes
```

## Approach

Every language has their own set of keywords. All (major) programming languages have these keywords in English. Some programming languages (Python, Javascript, Rust) support unicode, and some (C, C++) don't. 

### Version 1 (Currently):
 - User writes the entire code in their native language.
 - The language supports unicode identifiers.
 - One-to-one mapping for English keywords with native language keywords.
 - The programming language keywords from the user code will be replaced to actual English keywords.
 - This is executable code.

### Version 1.2 (Next):
 - Everything from A.
 - After replacing the keywords, all identifiers will also be transliterated to English. This will effectively support all languages. Even the languages which don't support unicode identifiers.

## Version C (Later):
 - Using Abstract Syntax Trees to make the syntax more sensible in native languages.

## Usage

1. The `dictionaries.py` file contains the dictionaries with the desired keyword mappings for the programming languages and natural languages you want to support.

2. Run the `convert_to_english.py` script from the command line with the following arguments:

```
bash

python .\convert_to_english.py --script_file <script_file> --prog_lang <programming_language> --lang <target_language> --output <output_file>

- `<script_file>`: Path to the script file you want to translate
- `<programming_language>`: Programming language of the script file (e.g., python). All small letters.
- `<target_language>`: Target natural language for the translation (e.g., Telugu). First letter Capital.
- `<output_file>`: Path to the output file where the translated code will be written
```

For example, to translate a Python script from English to Telugu:

```
bash
python convert_to_english.py --script_file test_scripts/tel_python_code.py --prog_lang python --lang Telugu --out_file test_scripts/tel_python_code_converted.py
```


## Testing

The `quick_test.py` script provides a function `test_python_function` to test the translation functionality by converting sample code snippets between English and Telugu. You can modify this script to add your own test cases.

## Example

Python code in Telugu.
```
చెల్లు = 5
సందర్భం = నిజము
ఐతే సందర్భం:
    ముద్రించు("చెల్లు:", చెల్లు)
    ముద్రించు("సందర్భం:", సందర్భం)
లేదా:
    ముద్రించు("అబద్ధం: తప్పు")


సంఖ్యలు = [1, 2, 3, 4, 5]
మొత్తం = 0
ప్రతి సంఖ్య లో సంఖ్యలు:
    మొత్తం += సంఖ్య

ముద్రించు("సంఖ్యల మొత్తం:", మొత్తం)


కౌంట్ = 10
ప్రతి సంఖ్య లో శ్రేణి(కౌంట్):
    ముద్రించు(కౌంట్)
    కౌంట్ += 1


वर्ग मेरी_कक्षा:
    संदेश = "यह एक कक्षा है"
    निर्धारित मुद्र_संदेश(self):
        मुद्र(self.संदेश)


पथ = "/कक्षा/उदाहरण/पथ/फ़ाइल.टेक्स्ट"
प्रयास:
    साथ खोलें(पथ) जैसा फ़ाइल:
        चलो
अपवाद:
    मुद्र("फ़ाइल नहीं मिली")

```

Converted code.
```
చెల్లు = 5
సందర్భం = True
if సందర్భం:
    print("చెల్లు:", చెల్లు)
    print("సందర్భం:", సందర్భం)
else:
    print("అబద్ధం: తప్పు")


సంఖ్యలు = [1, 2, 3, 4, 5]
మొత్తం = 0
for సంఖ్య in సంఖ్యలు:
    మొత్తం += సంఖ్య

print("సంఖ్యల మొత్తం:", మొత్తం)


కౌంట్ = 10
for సంఖ్య in range(కౌంట్):
    print(కౌంట్)
    కౌంట్ += 1


class मेरी_कक्षा:
    संदेश = "यह एक कक्षा है"

    def print_संदेश(self):
        print(self.संदेश)


पथ = "/कक्षा/उदाहरण/पथ/फ़ाइल.टेक्स्ट"
try:
    with open(पथ) as फ़ाइल:
        pass
except:
    print("फ़ाइल नहीं मिली")
```


## Contributing

Contributions are highly welcome! If you want to add support for additional programming languages or natural languages, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Update the `dictionaries.py` file with the keyword mappings for the new programming and natural language(s)
4. Test your changes
5. Submit a pull request
