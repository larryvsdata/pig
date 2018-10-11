#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:52:55 2018

@author: ermanbekaroglu
"""
import speech_recognition as sr

class pigSpeech():
    
    def __init__(self):
        self.pigSay="Say something!"
        self.sphinxThinks="Sphinx thinks you said:  "
        self.sphinxUnable="Unable to understand. "
        self.r=sr.Recognizer()
        
    
    def translateToPig(self,sentence):
        lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
        sentence = sentence.split()
        
        for k in range(len(sentence)):
                i = sentence[k]
                if i[0] in ['a', 'e', 'i', 'o', 'u']:
                        sentence[k] = i+'ay'
                elif self.getFirstLastChar(i) in lst:
                        sentence[k] = i[2:]+i[:2]+'ay'
                elif i.isalpha() == False:
                        sentence[k] = i
                else:
                        sentence[k] = i[1:]+i[0]+'ay'
        return ' '.join(sentence)
        
        
        
    def getFirstLastChar(self,str):
        return str[0]+str[1]
    
    def getTheSpeechandInterpret(self):
        with sr.Microphone() as source:
            print(self.translateToPig(self.pigSay))
            audio=self.r.listen(source)
            
            try:
                print(self.translateToPig(self.sphinxThinks)+self.translateToPig(self.r.recognize_sphinx(audio)))
            except:
                print(self.translateToPig(self.sphinxUnable))
        
    
if __name__ == "__main__":

    pigTranslator= pigSpeech()
    aString="Hey man. How are you today?"
    pigTranslator.getTheSpeechandInterpret()