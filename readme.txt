This code supports all the languages as google translator.
This is a CLI app made using python3.

How does it work?

Its first input takes the word/sentence.
It detects the language of the word/sentence automatically.
Its second input takes the language in which we want to translate the word/sentence.
If we keep empty any input, it returns a value error.
Then it matches the language with languages in the file named languages.json.
If the language does not match with any language in the file, it returns a value error.
At last, it prints the translated word/sentence.