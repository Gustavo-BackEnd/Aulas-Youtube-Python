import pyttsx3

motor = pyttsx3.init()

#Fazer o computador falar o print
def computadorfala(mensagem):
    motor.say(mensagem)
    motor.runAndWait()

computadorfala('Desculpa eu te amo gatona')