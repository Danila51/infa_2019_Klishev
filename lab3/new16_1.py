from graph import *

windowSize(900, 1400)
canvasSize(792, 1200)


#  возвращает эллипс
# a-большая полуось,b-малая
def leps(a, b, x0, y0):
	x = a
	p = [(x0 + a, y0)]
	for i in range(2 * a):
		x -= 1
		y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
		p.append((x + x0, y + y0))
	for i in range(2 * a):
		x += 1
		y = -(((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
		p.append((x + x0, y + y0))
	obj=polygon(p)
	return obj


# функция рисует область перекрытия овала прямоуголником
# f и g границы прямоугольника по оси y
def leps2(a, b, x0, y0, f, g):
	x = a
	p = []
	for i in range(2 * a):
		x -= 1
		y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
		if (x + x0 <= f) and (x + x0 >= g):
			p.append((x + x0, y + y0))
	for i in range(2 * a):
		x += 1
		y = -(((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
		if (x + x0 <= f) and (x + x0 >= g):
			p.append((x + x0, y + y0))
	polygon(p)


# зона облака и белого дома
def leps3(a, b, x0, y0, f, g):
	x = -a
	p = [(761, 22), (605, 22)]
	for i in range(2 * a):
		x += 1
		y = (((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
		if (x + x0 <= f) and (x + x0 >= g):
			p.append((x + x0, y + y0))
	polygon(p)


# рисует дом с размерами sхh
def dom(x, y, s, h):
	obj_dom = polygon([(x, y), (s + x, y), (s + x, h + y), (x, h + y)])
	return obj_dom

def okno(a, b):
	polygon([(60 + a, b - 20), (80 + a, b - 20), (80 + a, b - 10), (60 + a, b - 10)])


# x большая полуось, y -малая
# a начало машины по оси х, b по y
def koleso(x, y, a, b):
	penColor("#00222b")
	brushColor("#00222b")
	leps(x, y, a, b)

def kolesomove(x, y, a, b):
	penColor("#00222b")
	brushColor("#00222b")
	b = leps(x, y, a, b)
	return b
# рисуем машину и колеса
# a начало машины по оси х, b по y
def car(a, b):
	penColor("#00ccff")
	brushColor("#00ccff")
	polygon([(a, b), (a + 273, b), (a + 273, b + 30), (a, b + 30)])
	polygon([(a + 50, b), (a + 150, b), (a + 150, b - 30), (a + 50, b - 30)])

	penColor("#d5f6ff")
	brushColor("#d5f6ff")

	okno(a, b)
	okno(50 + a, b)

	penColor("#00222b")
	brushColor("#00222b")
	polygon([(a, b + 25), (a, b + 15), (a - 30, b + 15), (a - 30, b + 25)])

	koleso(25, 15, a + 50, b + 30)
	koleso(25, 15, a + 170, b + 30)

def movecar(a,b,t):
	penColor("#00ccff")
	brushColor("#00ccff")
	c = polygon([(a, b), (a + 273, b), (a + 273, b + 30), (a, b + 30)])
	d = polygon([(a + 50, b), (a + 150, b), (a + 150, b - 30), (a + 50, b - 30)])
	onTimer(lambda c = c:moveObjectBy(c, 5, 0),t)
	onTimer(lambda d = d:moveObjectBy(d, 5, 0),t)
	
	penColor("#d5f6ff")
	brushColor("#d5f6ff")
	c = polygon([(60 + a, b - 20), (80 + a, b - 20), (80 + a, b - 10), (60 + a, b - 10)])
	d = polygon([(110 + a, b - 20), (130 + a, b - 20), (130 + a, b - 10), (110 + a, b - 10)])
	onTimer(lambda c = c:moveObjectBy(c, 5, 0),t)
	onTimer(lambda d = d:moveObjectBy(d, 5, 0),t)
	
	penColor("#00222b")
	brushColor("#00222b")
	c = polygon([(a, b + 25), (a, b + 15), (a - 30, b + 15), (a - 30, b + 25)])
	onTimer(lambda c = c:moveObjectBy(c, 5, 0),t)

	c = kolesomove(25, 15, a + 50, b + 30)
	d = kolesomove(25, 15, a + 170, b + 30)
	onTimer(lambda c = c:moveObjectBy(c, 5, 0),t)
	onTimer(lambda d = d:moveObjectBy(d, 5, 0),t)

def nebo():
	penColor("#b7c4c8")
	brushColor("#b7c4c8")
	a = polygon([(0, 0), (792, 0), (792, 710), (0, 710)])
	onTimer(lambda a=a:changeFillColor(a,randColor()),100)

# рисуем фон

nebo()
penColor("#536c67")
brushColor("#536c67")
p2 = [(0, 715), (792, 715), (792, 1200), (0, 1200)]
polygon(p2)

penColor("#b7c8c4")
brushColor("#b7c8c4")
circle(370, 1500, 650)

# рисуем задние эллипсы
penColor("#a8baba")
brushColor("#a8baba")
leps(330, 90, 225, 141)
leps(330, 90, 178, 573)
leps(330, 90, 621, 40)

# дома
penColor("#93a7ac")
brushColor("#93a7ac")
a = dom(0, 0, 157, 700)


penColor("#93aca7")
brushColor("#93aca7")
dom(198, 40, 157, 700)

penColor("#b7c8c4")
brushColor("#b7c8c4")
dom(105, 100, 157, 700)

penColor("#dbe3e2")
brushColor("#dbe3e2")
dom(590, 0, 157, 700)

penColor("#6f918a")
brushColor("#6f918a")
dom(505, 120, 157, 700)

# облака над домом
"""penColor("#a8baba")
brushColor("#a8baba")
leps(330, 90, 570, 372)

penColor("#7d9b59")
brushColor("#7d9b95")
leps2(330, 90, 570, 372, 676, 519)

penColor("#a8baba")
brushColor("#a8baba")
leps2(330, 90, 570, 372, 519, 370)

penColor("#beccca")
brushColor("#beccca")
leps2(330, 90, 570, 372, 761, 677)

penColor("#93aca7")
brushColor("#93aca7")
leps2(330, 90, 570, 372, 369, 276)
penColor("#a8bcb8")
brushColor("#a8bcb8")
leps2(330, 90, 570, 372, 276, 0)

penColor("#beccca")
brushColor("#beccca")
leps3(330, 90, 621, 40, 761,605)"""

# дым летит
penColor("#6c8580")
brushColor("#6c8580")
a=leps(80, 20, 0, 832)
b=leps(80, 20, 130, 900)
onTimer(lambda a=a:moveObjectBy(a, 0, -5),8)
onTimer(lambda b=b:moveObjectBy(b, 0, -5),8)
#машина едет
movecar(250,900,40)
run()
