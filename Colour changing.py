
from tkinter import *
import random

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {"colour" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1",
                          "deep pink","cyan"]}

def bg_change():
    random_no =random.randint(0,7)
    print(dictionary["colour"][random_no])
    root.configure(background = dictionary["colour"][random_no])
   
btn = Button(root,text = "click me", command = bg_change)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

root.mainloop()

"""
Created on Wed Oct 13 14:09:22 2021

@author: Admin
"""

