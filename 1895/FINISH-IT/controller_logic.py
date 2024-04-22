import RPi.GPIO as GPIO
import time
import random

            #print winning screen to lcd

#def game1():#dance recognition

#def game2():# voice recognition
def main():


    score = 0
    time = 30
    valid = True

    num = random.randint(0,2)

    while valid:
        if num == 0:
            if game1(time):
                score += 1
                #updatelcd()
            else:
                valid = False
        elif num == 1:
            if game2(time):
                score += 1
                #updatelcd()
            else:
                valid = False
        elif num == 2:
            if game3(time):
                score += 1
                #updatelcd()
            else:
                valid = False

        if score % 5 == 0:
            time = time - 5
        
        if time == 0:
            time = 5
    


def getArtist(promptNum,check,type):#function containing fixed library of prompts for game 3
    #if check is true, then the function will return T/F else return strings

    #the format of the prompt will be question, ans1, ans2, ans3 (semicolons signal next segment and colon signals end)
    questions = songs = [
        "Goosebumps by ___;*Travis Scott;Ed Sheeran;Lil Nas X",
        "Shape of You by ___;*Ed Sheeran;Post Malone;Shawn Mendes",
        "Blinding Lights by ___;*The Weeknd;Billie Eilish;Lewis Capaldi",
        "Old Town Road by ___;*Lil Nas X;Lewis Capaldi;Shawn Mendes",
        "Dance Monkey by ___;*Tones and I;Billie Eilish;Post Malone",
        "Someone You Loved by ___;*Lewis Capaldi;The Weeknd;Shawn Mendes",
        "Bad Guy by ___;*Billie Eilish;Tones and I;Travis Scott",
        "Sunflower by ___;*Post Malone;The Weeknd;Shawn Mendes",
        "Senorita by ___;*Shawn Mendes;Camila Cabello;Ed Sheeran",
        "Stressed Out by ___;*Twenty One Pilots;Lewis Capaldi;Tones and I"
        ]

    cor = 0
    if(check == False):
        prompt = questions[promptNum]
        val = []
        for char in prompt:
            if char == ';':
                break
            
            val.append(char)

        
        return ''.join(val)
            
    else:
        parsed = parser(questions[promptNum])
       
        for i in range(3):
            curr = parsed[i]
            if curr[0] == '*':
                cor = i
                break
        
        if cor+1 == type:
            return True
        else:
            return False
            


def parser(sentence):
    
    x = 0
    k = 0
    info = []
    for i in range(len(sentence)):
        x = x + 1

        if sentence[i] == ';':
            info.append(sentence[:x-1])
            x=0
            k = k + 1
        
    return info  

def set_buttons():
    GPIO.setmode(GPIO.BCM)
    
    ANS1 = 5
    ANS2 = 6
    ANS3 = 26

    GPIO.setup(ANS1,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(ANS2,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(ANS3,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

def set_sound():
    GPIO.setmode(GPIO.BCM)
    
    success = 16
    fail = 24
    
    GPIO.setup(success,GPIO.OUT)
    GPIO.setup(fail,GPIO.OUT)
    
def game3(x):
    #x dictates how long the player has to answer, the time will decrease as the player answers rounds correctly
    
    set_buttons()#configure GPIO
    
    num = random.randint(0,9)
    
    questions = getArtist(num,False,0)
    
    print(questions)#debug


    
    counter = 0
    
    while counter < x:
        
        x = x - 1

        ANS1 = GPIO.input(5)
        ANS2 = GPIO.input(6)
        ANS3 = GPIO.input(26)
        
        if ANS1 == 1 or ANS2 == 1 or ANS3 == 1:
            print("ans detected")
            break
        
        print(x) #debug
        
        time.sleep(1)
    
    if((ANS1 == 1 and ANS2 == 1) or (ANS1 == 1 and ANS3 == 1) or (ANS2 == 1 and ANS3 == 1) or (ANS1 == 0 and ANS2 == 0 and ANS3 == 0) or (ANS1 == 1 and ANS2 == 1 and ANS3 == 1)): #error checking
        print("Wrong")
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

    
    result = getArtist(num,True,GPIO_res)
    
    GPIO.cleanup()
    
    return result
    

def res_sound(stat):
    
    set_sound()
    
    if stat:
        GPIO.output(16,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(16,GPIO.LOW)
    else:
        GPIO.output(24,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(24,GPIO.LOW)
        
def main():
    
    res = game3(10)
    if res:
        res_sound(True)
    else:
        res_sound(False)

if __name__ == "__main__":
    main()
    
        

