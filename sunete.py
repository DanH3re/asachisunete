# Import
import datetime
import time
import csv
from pygame import mixer

# Variables
orar = [
"19:30:00",
"19:39:00", 
"19:39:20",
"19:40:00"
]

playlist = [
"001.mp3",
"002.mp3", 
"003.mp3",
"004.mp3",
"005.mp3",
"006.mp3",
"007.mp3",
"008.mp3"]
playListTime = 1140

# Mixer Init
mixer.init()

# Functions
def calculateTime(i:str):
    currentime = datetime.datetime.now()
    times = currentime.strftime('%H:%M:%S')
    times = times.split(":")
    i = i.split(":")
    x = int(times[0])*360 + int(times[1])*60 + int(times[2])*1 
    y = int(i[0])*360 + int(i[1])*60 + int(i[2])*1 
    if(x < y):
        return y-x
    else:
        return False

def sunet(sec:int):
        currentime = datetime.datetime.now()
        times = currentime.strftime('%H:%M:%S')
        print("[" + times + "]" + "A sunat.")
        mixer.music.load("30sec.mp3")
        mixer.music.play()
        time.sleep(sec)
        mixer.music.stop()
        mixer.music.unload()

def playList(sec:int):
    currentime = datetime.datetime.now()
    times = currentime.strftime('%H:%M:%S')
    print("[" + times + "]" + "Playlist.")
    mixer.music.load("imnul.mp3")
    for cantec in playlist:
        mixer.music.queue(cantec)
    mixer.music.play()
    time.sleep(sec)
    mixer.music.stop()

# Loop
for i in orar:
    sleepTime = calculateTime(i)
    if sleepTime != False:
        if i == orar[2]:
            time.sleep(sleepTime)
            sunet(10)
            playList(20)
        else:
            time.sleep(sleepTime)
            sunet(10)