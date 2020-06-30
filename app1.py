import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word]

    elif word.upper() in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
            "Did you mean %s instead ? " %get_close_matches(word, data.keys())[0] + word + " Enter yes or no .")
        if yn.lower() == "yes":
            return data[get_close_matches(word, data.keys())[0]]

        elif yn.lower() == "no":
            return "The word doesn't exists . Please double check it . "

        else:
            return "We didn't understand your query "


word = input('Enter a word : ')
output = translate(word)

if type(output) == list:
    for i in output:
        print(i)

else:
    print(output)
