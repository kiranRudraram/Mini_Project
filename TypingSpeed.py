#importing all required libraries
#tkinter is a GUI library
import tkinter as tk
import random
from tkinter import messagebox
from tkinter.font import Font
import pygame
from pygame import mixer
from PIL import ImageTk, Image

#collection of words
words = ['Mobile', 'Paraphernalia', 'Indict', 'Laptop', 'Liquefy',  'Hyderabad', 'computer', 'Mango', 'Apple', 'samsung', 'Google', 'Microsoft', 'Lenovo',
         'python', 'Java', 'message', 'Onomatopoeia', 'Android', 'gmail', 'email', 'Playwright', 'Albeit', 'Appease', 'Bemused', 'Contrived', 'Fuchsia', 'Minuscule',
         'Colloquial', 'Conundrum', 'Dystopia', 'Egregious', 'Fortuitous', 'Incongruous', 'Nauseous', 'Obsolete', 'Vernacular' , 'Ingenious', 'Sacrilegious',
         'suburban', 'assuming', 'obstinance', 'foramens', 'Nauseous', 'Dilate', 'Orangutan', 'Mischievous', 'Gubernatorial', 'Acquiesce', 'Conscientious']


#function for title sliding effect
def labelSlider():
    global count, sliderWord
    text = "Typing Speed Increaser Game"
    if (count >= len(text)):
        count = 0
        sliderWord = ''
    sliderWord += text[count]
    count += 1
    fontLabel.configure(text=sliderWord)
    fontLabel.after(150, labelSlider)


def reminder():
    global load4, image4, render4, img4
    open_window = tk.Toplevel(root)
    open_window.title('Intro')
    open_window.geometry('512x326+400+100')
    open_window.resizable(0, 0)

    load4 = Image.open('keyboard.jpg')
    image4 = load4.resize((512, 326), Image.ANTIALIAS)
    render4 = ImageTk.PhotoImage(image4)
    img4 = tk.Label(open_window, image=render4)
    img4.place(x=0, y=0)

pygame.init()

def playMusic():
    # music
    mixer.music.load('bg.mp3')
    mixer.music.play(-1)

def stopMusic():
    mixer.music.stop()

def startGame(event):
    global score, miss

    if (timeleft == 30):
        time()
    gamePlayLabel.configure(text='')
    if (wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelcount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, tk.END)


def time():
    global timeleft, score, miss
    if (timeleft >= 11):
        pass
    else:
        timeLabelcount.configure(fg='red', font=('airal', 30, 'italic bold'))
    if (timeleft > 0):
        timeleft -= 1
        timeLabelcount.configure(text=timeleft)
        timeLabelcount.after(1000, time)
    else:
        last_window = tk.Toplevel(root)
        last_window.title('Game over!!')
        last_window.geometry('800x600+400+100')
        last_window.resizable(0, 0)

        load3 = Image.open('last.jpg')
        image3 = load3.resize((796, 598), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(image3)
        img3 = tk.Label(last_window, image=render3)
        img3.place(x=0, y=0)



        output_label = tk.Label(last_window,text='Hit = {} \n Miss = {} \nTotal Score = {}'.format(score, miss, score - miss),
                                font=('Castellar', 25, 'italic bold'), bg='#EEEEEE', fg='red')
        output_label.place(x=250, y=250)

        rr = messagebox.askretrycancel('Notification', 'For Play Again Hit Retry', parent=last_window)
        if (rr == True):
            score = 0
            timeleft = 30
            miss = 0
            timeLabelcount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelcount.configure(text=score)
            gamePlayLabel.configure(text='Type Word \n & \nHit Enter')
            last_window.destroy()
        else:
            last_window.destroy()
            root.destroy()




####### Root Method #######
root = tk.Tk()
root.geometry('800x600+400+100')
root.resizable(False, False)

load = Image.open('bg.jpg')
image = load.resize((850, 600), Image.ANTIALIAS)
render = ImageTk.PhotoImage(image)
img = tk.Label(root, image=render)
img.place(x=0, y=0)


root.wm_title('Typing Speed Increase Game')
root.iconbitmap('typingicon.ico')

score = 0
timeleft = 30
count = 0
sliderWord = ''
miss = -1

#defining font
bigFont = Font(family="Times", size=26, weight="bold", slant="roman", underline=1)
##### Label Method #####
fontLabel = tk.Label(root, text="", font=bigFont, bg='#F6F6F6', fg="#D3212D",  width=37)
fontLabel.place(x=15, y=25)
labelSlider()

random.shuffle(words)
wordLabel = tk.Label(root, text=words[0], font=('Helvetica', 35, 'bold'))
wordLabel.place(x=310, y=250)

scoreLabel = tk.Label(root, text='Your Score : ', font=('Helvetica', 24, 'bold'), fg='blue')
scoreLabel.place(x=30, y=130)

scoreLabelcount = tk.Label(root, text=score, font=('Helvetica', 24, 'bold'), fg='green')
scoreLabelcount.place(x=80, y=190)

timeLabel = tk.Label(root, text='Time Left : ', font=('Helvetica', 24, 'bold'), fg='blue')
timeLabel.place(x=550, y=130)

timeLabelcount = tk.Label(root, text=timeleft, font=('Helvetica', 24, 'bold'), fg='green')
timeLabelcount.place(x=600, y=190)

gamePlayLabel = tk.Label(root, text='Hit Enter \n to \nStart the game', font=('Helvetica', 20, 'italic bold'), bg='#F6F6F6', fg='red')
gamePlayLabel.place(x=360, y=420)

btn = tk.Button(root, text="Advice", command=reminder)
btn.place(x=700, y=560)


play_music = tk.PhotoImage(file='play.png')
play_label = tk.Label(image=play_music)
play_btn = tk.Button(root, image=play_music, command=playMusic, borderwidth=0)
play_btn.place(x=5, y=540)



stop_music = tk.PhotoImage(file='mute.png')
stop_label = tk.Label(image=stop_music)
stop_btn = tk.Button(root, image=stop_music, command=stopMusic, borderwidth=0)
stop_btn.place(x=60, y=540)




###### Entry Method ######

wordEntry = tk.Entry(root, font=('airal', 28, 'italic bold'), bd=8, justify='center')
wordEntry.place(x=210, y=340)
wordEntry.focus_set()
############################################################
root.bind('<Return>', startGame)



root.mainloop()
