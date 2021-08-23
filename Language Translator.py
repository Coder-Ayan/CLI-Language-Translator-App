import requests
from json import load as jsonLoad

URL = "https://translate.google.com/translate_a/single" + "?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=" + "auto" + "&ie=UTF-8" + "&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"

with open('languages.json') as jf:
    langs = jsonLoad(jf)['languages']

s = input("Enter the sentence(Any language): ")
translate = input("Translate to: ")

if s == '' or translate == '':
    raise ValueError("Values are required")

for key in langs:
    if key == translate.lower().capitalize() or langs[key] == translate.lower():
        tl = langs[key]
        break
else:
    raise ValueError("Unknown language to translate")

PARAMS = {
    'q': s,
    'tl': tl,
    'format': 'text',
    'sl': 'auto'
}

result = requests.post(url=URL, params=PARAMS)
print(result.json()['sentences'][0]['trans'])
