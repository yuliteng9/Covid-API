from tkinter import *

window = Tk()
window.title("Rectangular Prism")

canvas = Canvas(window, width= 400, height=400)   #the height of canvas can't be too big, or the button can't be shown
canvas.pack()

top_left_x=200
top_left_y=100
top_size=50
front_size_x=100
front_size_y=200

top = canvas.create_polygon(top_left_x, top_left_y, top_left_x+front_size_x, top_left_y,
                              top_left_x+top_size, top_left_y-top_size, top_left_x-top_size, top_left_y-top_size, fill='blue')
front = canvas.create_polygon(top_left_x, top_left_y, top_left_x+front_size_x, top_left_y,
                              top_left_x+front_size_x, top_left_y+front_size_y,top_left_x, top_left_y+front_size_y,fill="red")
left = canvas.create_polygon(top_left_x, top_left_y, top_left_x, top_left_y+front_size_y,
                            top_left_x-top_size,  top_left_y-top_size+front_size_y, top_left_x-top_size, top_left_y-top_size, fill="yellow")
faces = [front, top, left]

colour_entry = Entry(window, text="")
colour_entry.pack()

def change_front_colour():
    new_colour=colour_entry.get()
    canvas.itemconfig(front, fill=new_colour)

def change_left_colour():
    new_colour=colour_entry.get()
    canvas.itemconfig(left, fill=new_colour)

def change_top_colour():
    new_colour=colour_entry.get()
    canvas.itemconfig(top, fill=new_colour)

button1 = Button(window, text="Change Front Colour", command=change_front_colour)
button1.pack()
button2 = Button(window, text="Change Left Colour", command=change_left_colour)
button2.pack()
button3 = Button(window, text="Change Top Colour", command=change_top_colour)
button3.pack()
#colour_list = ["red", "yellow", "lightblue", "green", "orange", "darkblue","purple", "pink", "cyan", "lime", "magenta"]

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

window.mainloop()