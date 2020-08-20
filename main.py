import os
import pyttsx3 as p
import datetime
import smtplib
import wikipedia
import webbrowser


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        p.speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        p.speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        p.speak("Good Evening!")
        print("Good Evening!")

    print("hello mam, I am jarvis, how can I help you?")




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def takeCommand():
    inp = input(p.speak("hello mam, I am jarvis, How can I help you?\n"))
    return inp


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if "don't" in query or "dont" in query or "do not" in query:
            print("ok mam , i will not perform the following task")
            p.speak("ok mam , i will not perform the following task ")

        elif "wikipedia" in query:
            p.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            p.speak("According to Wikipedia")
            print(results)
            p.speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            p.speak("opening Youtube")
            print("opening Youtube")

        elif "open google" in query:
            webbrowser.open("google.com")
            p.speak("opening google")
            print("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            p.speak("opening Stackoverflow")
            print("opening Stackoverflow")


        elif 'play music' or 'music' in query:
             music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            p.speak(f"Mam, the time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            p.speak("opening Visual Studio")
            os.startfile(codePath)

        elif "email to rishita" or "email" in query:
            try:
                p.speak("What should I say?")
                content = takeCommand()
                to = "rishitaEmail@gmail.com"
                sendEmail(to, content)
                p.speak("Email has been sent!")
            except Exception as e:
                print(e)
                p.speak("Sorry mam. I am not able to send this email")
        elif "chrome" in query or "run" in query or "execute" in query:
            print("ok mam , opening chrome")
            p.speak("ok mam , opening chrome")
            os.system("chrome")


        elif "notepad" in query or "run" in query or "execute" in query:
             print("ok mam , opening notepad")
             p.speak("ok mam , opening notepad")
             os.system("notepad")


        elif "stop" in query or "offline" in query or "quit" in query:
              print("ok mam , see you soon!")
              p.speak("ok mam , see you soon")
              break

        else:
            print("Sorry mam, I didn't get you")
            p.speak("Sorry mam, I didn't get you")







