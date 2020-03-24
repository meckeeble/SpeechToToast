import speech_recognition as sr

def speechInput():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        #I'm using a very cheap mic, this was necessary
        print("calibrating mic...")
        r.adjust_for_ambient_noise(source, duration = 5)
    
    with sr.Microphone() as source:
    
        key = input("press enter to send your message \n")
        while key:
            key = input("press enter to begin your message")
        print("listening...")
        audio = r.listen(source)
        print("listening concluded")
        try:
            
            text = r.recognize_google(audio, language="en-gb" ) #set to British English 
            return '{}'.format(text)
        except:
            return ""
        

def speechFromAudio():
    r = sr.Recognizer()
    with sr.WavFile("dinner.wav") as source:
        audio = r.record(source)
        
    try:
        print("Transcription: "+r.recognize_google(audio))
    except LookupError:
        print("failed")