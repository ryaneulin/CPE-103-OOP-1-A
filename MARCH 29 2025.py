from pygame.examples.scroll import scroll_view
from tkinter import *

window = Tk()
window.title("Using grid manager")
window.geometry("500x650+1150+150")


yscroll =Scrollbar(window)
yscroll.pack( side = RIGHT, fill = Y)
listbox = Listbox(window, yscrollcommand = yscroll.set)
listbox.pack( side = RIGHT, fill = BOTH, expand = TRUE)

yscroll.config(command = listbox.yview)

for i in range(1, 100):
    listbox.insert(END, i)



window.mainloop()