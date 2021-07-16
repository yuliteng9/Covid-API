from tkinter import *

window = Tk()
window.title("rectangle and arc")

canvas = Canvas(window, width= 800, height=800)   
canvas.pack()

rec = canvas.create_rectangle(100,100,200,300)
arc = canvas.create_arc(100,100,200,300,start=0,extent=90,fill="purple")

canvas.config(bg="pink")
canvas.itemconfig(rec,fill="yellow")
canvas.itemconfig(arc,start=30,extent=180)
canvas.move(rec, 50,50)

window.mainloop()