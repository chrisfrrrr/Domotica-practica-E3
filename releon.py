import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

#Controlando relay 13
GPIO.setup(23, GPIO.OUT)

while False:
    boton = int(input("Instrucción:"))
    if boton == 0:
        GPIO.output(23, GPIO.HIGH)
        break

GPIO.cleanup()