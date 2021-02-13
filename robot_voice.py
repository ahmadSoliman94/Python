#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install SpeechRecognition')


# In[5]:


get_ipython().system('pip install playsound')


# In[6]:


get_ipython().system('pip install pyaudio')


# In[7]:


get_ipython().system('pip install pipwin')
get_ipython().system('pip install pyaudio')


# In[8]:


get_ipython().system('pip install PyAudio')


# In[1]:


conda install pyaudio


# In[32]:


import os 
import time
import playsound
import speech_recognition as sr
from gtts import gTTS 

def speak(text):
    tts = gTTS(text = text,lang = "de")
    filename = "v1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
            pass
            print(said)
        except Exception as e:
            print(str(e))
            
            
    return(said)

text = get_audio()

if "hi" in text:
    speak('moin moin')
if "I am fine" in text:
    speak('that is good for you ')
if "wie heisst du" in text:
    speak('ich heiße elham')
    


# In[ ]:





# In[ ]:




