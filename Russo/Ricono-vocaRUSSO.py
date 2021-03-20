import speech_recognition as sr
import time

def inizio():
    try:
        Riconoscitorevoce = sr.Recognizer()
        print("Lingua RUSSO, il russo non può essere scritto su un file txt come le altre lingue(non so il perchè)")
        print("In ascolto")
        with sr.Microphone() as mic:
            Riconoscitorevoce.adjust_for_ambient_noise(mic)
            
            audio = Riconoscitorevoce.listen(mic)
            print("Ok! sto ora elaborando il messaggio!")
            
            text = Riconoscitorevoce.recognize_google(audio, language="ru-RU")
            
            print(text)
            time.sleep(10)
            #f = open('Scrittore.txt', 'a')
            #f.write(text)
            #f.write('\n')
            #f.close()            
    except:
        print("Errore, non ho rilevato una voce, o è poco chiara")
inizio()
    
    
