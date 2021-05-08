from tkinter import *
import pandas
import random
Backg="#f7f7f7"

#loading data using panda
data=pandas.read_csv("data/flash_card- Sheet1.csv")
learn=data.to_dict(orient="records")

def next_card():
  global current_card,flip_time
  window.after_cancel(flip_time)
  current_card= random.choice(learn)
  print(current_card["English"])
  #for randering random word
  canvas.itemconfig(title,text="English",fill="black")
  canvas.itemconfig(words,text=current_card["English"],fill="black")
  flip_time = window.after(4000, flip)
  canvas.itemconfig(card_bg, image=cardf)
def flip():
  canvas.itemconfig(title, text="Hindi" ,fill="white")
  canvas.itemconfig(words, text=current_card["Hindi"],fill="white")
  canvas.itemconfig(card_bg,image=cardg)


window= Tk()
window.title("Word Catch")
window.config(padx=50,pady= 50,bg=Backg)
#window after  is excuting the commond after some dealy
flip_time = window.after(4000,flip)
#for layring a card on Background

canvas=Canvas(width=806,height=608)
cardf=PhotoImage(file="images/caba.png")
cardg=PhotoImage(file="images/re1.png")
#for showing image on background
card_bg=canvas.create_image(403,304, image=cardf)
title=canvas.create_text(403,150,text="", font=("Ariel",40,"italic"))
words=canvas.create_text(403,340,text="",font=("Ariel",60,"bold"))
canvas.config(bg=Backg ,highlightthickness=0)


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
