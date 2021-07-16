from tkinter import *
from random import *

window = Tk()
window.title("Rectangular Prism")

canvas = Canvas(window, width=1000, height=1000)
canvas.pack()

front = canvas.create_polygon(450, 450, 450, 250, 550, 250, 550, 450, fill='blue')
top = canvas.create_polygon(400, 200, 450, 250, 550, 250, 500, 200, fill="red")
left = canvas.create_polygon(450, 450, 400, 400, 400, 200, 450, 250, fill="yellow")
faces = [front, top, left]

colour_list = ["red", "yellow", "lightblue", "green", "orange", "darkblue","purple", "pink", "cyan", "lime", "magenta"]

def change_colors(event):
    for face in faces:
        num = randint(0, len(colour_list)-1)
        canvas.itemconfig(face, fill=colour_list[num])

def move_left(event):
    for face in faces:
        canvas.move(face, -10, 0)

def move_right(event):
    for face in faces:
        canvas.move(face, 10, 0)

def move_up(event):
    for face in faces:
        canvas.move(face, 0, -10)

def move_down(event):
    for face in faces:
        canvas.move(face, 0, 10)


canvas.bind_all("<Left>", move_left)
canvas.bind_all("<Right>", move_right)
canvas.bind_all("<Up>", move_up)
canvas.bind_all("<Down>", move_down)
canvas.bind_all("c", change_colors)

window.mainloop()