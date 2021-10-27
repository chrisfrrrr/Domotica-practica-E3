import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Trigger = 10
Echo = 12
GPIO.setup(Trigger,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
print ("Sensor Ultrasonico") 
try:
        while True:
                GPIO.output(Trigger,False)
                time.sleep(0.5)
                GPIO.output(Trigger,True)
                time.sleep(0.00001)
                GPIO.output(Trigger,False)
                inicio=time.time()
                while GPIO.input(Echo)==0:
                        inicio=time.time()
                while GPIO.input(Echo)==1:
                        final=time.time()
                t_transcurrido=final-inicio
                distancia=t_transcurrido*34000
                distancia=distancia/2
                if distancia < 45:
                        GPIO.setmode(GPIO.BOARD)
                        GPIO.setwarnings(False)
                        GPIO.setup(40, GPIO.OUT)
                        GPIO.output(40,1)
                else:
                        GPIO.setmode(GPIO.BOARD)
                        GPIO.setwarnings(False)
                        GPIO.setup(40, GPIO.OUT)
                        GPIO.output(40,0)
except KeyBoardInterrupt:
        GPIO.cleanup()
