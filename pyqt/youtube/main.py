import sys
import os
from PyQt5 import QtWidgets
import pywhatkit
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound
import time


from ui.mainwindow import Ui_MainWindow 

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Studierendenverwaltung")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.search)   
        
    def search(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #text = "what you want to search?"
            #var = gTTS(text=text, lang="en-AU", slow=False)
            #var.save("search.mp3")
            
            #playsound(".\s.wav")
            audio = r.listen(source)
            play = r.recognize_google(audio, language='ar')
            pywhatkit.playonyt(play) 
            
            text = "completed"
            var = gTTS(text=text, lang="en")
            var.save("search1.mp3")
            playsound(".\search1.mp3") 
            
            #os.remove("search.mp3")
            os.remove("search1.mp3")


window = MainWindow()
window.show()

sys.exit(app.exec_())

