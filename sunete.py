# Import
import datetime
import time
from pygame import mixer
import random
from mutagen.mp3 import MP3


# Variabile
orar = [
"8:00:00",
"8:45:00",
"9:00:00",
"9:45:00",
"9:55:00",
"23:39:00",
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
        mixer.music.load("./muzica/sunet.mp3")
        mixer.music.play()
        time.sleep(sec)
        mixer.music.stop()
        mixer.music.unload()

def playList(sec:int):
    currentime = datetime.datetime.now()
    times = currentime.strftime('%H:%M:%S')
    playlistLength = 0
    print("[" + times + "]" + "Playlist.")
    mixer.music.load("./muzica/imnul.mp3")
    audio = MP3("./muzica/imnul.mp3")
    mixer.music.play()
    print("Cântă: Imnul")
    playlistLength = audio.info.length
    time.sleep(int(audio.info.length))
    mixer.music.unload()
    for cantec in playlist:
        audio = MP3("./muzica/" + cantec)
        if playlistLength + audio.info.length < sec:
            playlistLength = playlistLength + audio.info.length
            mixer.music.load("./muzica/" + cantec)
            mixer.music.play()
            print("Cântă: " + cantec)
            time.sleep(audio.info.length)
            mixer.music.unload()

# For loop
for i in orar:
    sleepTime = calculateTime(i)
    if sleepTime != False:
        if i == orar[5]:
            time.sleep(sleepTime)
            sunet(13)
            playList(playListTime)
        else:
            time.sleep(sleepTime)
            sunet(13)
