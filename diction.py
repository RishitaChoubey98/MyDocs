from difflib import get_close_matches
import pyttsx3 as p
import json


data = json.load(open('data.json'))
engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def takeCommand():
    query = input(p.speak("Ask anything\n"))
    print(query)
    return query


def translate(word):
    word = word.lower()
    if word in data:
        p.speak(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        p.speak('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = takeCommand().lower()
        if 'yes' in ans:
            p.speak(data[x])
        elif 'no' in ans:
            p.speak("Word doesn't exist. Please make sure you spelled it correctly.")
        else:
            p.speak("We didn't understand your entry.")

    else:
        p.speak("Word doesn't exist. Please double check it.")


if __name__ == '__main__':
    translate()