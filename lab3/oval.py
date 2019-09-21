from graph import *

windowSize(2000,2000)
canvasSize(2000,2000)
def leps(a,b,x0,y0):
	x=a
	y=0
	tet=[(x0+a,y0)]
	for i in range(2*a):
		x-=1
		y=((1-x**2/(a**2))*b**2)**0.5
		tet.append((x+x0,y+y0))
	for i in range(2*a):
		x+=1
		y=-(((1-x**2/(a**2))*b**2)**0.5)
		tet.append((x+x0,y+y0))
	polygon(tet)
penColor("black")
brushColor("black")
leps(100,100,300,300)
run()
