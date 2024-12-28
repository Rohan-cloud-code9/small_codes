from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm():
    minutes = int(input("enter minutes after which you want to me to play your alarm -  "))
    seocnds = int(input("enter seconds after which you want to me to play your alarm -  "))
    timer = minutes*60 + seocnds
    time_elapsed = 0
    print(CLEAR)
    while True:
        
        if(time_elapsed < timer):
            time.sleep(1)
            time_elapsed += 1
            time_left = timer - time_elapsed
            if(time_left >= 60):
                minute_left = time_left//60
            else:
                minute_left = 0
            seconds_left = time_left - minute_left*60 #or time_left%60
            print(f"{CLEAR_AND_RETURN}{minute_left}:{seconds_left}")
        
        else:
            playsound("music.mp3")


alarm()