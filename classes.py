import speech_recognition as sr 


class Recorder():
    def __init__(self, r=sr.Recognizer()):
        self.r = r

    def record(self):
        with sr.Microphone() as source:
            print("say Something")
            global audio 
            audio = self.r.listen(source)


class Recorder_print(Recorder):
    def __init__(self):
        Recorder.__init__(self, r=sr.Recognizer()) 

    def printer(self):
        print(self.r.recognize_google(audio, language='en-US'))


def main():
    r = Recorder()
    r.record()
    rp = Recorder_print()
    rp.printer()


if __name__ == "__main__":
    main()