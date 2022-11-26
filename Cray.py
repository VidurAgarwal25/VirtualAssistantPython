#%%
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import cv2
import sys
import smtplib
import requests
from requests import get
import pywhatkit
import pyjokes
import time
import pyautogui
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from crayui import Ui_crayui
from bs4 import BeautifulSoup

#%%
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',175)

#%%
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#%%
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Cray Sir. Please tell me how may I help you")       
#%%
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maestro025agarwal@gmail.com', 'lifegood@1234')
    server.sendmail('maestro025agarwal@gmail.com', to, content)
    server.close()
#%%
def news():
    main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b91e6164a385482f936a74a2531d3cf9'
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is:", {head[i]})
        print("\n")
        speak(f"today's {day[i]} news is: {head[i]}")

#%%
def pdf_reader():
    book = open('book.pdf','rb')
    pread=PyPDF2.PdfFileReader(book)
    pages=pread.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Sir please enter a page number I have to read")
    pg=int(input("please enter the page number: "))
    page=pread.getPage(pg)
    t=page.extractText()
    print(t)
    speak(t)

#%%
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.recog()

    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=5)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query
        
    def TaskExecution(self):
        pyautogui.press('esc')
        speak("verification successful")
        speak("welcome back sir")
        wishMe()
        while True:
    # if 1:
            self.query = self.takeCommand().lower()

        # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open notepad' in self.query:
                npath="C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)
            elif 'close notepad' in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
            elif "joke" in self.query:
                joke=pyjokes.get_joke()
                speak(joke)
            elif 'command prompt' in self.query:
                os.system("start cmd")
            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
            elif 'open instagram' in self.query:
                webbrowser.open("instagram.com")

            elif 'open facebook' in self.query:
                webbrowser.open("facebook.com")

            elif 'open google' in self.query:
                speak("sir, what should i search on google")
                cm=self.takeCommand().lower()
                webbrowser.open(f"{cm}")
        
            elif 'tab' in self.query:
                webbrowser.open("google.com")
        
            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")   

            elif 'temperature' in self.query:
                search=input("Enter city")
                url=f"https://www.google.com/search?q=temperature in{search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temp=data.find("div",class_="BNeawe").text
                speak(f"current temperature in {search} is {temp}")

            elif 'play music' in self.query:
                music_dir = "C:/Users/Asus/Desktop/Music"
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                codePath = "C:/Users/Asus/Desktop/ironman.gif"
                os.startfile(codePath)
        
            elif 'open camera' in self.query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(5)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif 'ip address' in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")
        
            elif "shut" in self.query:
                os.system("shutdown /s /t 5")
            elif "restart" in self.query:
                os.system("shutdown /r /t 5")
        
            elif "sleep" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
            elif 'switch' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif 'news' in self.query:
                speak("please wait, I am fetching the latest news for you")
                news() 

            elif 'where we are' in self.query:
                speak("wait sir, let me check")
                try:
                    ipadd=requests.get('https://api.ipify.org').text
                    print(ipadd)
                    url='https://get.geojs.io/v1/ip/geo/' +ipadd+ '.json'
                    loc=requests.get(url)
                    loc_data=loc.json()

                    city=loc_data['city']
                    country=loc_data['country']
                    print(f"Sir I am not sure, but I think we are in {city} city of {country} country.")
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country.")
                except Exception as e:
                    speak("sorry sir, due to the network issue I am not able to find where we are.")
                    pass 
            elif "read pdf" in self.query:
                pdf_reader()

            elif "speed" in self.query:
                webbrowser.open("fast.com")

            elif "increase" in self.query:
                pyautogui.press("volumeup")

            elif "decrease" in self.query:
                pyautogui.press("volumedown")

            elif "mute" in self.query:
                pyautogui.press("volumemute")


            elif "alarm" in self.query:
                print("Please tell me the time to set alarm")
                speak("Please tell me the time to set alarm")
                tt=input()
                tt=tt.upper()
                import myalarm
                myalarm.alarm(tt)

            elif 'email to sarthak' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand().lower()
                    to = "sgsaarthak7@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir. I am not able to send this email") 
            elif 'stop' in self.query:
                speak("Thanks for using me, have a good day!")
                sys.exit()
    
    def recog(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


        id = 0 #number of persons you want to Recognize


        names = ['','vidur']  #names, leave first empty bcz counter starts from 0


        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
        cam.set(3, 640) # set video FrameWidht
        cam.set(4, 480) # set video FrameHeight

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        # flag = True

        while True:

            ret, img =cam.read() #read the frames using the above created object

            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale( 
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match 
                if (accuracy < 100):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    self.TaskExecution()

                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("Thanks for using this program, have a good day.")
        cam.release()
        cv2.destroyAllWindows()

#%%
startExecution=MainThread()
#%%
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_crayui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("x.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


#%%
app=QApplication(sys.argv)
cray= Main()
cray.show()
exit(app.exec_())


