from tkinter import *
import pandas
import random
Backg="#f5f7b2"

#loading data using panda
data=pandas.read_csv("data/flash_card- Sheet1.csv")
learn=data.to_dict(orient="records")

def next_card():
  current_card= random.choice(learn)
  print(current_card["English"])
  #for randering random word
  canvas.itemconfig(title,text="English")
  canvas.itemconfig(words,text=current_card["English"])

window= Tk()
window.title("Word Catch")
window.config(padx=50,pady= 50,bg=Backg)
#for layring a card on Background

canvas=Canvas(width=920,height=680)
cardf=PhotoImage(file="images/cardfn.png")
#for showing image on background
canvas.create_image(460,340, image=cardf)
title=canvas.create_text(450,150,text="", font=("Ariel",40,"italic"))
words=canvas.create_text(450,340,text="",font=("Ariel",60,"bold"))
canvas.config(bg=Backg,highlightthickness=0)


canvas.grid(row=0,column=0,columnspan=2)

#Button
check_img=PhotoImage(file="images/chec1.png")
un_button=Button(image=check_img,highlightthickness=0,command=next_card)
un_button.grid(row=1,column=1)
cross_img=PhotoImage(file="images/wrong.png")
un_butt=Button(image=cross_img,highlightthickness=0,command=next_card)
un_butt.grid(row=1,column=0)


next_card()








window.mainloop()
