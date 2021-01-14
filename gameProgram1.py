from tkinter import *
from PIL import ImageTk, Image
import os
import random


attempts = 10
answer = random.randint(1, 99)

def check_answer():

    global attempts
    global text

    ##decreasing the number of attempts
    attempts -=1
    guess = int(entryWindow.get())

    if answer == guess:
        text.set("You win!!!!")
        imageWin = Image.open("D:\setOfStar.png")
        ##imageSize = imageWin.resize(30,30)
        ##imgWin = ImageTk.PhotoImage(imageWin)
        ##imgLabel = Label(window, image =imgWin).pack(side=BOTTOM)
        btn_check.pack_forget()

    elif attempts ==0:
        text.set("You are out of attempts!!!")
        btn_check.pack_forget()

    elif guess < answer:
        text.set("Not quite!!! You have " + str(attempts) + " attempts REMAINING - Go UP!!")

    elif guess > answer:
        text.set("Not yet!!! You have " + str(attempts) + " attempts REMAINING - Go DOWN!!")

    return

window = Tk()
window.title("Guessing The Number")
window.geometry("500x550")
##logo = PhotoImage(file = 'D:\star.png')
##window.iconphoto(FALSE, logo)

##top image
image1 = Image.open("D:\cat.png")
img = ImageTk.PhotoImage(image1)
imgLabel = Label(window, image =img).pack(side=TOP)

## where numbers will be entered
label = Label(window, text = "Guessing the number betweeen 1 & 99", font = "bold", bg = "pink")
label.pack()

##how entered numbers will look like
entryWindow = Entry(window, width=40, borderwidth=4, fg="#006400", cursor="heart", bg = "#FFE6EE")
entryWindow.pack()

## check button
btn_check = Button(window, text="check", command=check_answer, bg='#ffb3fe', font="bold")
btn_check.place(x=50, y=70)
btn_check.pack()

##quit button
btn_quit = Button(window, text="Quit", command=window.destroy, bg='#add8e6', font="bold")
btn_quit.pack()

##text below text bar
text = StringVar()
text.set("You have 10 attempts remaining! Good luck!")


guess_attempts = Label(window, textvariable=text)
guess_attempts.pack()

window.mainloop() ##what runs the class