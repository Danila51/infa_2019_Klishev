# DONE:
# Заккоментировал кривоватое столкновение шаровd

from tkinter import *
from random import randrange as rnd, choice
import numpy as np 
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'black', 'brown', 'pink']
score = 0  # Переменная счета
model = canv.create_text(50, 50, text=score, font="Verdana 14")  # Объект счета


def new_ball():  # Модуль создания шара
    ball = {}
    ball['x'] = rnd(100, 700)
    ball['y'] = rnd(100, 500)
    ball['r'] = rnd(60, 90)
    ball['dx'] = rnd(-10, 10)
    ball['dy'] = rnd(-10, 10)
    ball['model'] = canv.create_oval(ball['x'] - ball['r'], ball['y'] - ball['r'], ball['x'] + ball['r'],
                                     ball['y'] + ball['r'],
                                     fill=choice(colors), width=0)
    return ball


def move_ball(ball):  # Модуль движения
    
    if ball['x'] <= ball['r'] or ball['x'] >= 800 - ball['r']:  # Подмодуль отражения от стены
        ball['dx'] = - ball['dx']
    if ball['y'] <= ball['r'] or ball['y'] >= 600 - ball['r']:
        ball['dy'] = - ball['dy']
    
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']
    canv.move(ball['model'], ball['dx'], ball['dy'])
    

def update():  # Изменение времени
    global b1, b2, b3
    """
    if ((b1['x'] - b2['x'])**2 + (b1['y']-b2['y'])**2)**(1/2) <= b1['r'] + b2['r']:
        b1['dx'] = rnd(-10, 10)
        b1['dy'] = rnd(-10, 10)
        b2['dx'] = rnd(-10, 10)
        b2['dy'] = rnd(-10, 10)
    if ((b1['x'] - b3['x'])**2 + (b1['y']-b3['y'])**2)**(1/2) <= b1['r'] + b3['r']:
        b1['dx'] = rnd(-10, 10)
        b1['dy'] = rnd(-10, 10)
        b3['dx'] = rnd(-10, 10)
        b3['dy'] = rnd(-10, 10)
    if ((b3['x'] - b2['x'])**2 + (b3['y']-b2['y'])**2)**(1/2) <= b3['r'] + b2['r']:
        b3['dx'] = rnd(-10, 10)
        b3['dy'] = rnd(-10, 10)
        b2['dx'] = rnd(-10, 10)
        b2['dy'] = rnd(-10, 10)
    """
    move_ball(b1)
    move_ball(b2)
    move_ball(b3)
    root.after(20, update)


def click(event):  # Модуль изменеия счета и пересоздания шариков
    global score, b1, b2, b3, model
    if ((b1['x'] - event.x) ** 2 + (b1['y'] - event.y) ** 2) ** (1 / 2) <= b1['r']:
        canv.delete(b1['model'])
        b1 = new_ball()

        score += 1
        canv.delete(model)
        model = canv.create_text(50, 50, text=score, font="Verdana 14")

    if ((b2['x'] - event.x) ** 2 + (b2['y'] - event.y) ** 2) ** (1 / 2) <= b2['r']:
        canv.delete(b2['model'])
        b2 = new_ball()

        score += 1
        canv.delete(model)
        model = canv.create_text(50, 50, text=score, font="Verdana 14")

    if ((b3['x'] - event.x) ** 2 + (b3['y'] - event.y) ** 2) ** (1 / 2) <= b3['r']:
        canv.delete(b3['model'])
        b3 = new_ball()

        score += 1
        canv.delete(model)
        model = canv.create_text(50, 50, text=score, font="Verdana 14")


b1 = new_ball()
b2 = new_ball()
b3 = new_ball()
update()
canv.bind('<Button-1>', click)
mainloop()
