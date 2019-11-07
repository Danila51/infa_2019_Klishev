from random import randrange as rnd, choice
from tkinter import mainloop, BOTH, Canvas, Frame, Tk
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class ball():
    def __init__(self, g, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 9
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color)
        self.live = 30
        self.game = g

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        if self.y <= 550:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coords()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 549
            if self.live < 0:
                self.game.balls.pop(self.game.balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 1.5
            self.x = 779

    def hittest(self, ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False


class gun():
    def __init__(self, g):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)
        self.game = g
        

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        if self.game.t1.live or  self.game.t2.live or self.game.t3.live:
            self.game.bullet += 1
            new_ball = ball(self.game)
            self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x + 0.00001))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = -self.f2_power * math.sin(self.an)
            self.game.balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='40')
        x = self.x = rnd(500, 780)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(20, 50)
        vy = self.vy = 5
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill = color)
        self.live = 1

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        
    def move_target(self):
        self.y += self.vy
        if (self.y <= 50 + self.r) or (self.y >= 600 - self.r):
            self.vy *= -1
        if self.live == 0:
            canv.delete(self.id)
        self.set_coords()

    def hit(self):
        self.points += 1
        #canv.itemconfig(self.id_points, text = self.points)  # меняет


class Game():
    def __init__(self):
        self.balls = []
        self.bullet = 0
        self.t1 = target()
        self.t2 = target()
        self.t3 = target()
        self.targets = [self.t1, self.t2, self.t3]
        self.g1 = gun(self)
        
    def new_game(self, event=''):
        screen1 = canv.create_text(400, 300, text='', font='40')
        self.balls = []
        self.bullet = 0
        canv.bind('<Button-1>', self.g1.fire2_start)
        canv.bind('<ButtonRelease-1>', self.g1.fire2_end)
        canv.bind('<Motion>', self.g1.targetting)
        while self.t1.live or  self.t2.live or self.t3.live or self.balls:
            for t in self.targets:
                t.move_target()
            for b in self.balls:
                b.move()
                for t in self.targets:
                    if b.hittest(t):
                        t.live = 0
                        t.hit()
                        if self.bullet == 1:
                            canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(self.bullet) + ' выстрел')
                        elif (self.bullet % 10 >= 2) and (self.bullet % 10 <= 4):
                            canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(self.bullet) + ' выстрела')
                        else:
                            canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(self.bullet) + ' выстрелов')
            canv.update()
            time.sleep(0.009)
            self.g1.targetting()
            self.g1.power_up()
        canv.itemconfig(screen1, text='')
        root.after(500, self.new_game)


game1 = Game()
game1.new_game()
mainloop()
