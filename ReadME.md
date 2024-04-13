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

python convert_to_english.py --script <script_file> --lang <programming_language> --target <target_language> --output <output_file>

- `<script_file>`: Path to the script file you want to translate
- `<programming_language>`: Programming language of the script file (e.g., python). All small letters.
- `<target_language>`: Target natural language for the translation (e.g., Telugu). First letter Capital.
- `<output_file>`: Path to the output file where the translated code will be written
```

For example, to translate a Python script from English to Telugu:

```
bash
python convert_to_english.py --script test_scripts/eng_python_code.py --lang python --target Telugu --output test_scripts/tel_python_code_converted.py
```


## Testing

The `quick_test.py` script provides a function `test_python_function` to test the translation functionality by converting sample code snippets between English and Telugu. You can modify this script to add your own test cases.


## Contributing

Contributions are highly welcome! If you want to add support for additional programming languages or natural languages, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Update the `dictionaries.py` file with the keyword mappings for the new programming and natural language(s)
4. Test your changes
5. Submit a pull request
