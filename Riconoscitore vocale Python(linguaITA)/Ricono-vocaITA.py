import speech_recognition as sr

def inizio():
    try:
        Riconoscitorevoce = sr.Recognizer()
        print("Lingua ITALIANO")
        print("In ascolto")
        with sr.Microphone() as mic:
            Riconoscitorevoce.adjust_for_ambient_noise(mic)
            
            audio = Riconoscitorevoce.listen(mic)
            print("Ok! sto ora elaborando il messaggio!")
            
            text = Riconoscitorevoce.recognize_google(audio, language="it-IT")
            
            print(text)
                f = open('Scrittore.txt', 'a')
                f.write(text)
                f.write('\n')
                f.close()            
    except:
        print("Errore, non ho rilevato una voce, o è poco chiara o non è inglese")
inizio()
    
    
