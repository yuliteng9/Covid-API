from random import *
from tkinter import *

width = 500
height = 500

window = Tk()
window.geometry("" + str(width) + "x" + str(height))
window.title("Contact Tracing")

canvas = Canvas(window,width=width, height=height)
canvas.pack()

circle = canvas.create_oval(240, 240, 260, 260, fill="cyan")

def move_left(event):
    canvas.move(circle, -10, 0)
    check_collisions(circle, rectangles)

def move_right(event):
    canvas.move(circle, 10, 0)
    check_collisions(circle, rectangles)

def move_up(event):
    canvas.move(circle, 0, -10)
    check_collisions(circle, rectangles)

def move_down(event):
    canvas.move(circle, 0, 10)
    check_collisions(circle, rectangles)

canvas.bind_all("<Left>", move_left)
canvas.bind_all("<Right>", move_right)
canvas.bind_all("<Up>", move_up)
canvas.bind_all("<Down>", move_down)

def check_collision(shape1, shape2):
    c1 = canvas.coords(shape1)
    c2 = canvas.coords(shape2)
    c1x1 = c1[0]
    c1x2 = c1[2]
    c2x1 = c2[0]
    c2x2 = c2[2]
    c1y1 = c1[1]
    c1y2 = c1[3]
    c2y1 = c2[1]
    c2y2 = c2[3]
    if c1x1 <= c2x1 <= c1x2 or c1x1 <= c2x2 <= c1x2 or c2x1 <= c1x1 <= c2x2 or c2x1 <= c1x2 <= c2x2:
        if c1y1 <= c2y1 <= c1y2 or c1y1 <= c2y2 <= c1y2 or c2y1 <= c1y1 <= c2y2 or c2y1 <= c1y2 <= c2y2:
            print("collision between: " + str(shape1) + " and " +str(shape2))
            canvas.delete(str(shape2))
            rectangles.remove(shape2)
            if rectangles == []:
                random_rectangles(5, rectangles)

def check_collisions(shape, shapes):
    for s in shapes:
        check_collision(shape, s)

def random_rectangles(num, rectangle_list):
    for i in range(num):
        x1 = randint(0, width - 50)
        y1 = randint(0, height - 50)
        rect = canvas.create_rectangle(x1, y1, x1+50, y1+50, fill="red")
        rectangle_list.append(rect)

rectangles = []
random_rectangles(5, rectangles)

window.mainloop()