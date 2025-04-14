import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from datetime import datetime
# imp
import cv2
from requests import get
# import random
import pywhatkit as pwk
import sys
import pyjokes
import time
# from bs4 import BeautifulSoup
# from
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',
voices[len(voices)-1].id)
# for voice in voices:
# print(voice.id)
# engine.setProperty('voices',voice.id)
# engine.say("Hello sir")
# engine.runAndWait()
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def wishMe():
    # hour = int(datetime.datetime())
    hour = datetime.strftime("%H:%M:%S")
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour==12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    # strTime = datetime.datetime.now().
tm = ("%H:%M:%S")
speak(f" Sir its {tm} , i am Mister Nobody, Tell me,how can i help you")
def takeCommand():
# it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
    # after giving command by user jarvis
    # will take time of 1 sec to reply
        audio = r.listen(source, timeout = 5, phrase_time_limit=8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
            print("Say that again please...")
            return "None"
    return query

# def news():
#     main_url = 'http://newapi.org/v2/topheadlines?'
#     sources=techcrunch&apikey='84b5bb82621e49b682307f984a8e3282'
#     main_page=requests.get(main_url).json()
#     # print)(main_page)
#     articles = main_page["articles"]
#     head = []
#     day = ["first" , "second", "third","fourth","fifth"]
#     for ar in articles:
#         head.append(ar["title"])
#         for i in range(len(day)):
#             speak(f"today's {day[i]} news is:",{head[i]})
if __name__ == "__main__":
# speak("Kedar is Good boy")
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower() # type: ignore
    # logic for excuting task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,
            sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    #---------------------------->>>>>>>>here nova must give info about user spoken thing
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")#-------------...........................................>>>>nova must open youtube
        elif 'open google' in query:
            webbrowser.open("google.com")#-------
            # ------.................
            # ..........................>>>>nova must
            # open google
            speak("Welcome sir...Google is fetching for you")
            speak("Sir, what should i search on google")
            cm = takeCommand().lower() # type: ignore
            webbrowser.open(f"{cm}")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")#-------------..........
            # .................................>>>>jarvis
            # must open stackoverflow
        elif 'open linkedin' in query:
            webbrowser.open("Linkedin.com")
            speak("sure")
        elif 'open geeks for geeks' in query:
            webbrowser.open("Geeks for Geeks")
            # elif 'open chat Gpt' in query:
            # webbrowser.openI("chat.openai.com/auth/login?next=%2F")
        elif 'how are you' in query:
            speak("I am fine sir...what about you")
        elif 'project teacher' in query:
            speak("Sneha mam")
            # elif 'largest country in t*he world' in query:
            # speak("Russia")
            # print("Russia")
        elif 'open Notepad' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\StartMenu\\Programs\\Accessories.exe")
        elif 'activate face recognition system' in query:
            speak("Face recognition system activated")
            os.startfile("C:\\Users\\kedar\\OneDrive\\Desktop\\Web development courseCWH\\face_recognition_system.py")
        elif 'play music' in query:
            music_dir ='C:\\Users\\kedar\\Music\\Favorite songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,
            songs[1]))
            speak("Have a good day Sir...")
        # elif 'time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #     speak(f"Sir , the time is {strTime}")
            
        elif 'open code' in query:
            codePath ="C:\\Users\\kedar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        # elif 'email to kedar' in query:
        # try:
        #     speak("What should I say?")
        #     content = takeCommand()
        #     to = "kedarmahadik21@gmail.com"
        #     sendEmail(to , content)
        #     speak("Email has been sent kedar!")
        # except Exception as e:
        #     print(e)
        #     speak("Sorry sir...I am not able to send this email at the moment")
        elif 'open calculator' in query:
            webbrowser.open("calculator")
        elif 'open facebook' in query:
            webbrowser.open("Facebook.com")
            
        elif 'open command prompt' in query:
            path1 ="C:\\Users\\kedar\\AppData\\Roaming\\Microsoft\\Windows\\StartMenu\\Programs\\System Tools\\CommandPrompt.lnk"
            os.startfile(path1)
            # to close the cmd
        elif 'close command prompt' in query:
            speak("ok sir, command promt is closing")
            os.system("taskkill /f /im Command Prompt.lnk")
        # elif 'set alarm' in query:
        #     Al = int(datetime.datetime.now().hour)
        #     if Al == 16:
        #         music_dir = 'C:\\Users\\kedar\\Music\\Favorite songs'
        #     songs = os.listdir(music_dir)
        #     # print(songs)
        #     os.startfile(os.path.join(
        #     music_dir, songs[1]))
            # ==============================
            # =====================================
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the window" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rundll32.exepowrprof.dll,SetSuspendState 0,1,0")
            # ==============================
            # ==============================
            # ================
        # elif " switch the window " in query:
        #     pyautogui.keyDown("alt")
        #     pyautogui.press("tab")
        #     time.sleep(1)
        #     pyautogui.keyUp("alt")
        elif "email to kedar" in query:
            pass
        # elif 'open camera' in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #     ret, img = cap.read()
        #     cv2.imshow('webcam',img)
        #     k = cv2.waitKey(50)
        #     if k == 27:
        #     break
        #     cap.release()
        #     cv2.destroyAllWindows()
        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your ip address is {ip}")
            # whatsapp messages sending
        # elif "send message" in query:
        #     msg = takeCommand().lower() # type: ignore
        #     pwk.sendwhatmsg("+917720032922",
        #     {msg}, 2,2)
        elif "play on youtube" in query:
            speak("what should i play")
            pl = takeCommand().lower() # type: ignore
            pwk.playonyt(f"{pl}")
        # elif "send email to kedar" in query:
        #     speak("sir what should i say")
        #     query = takeCommand().lower()
        #     if "send a file"in query:
        #         yourEmail = takeCommand().lower()
        #         email = f'{yourEmail}@gmail.com'
        #         speak("and your password")
        #     password = f'{yourEmail}'
        #     speak("to whom i send this
        #     email")
        #     send_to_email =
        #     f'{yourEmail}@gmail.com'
        #     speak("okay sir,what is the
        #     subject for this email")
        #     query2 = takeCommand().lower()
        #     message = query2
        #     speak("sir please enter the
        #     correct path of the file into shell")
        #     file_loc = input("please enter
        #     the path")
        #     speak("please wait sir, i am
        #     sending email now")
        #     msg = MIMEMultipart()
        #     msg['From'] = email
        #     msg['To'] = send_to_email
        #     msg['subject'] = subject
        #     msg.attach(MIMEText(message,
        #     'plain'))
        #     # setup attachment
        #     filename =
        #     os.path.basename(file_loc)
        #     attachment = open(file_loc,"rb")
        #     part =
        #     MIMEBase('application','octet-stream')
        #     part.set_payload(attachment.
        #     read())
        #     encoders.encode_base64(part)
        #     part.add_header('Content-
        #     Disposition',"attachment; filename = %s"
        #     %filename)
        #     # attach the attachmentt to the
        #     MIMEMultipart object
        #     msg.attach(part)
        #     server =
        #     smtplib.SMTP('smtp.gmail.com', 587)
        #     server.ehlo()
        #     server.starttls()
        #     server.login('kedarmahadik21@
        #     gmail.com' , 'kedar@2121')
        #     server.sendemail('kedarmahadik
        #     21.com', to, content)
        #     server.close()
        elif "open whatsapp" in query:
            webbrowser.open("Whatsapp.com")
        elif "close the system" in query:
            speak("System is now closing...have a good day sir")
            sys.exit()
#         elif "tell me news" in query:
#             speak("please wait sir,feteching the latest news")
# news()
            