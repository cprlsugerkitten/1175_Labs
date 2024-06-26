import RPi.GPIO as GPIO
import time
import random

def setGPIO():
    GPIO.setmode(GPIO.BCM)
    
    ANS1 = 17
    ANS2 = 27
    ANS3 = 22

    GPIO.setup(ANS1,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(ANS2,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(ANS3,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    
def game3(x):
    #x dictates how long the player has to answer, the time will decrease as the player answers rounds correctly
    
    setGPIO()#configure GPIO
    
    num = random.randint(0,49)
    
    questions = getArtist(num,False,0)
    
    counter = 0
    
    while counter < x:
        ANS1 = GPIO.input(17)
        ANS2 = GPIO.input(27)
        ANS3 = GPIO.input(22)
        if ANS1 == 1 or ANS2 == 1 or ANS3 == 1:
            break
    
    if((ANS1 == 1 and ANS2 == 1) or (ANS1 == 1 and ANS3 == 1) or (ANS2 == 1 and ANS3 == 1) or (ANS1 == 0 and ANS2 == 0 and ANS3 == 0) or (ANS1 == 1 and ANS2 == 1 and ANS3 == 1)): #error checking
        return False
    else:
        if(ANS1 == 1):
            print("ANS1 was chosen")
            GPIO_res = 1
        elif(ANS2 == 1):
            print("ANS2 was chosen")
            GPIO_res = 2
        else:
            print("ANS3 was chosen")
            GPIO_res = 3

    GPIO.cleanup()