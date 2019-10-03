from graph import *

windowSize(900, 1400)
canvasSize(792, 1200)
# рисут эллипс
def leps(a, b, x0, y0):
    x = a
    y = 0
    tet = [(x0 + a, y0)]
    for i in range(2 * a):
        x -= 1
        y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        tet.append((x + x0, y + y0))
    for i in range(2 * a):
        x += 1
        y = -(((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
        tet.append((x + x0, y + y0))
    polygon(tet)

#зона перекрытия большого облака и домов
def leps2(a, b, x0, y0, f, g):
    x = a
    y = 0
    tet = []
    for i in range(2 * a):
        x -= 1
        y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        if (x + x0 <= f) and (x + x0 >= g):
            tet.append((x + x0, y + y0))
    for i in range(2 * a):
        x += 1
        y = -(((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
        if (x + x0 <= f) and (x + x0 >= g):
            tet.append((x + x0, y + y0))
    polygon(tet)
# зона облака и белого дома
def leps3(a, b, x0, y0, f, g):
    x = -a
    y = 0
    tet = [(761, 22),(605, 22)]
    for i in range(2 * a):
        x += 1
        y = (((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
        if (x + x0 <= f) and (x + x0 >= g):
            tet.append((x + x0, y + y0))
    polygon(tet)


def dom(x, y):
    p3 = [(15 + x, 22 + y), (171 + x, 22 + y), (171 + x, 736 + y), (15 + x, 736 + y)]
    polygon(p3)


def okno(x, y):
    p5 = [(320 + x, 880 + y), (340 + x, 880 + y), (340 + x, 890 + y), (320 + x, 890 + y)]
    polygon(p5)


# рисуем фон
penColor("#b7c4c8")
brushColor("#b7c4c8")
p1 = [(0, 0), (792, 0), (792, 710), (0, 710)]
polygon(p1)

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

penColor("#93a7ac")
brushColor("#93a7ac")
dom(0, 0)

penColor("#93aca7")
brushColor("#93aca7")
dom(198, 40)

penColor("#b7c8c4")
brushColor("#b7c8c4")
dom(105, 100)

penColor("#dbe3e2")
brushColor("#dbe3e2")
dom(590, 0)

penColor("#6f918a")
brushColor("#6f918a")
dom(505, 120)

penColor("#a8baba")
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
leps3(330, 90, 621, 40, 761,605)

# рисуем машину и колеса
penColor("#00ccff")
brushColor("#00ccff")
p3 = [(260, 900), (533, 900), (533, 930), (260, 930)]
polygon(p3)
p4 = [(310, 900), (410, 900), (410, 870), (310, 870)]
polygon(p4)
penColor("#d5f6ff")
brushColor("#d5f6ff")
okno(0, 0)
okno(50, 0)
penColor("#00222b")
brushColor("#00222b")
p6 = [(260, 925), (260, 915), (230, 915), (230, 925)]
polygon(p6)
penColor("#a8baba")
brushColor("#a8baba")
penColor("#00222b")
brushColor("#00222b")
leps(25, 15, 320, 935)
leps(25, 15, 460, 935)

#дым
penColor("#6c8580")
brushColor("#6c8580")
leps(80,20,0,832)
leps(80,20,130,900)

run()
