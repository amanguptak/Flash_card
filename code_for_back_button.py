from tkinter import *
import pandas
import random
import time
Backg="#f7f7f7"

#loading data using panda
data=pandas.read_csv("data/flash_card- Sheet1.csv")
learn=data.to_dict(orient="records")
print((learn[195]))
ind=0
value=[]
str=0

def next_card():
  global current_card,flip_time,count,str
  window.after_cancel(flip_time)

  current_card= random.choice(learn)

  global ind
  #for storing the index number of current card

  ind = learn.index(current_card)
  value.append(ind)
  print("vlue hau",value)

  #for randering random word
  canvas.itemconfig(title,text="English",fill="black")
  canvas.itemconfig(words,text=current_card["English"],fill="black")
  flip_time = window.after(5000, flip)
  canvas.itemconfig(card_bg, image=cardf)

  #reintialize value of str
  str=0

def flip():
  canvas.itemconfig(title, text="Hindi" ,fill="white")
  canvas.itemconfig(words, text=current_card["Hindi"],fill="white")
  canvas.itemconfig(card_bg,image=cardg)

#for back button 
def back():
  global flip_time,flip_time2,str
  window.after_cancel(flip_time)
  window.after_cancel(flip_time2)


  #for incrementing the value of str
  str+=1
  print("achha",str)
  if (len(value) - str)>=0:
   pre = learn[value[len(value) - str]]
   canvas.itemconfig(title, text="English", fill="black")
   canvas.itemconfig(words, text=pre["English"], fill="black")
   flip_time = window.after(3000, flip2)
   canvas.itemconfig(card_bg, image=cardf)

  else:
    print("you reached at end")


#for back button flip
def flip2():

  try:


    pre = learn[value[len(value) - str]]

    canvas.itemconfig(title, text="Hindi" ,fill="white")
    canvas.itemconfig(words, text=pre["Hindi"],fill="white")
    canvas.itemconfig(card_bg,image=cardg)
  except IndexError:
    print("this index is not avaliable")



window= Tk()
window.title("Word Catch by Aman Eagleax")
window.config(padx=50,pady= 50,bg=Backg)
#window after  is excuting the commond after some dealy
flip_time = window.after(5000,flip)
flip_time2 = window.after(4000,flip2)
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
un_butt=Button(image=cross_img,highlightthickness=0,command=back)
un_butt.grid(row=1,column=0)


next_card()








window.mainloop()
