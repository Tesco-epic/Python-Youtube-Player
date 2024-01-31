from easygui import *
from tkinter import *
import pafy
import vlc
import time

filename = "NULLL"
media = vlc.Media(filename)

url = "https://www.youtube.com/watch?v=IetJ8URgg5c"

length = 0
hours = 0
mins = 0
sec = 0
lengthlabel = Label(text="0")
best= 0
window = Tk()

inputtxt = Text(window, height=1, width = 50)


media_player = vlc.MediaPlayer()

def geturl():
    global url
    global media
    global best
    url = inputtxt.get(1.0, "end-1c")
    video = pafy.new(url)
    best = video.getbest()
    mda = vlc.MediaPlayer(best.url)
    media_player.stop()
    mda.play()

def browser():
    global filename
    filename = fileopenbox()
    media = vlc.Media(filename)
    media_player.set_media(media)
    

def playbutton():
    global length
    global lengthlabel
    global mins
    global sec
    global hours
    media_player.play()
    length = media_player.get_length()
    length = length / 1000
    mins = round(length / 60)
    sec = length - mins
    hours = round(length / 3600)
    lengthlabel.config(text = "Hours: " + str(hours) + "Minuets: " + str(mins) + "Seconds: " + str(sec))
    
    

def stopbutton():
    media_player.stop()




inputtxt.pack()
getb = Button(text="Play youtube URL", command=geturl)
brwsbutton = Button(text="Browse", command=browser)
plybutton = Button(text="Play", command=playbutton)
stpbutton = Button(text="Stop", command=stopbutton)
lengthlabel.pack()

getb.pack()
stpbutton.pack()
brwsbutton.pack()
plybutton.pack()
window.mainloop()




