# Import
import datetime
import time
from pygame import mixer
import random
from mutagen.mp3 import MP3
from os.path import isfile, join


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
"13:45:00",
"14:30:00"
]

directory = "C:/Users/MECC/Desktop/Senatul Elevilor/python sunete"
imnulPath = directory + "/sunete/imnul.mp3"
sunetPath = directory + "/sunete/sunet-christmas.mp3"
muzicaPath = directory + "/muzica/"

playListTime = 1140


# Intializarea mixer
mixer.init(devicename="Наушники (Realtek(R) Audio)")

# Functii
def calculateInterval(i:str,j:str):
    j = j.split(":")
    i = i.split(":")
    x = int(j[0])*3600+int(j[1])*60+int(j[2])*1 
    y = int(i[0])*3600+int(i[1])*60+int(i[2])*1 
    return x-y
    
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

def sunet():
        currentime = datetime.datetime.now()
        times = currentime.strftime('%H:%M:%S')
        print("[" + times + "]" + "A sunat.")
        audio = MP3(sunetPath)
        mixer.music.load(sunetPath)
        mixer.music.play()
        time.sleep(audio.info.length)
        mixer.music.stop()
        mixer.music.unload()

def playList(sec:int):
    from os import listdir
    playlist = [f for f in listdir(muzicaPath) if isfile(join(muzicaPath, f))]
    random.shuffle(playlist)
    currentime = datetime.datetime.now()
    times = currentime.strftime('%H:%M:%S')
    playlistLength = 0
    print("[" + times + "]" + "Playlist.")
    audio = MP3(imnulPath)
    playlistLength = audio.info.length
    for cantec in playlist:
        from os import listdir
        songLength = audio.info.length
        if playlistLength + songLength < sec:
            playlistLength = playlistLength + songLength
            mixer.music.load(muzicaPath + cantec)
            mixer.music.play()
            print("Cântă: " + cantec)
            time.sleep(songLength)
            mixer.music.stop()
            mixer.music.unload()

# For loop
for i in range(0, len(orar)):
    sleepTime = calculateTime(orar[i])
    if sleepTime != False:
            time.sleep(sleepTime)
            sunet()
            if i+1 > len(orar)-1 and i % 2 != 0:
                Ptime = calculateInterval(orar[i], orar[i+1])-60
                if i != 5:
                    playList(Ptime)
                else:
                    mixer.music.load(imnulPath)
                    mixer.music.play()
                    print("Cântă: Imnul")
                    audio = MP3(imnulPath)
                    time.sleep(audio.info.length)
                    mixer.music.unload()
                    playList(Ptime)