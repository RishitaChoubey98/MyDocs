import pyttsx3 as p
import wikipedia
import webbrowser
import datetime
import os
import smtplib
from news import speak_news
from diction import translate
from loc import weather


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        p.speak("Good Morning!")
        print("Good Morning!")

    elif 12 <= hour < 18:
        p.speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        p.speak("Good Evening!")
        print("Good Evening!")

    print("hello mam, I am jarvis, your personal assistant")
    p.speak("hello mam, I am jarvis, your personal assistant")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('your@email', to, content)
    server.close()


def takeCommand():
    query = input(p.speak("What can I do for you?\n"))
    print(query)
    return query


if __name__ == "__main__":
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wishMe()
    while True:

        s = takeCommand().lower()

        if "don't" in s or "dont" in s or "do not" in s:
            print("ok mam, i will not perform the following task")
            p.speak("ok mam, i will not perform the following task ")

        elif "wikipedia" in s:
            p.speak('Searching Wikipedia...')
            s = s.replace("wikipedia", "")
            results = wikipedia.summary(s, sentences=2)
            p.speak("According to Wikipedia")
            print(results)
            p.speak(results)

        elif 'location' in s:
            p.speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            p.speak('Here is the location ' + location)

        elif 'shutdown' in s:
            os.system('shutdown /p /f')

        elif 'weather' in s:
            p.speak("The current weather conditions are:")
            weather()

        elif 'dictionary' in s:
            p.speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())


        elif "open youtube" in s:
            webbrowser.open("youtube.com")
            p.speak("opening Youtube")
            print("opening Youtube")

        elif "open google" in s:
            webbrowser.open("google.com")
            p.speak("opening google")
            print("opening google")

        elif "open stackoverflow" in s:
            webbrowser.open("stackoverflow.com")
            p.speak("opening Stackoverflow")
            print("opening Stackoverflow")

        elif "time" in s:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            p.speak(f"Mam, the time is {strTime}")

        elif "open code" in s:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            p.speak("opening Visual Studio")
            os.startfile(codePath)


        elif 'location' in s:
            p.speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            p.speak('Here is the location ' + location)


        elif "notepad" in s or "run" in s or "execute" in s:
            print("ok mam , opening notepad")
            p.speak("ok mam , opening notepad")
            os.system("notepad")

        elif 'news' in s:
            p.speak('Ofcourse mam.')
            speak_news()


        elif "stop" in s or "offline" in s or "quit" in s:
            print("ok mam , see you soon!")
            p.speak("ok mam , see you soon")
            break

        elif "email to rishita" or "email" in s:
            try:
                p.speak('What should I say?')
                print("What should I say?")
                content = takeCommand()
                to = 'email_of_receiver'
                sendEmail(to, content)
                print("Email has been sent to,", to)
                p.speak('Email has been sent!')


            except Exception as e:
                p.speak('Sorry mam, Not able to send email at the moment')

        elif "play music" or "music" in s:
            music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            break
