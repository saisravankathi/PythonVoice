import speech_recognition as sr
import sys


class Speech:

    def __init__(self,value, idle_timeout):
        #Call to get the list of microphones, where the porgram is being executed.
        #self.list_of_microphones()
        self.count = value
        self.idle_tout = idle_timeout
        self.obtain_audio()
        
    def list_of_microphones(self):
        
        for index,name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index,name))

    def obtain_audio(self):

        print(self.count)
        if self.count >= self.idle_tout:
            sys.exit(0)
        
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=1) 
            print("Say Something...")
            self.audio = self.r.listen(source)
            self.text = self.r.recognize_sphinx(self.audio)
            self.recognize_using_sphinx(self.text)
            
##            if "okay" in self.text:
##                self.recognize_using_sphinx(self.text)
##                self.count = 0
##            else:
##                self.count += 1
##                self.obtain_audio()
                
                
            

    def recognize_using_sphinx(self,text):
        try:
            print("Sphinx thinks you said '"+ text + "'")
            self.obtain_audio()

        except sr.UnkownValueError:
            print("Sphinx could not understand audio, please say something again.")
            self.obtain_audio()


Speech(0,3)

