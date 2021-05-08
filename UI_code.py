from tkinter import *
Backg="#f5f7b2"

window= Tk()
window.title("Word Catch")
window.config(padx=50,pady= 50,bg=Backg)
#for layring a card on Background

canvas=Canvas(width=920,height=680)
cardf=PhotoImage(file="images/cardfn.png")
canvas.create_image(460,340, image=cardf)
canvas.create_text(450,150,text="Hello", font=("Ariel",40,"italic"))
canvas.create_text(450,340,text="word",font=("Ariel",60,"bold"))
canvas.config(bg=Backg,highlightthickness=0)


canvas.grid(row=0,column=0,columnspan=2)

#Button

check_img=PhotoImage(file="images/chec1.png")
un_button=Button(image=check_img,highlightthickness=0)
un_button.grid(row=1,column=1)
cross_img=PhotoImage(file="images/wrong.png")
un_butt=Button(image=cross_img,highlightthickness=0)
un_butt.grid(row=1,column=0)


