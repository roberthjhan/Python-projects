import pyautogui
from PyLyrics import *
import time

artist = 'Pinkfong'
song = "Baby Shark"

text = (PyLyrics.getLyrics(artist, song))

def spam_song (text):
    time.sleep(10) # You get 10s to put your cursor over the input you want to spam
    pyautogui.write("Have you heard the song, " + song + "?")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write("It goes like this:")
    pyautogui.press("enter")
    for x in text.split():
        pyautogui.write(x)
        pyautogui.press("enter")

spam_song(text)