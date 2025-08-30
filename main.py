# Code art, created by machineryman01.
from pyfiglet import Figlet
import time as t

word = ("Merdeka!", "Merdeka!!", "Merdeka!!", "Merdeka!!!", "Merdeka!!!!", "Merdeka!!!!!", "Merdeka!!!!!!", "Merdeka...")
font = Figlet(font='slant')
count_max = 7

def say_merdeka_7_times():
    num = 0
    while num <= count_max:
        num = num + 1
        print(font.renderText(word[num]))
        print(f"{num} times")
        t.sleep(1.30)
        
        # If reaching 7 times. Stops
        if num == count_max:
            break

# Call function
say_merdeka_7_times()
