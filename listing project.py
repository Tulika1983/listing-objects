from tkinter import *
import random

root = Tk()
root.title("Listing Objects")
root.geometry("400x400")
root.configure(background = "yellow")

List1 = ['Books , pencils, pens , erasers, tiffin.']

label1 = Label(root)
label2 = Label(root)

def randomlist():
    randomlist = random.sample(range(0,3),1)
    label1["text"] = "Listed Items :" + str(List1)
    label2["text"] = "Put item no : " + str(randomlist) + "In bag"


btn = Button(root , text = "Which item to put in bag", command = randomlist ,bg = "blue" , fg = "black")
btn.place(relx = 0.5,rely = 0.4, anchor = CENTER)

label1.place(relx = 0.5,rely = 0.5, anchor = CENTER)
label2.place(relx = 0.5,rely = 0.6, anchor = CENTER)

root.mainloop()