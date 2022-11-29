# Import
import datetime
import time
from pygame import mixer
import random

# Variabile
orar = [
"8:00:00",
"8:45:00",
"9:00:00",
"9:45:00",
"9:55:00",
"10:40:00",
"11:00:00",
"11:45:00",
"11:55:00",
"12:40:00",
"12:50:00",
"13:35:00",
"13:00:00",
"13:45:00",
"14:30:00"
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
random.shuffle(playlist)

# Intializarea mixer
mixer.init()

# Functii
def calculateTime(i:str):
    currentime = datetime.datetime.now()
    times = currentime.strftime('%H:%M:%S')
    times = times.split(":")
    i = i.split(":")
    x = int(times[0])*3600+int(times[1])*60+int(times[2])*1 
    y = int(i[0])*3600+int(i[1])*60+int(i[2])*1 
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

# For loop
for i in orar:
    sleepTime = calculateTime(i)
    if sleepTime != False:
        if i == orar[2]:
            time.sleep(sleepTime)
            sunet(10)
            playList(playListTime)
        else:
            time.sleep(sleepTime)
            sunet(10)
