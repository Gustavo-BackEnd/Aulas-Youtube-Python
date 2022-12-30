import speech_recognition as speech

#Fazer o computador ouvir o que eu falo e por no print de cima
def computadorouve():
    reconhecer = speech.Recognizer()

    try:
        with speech.Microphone() as microfone:
            print('Pode falar agora')
            audio = reconhecer.listen(microfone)
            texto = reconhecer.recognize_google (audio, language='pt-BR')
            print(texto)
            return texto.lower()

    except:
        pass

computadorouve()