from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

class ObjectClick():
	def __init__(self,cordx, cordy, color):
		self.cordx = cordx
		self.cordy = cordy
		self.color = color


class Ball(ObjectClick):
	def __init__(self, cordx, cordy, color, radius):
		self.cordx = cordx
		self.cordy = cordy
		self.color = color
		self.radius = radius
	
	def click(event):
		print(event.x, event.y)
		
colors = ['red','orange','yellow','green','blue']
def new_ball(n):
	canv.delete(ALL)
	for i in range [n]:
		ball = Ball(rnd(100,700), rnd(100,500), choice(colors), rnd(30,50))
		canv.create_oval(ball.cordx - ball.radius,ball.cordy - ball.radius,ball.cordx + ball.radius,ball.cordy + ball.radius,fill = ball.color, width=0)
	root.after(rnd(100,700),new_ball)



new_ball(2)
canv.bind('<Button-1>', Ball.click)
mainloop()
