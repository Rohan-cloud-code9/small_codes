import curses 
import time
import random
from curses import wrapper

def start_screen(screen):
    screen.clear()
    screen.addstr("Welcome to Speed Typing Test!")
    screen.addstr("\nPress any key to start")
    screen.refresh()
    screen.getkey()



def display_text(screen , target, current, wpm):
    screen.addstr(target)
    screen.addstr(1, 0, f"WPM : {wpm}")
    for i, char in enumerate(current):
        color = curses.color_pair(1)
        if char != target[i]:
            color = curses.color_pair(2)
        screen.addstr(0, i, char, color)
    
def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(screen):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    screen.nodelay(True)

    while True:
        time_eclapsed = max(time.time() - start_time , 1)
        cpm = len(current_text)/(time_eclapsed/60)
        wpm = round(cpm/5)
        screen.clear() #it clears the screen and also add the target text and then the word form current text
        
        display_text(screen, target_text, current_text, wpm)
        screen.refresh() 
        if "".join(current_text) == target_text:
            screen.nodelay(False)
            break
        try:
            key = screen.getkey()
        except:
            continue
        
        
        
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
    
    
    
    

    
def main(screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(screen)
    while True:
        wpm_test(screen)
        screen.addstr(2, 0, "You completed the test!. Press any key to continue....")
        key = screen.getkey()
        if ord(key) == 27:
            break
        
wrapper(main)

