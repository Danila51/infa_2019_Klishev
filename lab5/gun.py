# coding=utf-8
from random import randrange as rnd, choice
from tkinter import mainloop, BOTH, Canvas, Frame, Tk
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('1500x1000')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class Ball:
    def __init__(self, g, x, y, r, a, type):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0  # speed
        self.vy = 0  # speed
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.type = type  # 1- ball, 2 - square
        if self.type == 1:
            self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                       fill=self.color)
        else:
            self.id = canv.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                            fill=self.color)
        self.live = 100  # time of live
        self.game = g
        self.a = a  # a=0 start ball, a=1 fragment

    def set_coords(self):  # redraw
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):  # function of the motion of bodies
        if self.y <= 950:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coords()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 949
        if self.a == 0:
            if self.live == 60:  # if live == 60, boom happens
                self.game.balls.pop(self.game.balls.index(self))
                canv.delete(self.id)
                self.boom()
            else:
                self.live -= 1
        if self.a == 1:
            if self.live <= 0:
                self.game.balls.pop(self.game.balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 1480:
            self.vx = -self.vx / 1.3
            self.x = 1479

    def hittest(self, ob):  # checking collisions
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False

    def boom(self):  # boom
        n = rnd(4, 10)
        boomballs = [Ball(self.game, self.x + rnd(5, 10), self.y + rnd(5, 10), 4, 1, rnd(1, 3)) for _ in range(n)]
        for i in range(n):
            boomballs[i].vx = rnd(-10, 10)
            boomballs[i].vy = rnd(-10, 10)
            self.game.balls += [boomballs[i]]


class Gun:
    def __init__(self, g):
        self.f2_power = 10  # +power after targetting
        self.f2_on = 0  # start of fire
        self.an = 1  # angle
        self.y = 899  # starting coord of gun
        self.vy = 8  # starting speed of gun
        self.id = canv.create_line(20, self.y, 50, self.y - 30, width=7)
        self.game = g

    def fire2_start(self, event):  # start of fire
        self.f2_on = 1

    def fire2_end(self, event):  # end of fire
        if self.game.h:
            self.game.bullet += 1
            new_ball = Ball(self.game, 40, self.y, 9, 0, rnd(1, 3))
            self.move_gun()
            self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x + 0.00001))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = -self.f2_power * math.sin(self.an)
            self.game.balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 10

    def targetting(self, event=0):  # targetting
        if event:
            self.an = math.atan((event.y - self.y) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, self.y, 20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):  # +power after targetting
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move_gun(self):  # function of the motion of gun
        self.y += self.vy
        if (self.y <= 90) or (self.y >= 900):
            self.vy *= -1


class Target:
    def __init__(self):
        self.live = 1
        self.color = 'red'
        self.x = rnd(500, 1400)
        self.y = rnd(100, 800)
        self.r = rnd(20, 50)
        self.vy = 5
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='40')

    def new_target(self):
        x = self.x
        y = self.y
        color = self.color
        r = self.r
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def set_coords(self):  # redraw
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move_target(self):  # function of the motion of targets
        self.y += self.vy
        if (self.y <= 50 + self.r) or (self.y >= 950 - self.r):
            self.vy *= -1
        if self.live == 0:
            canv.delete(self.id)
        self.set_coords()

    def hit(self):
        self.points += 1
        # canv.itemconfig(self.id_points, text = self.points)  # меняет


class Game:
    def __init__(self):
        self.balls = []  # storage of balls
        self.bullet = 0  # storage of bullets
        self.number_of_targets = rnd(2, 10)
        self.targets = [Target() for _ in range(self.number_of_targets)]  # storage of targets
        self.g1 = Gun(self)  # пушка джокера
        self.h = 1  # if h=1 at least 1 target lives, if 0 - no one

    def new_game(self, event=''):
        screen1 = canv.create_text(700, 200, text='', font='40')
        self.balls = []
        self.bullet = 0
        self.targets = [Target() for _ in range(self.number_of_targets)]
        for t in self.targets:  # draw targets
            t.new_target()
        canv.bind('<Button-1>', self.g1.fire2_start)
        canv.bind('<ButtonRelease-1>', self.g1.fire2_end)
        canv.bind('<Motion>', self.g1.targetting)
        while True:
            self.targets_lives = [self.targets[i].live for i in
                                  range(self.number_of_targets)]  # storage of target's lives
            self.h = 1
            self.live_checker()
            if self.h or self.balls:
                for t in self.targets:
                    t.move_target()
                for b in self.balls:
                    b.move()
                    for t in self.targets:
                        if b.hittest(t):
                            t.live = 0
                            t.hit()
                            if self.bullet == 1:
                                canv.itemconfig(screen1, text='Вы сделали ' + str(self.bullet) + ' выстрел')
                            elif (self.bullet % 10 >= 2) and (self.bullet % 10 <= 4):
                                canv.itemconfig(screen1, text='Вы сделали ' + str(self.bullet) + ' выстрела')
                            else:
                                canv.itemconfig(screen1, text='Вы сделали ' + str(self.bullet) + ' выстрелов')
                canv.update()
                time.sleep(0.009)
                self.g1.move_gun()
                self.g1.targetting()
                self.g1.power_up()
            else:
                if self.bullet == 1:
                    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(self.bullet) + ' выстрел. Вы крутой')
                elif (self.bullet % 10 >= 2) and (self.bullet % 10 <= 4):
                    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(self.bullet) + ' выстрела')
                else:
                    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(self.bullet) + ' выстрелов')
                canv.update()
                time.sleep(2)
                break
        canv.itemconfig(screen1, text='')
        root.after(500, self.new_game)

    def live_checker(self):  # it check lives of targets
        if self.targets_lives[0] == 0:
            for i in range(1, self.number_of_targets):
                if self.targets_lives[i] == self.targets_lives[i - 1]:
                    self.h = 0
                else:
                    self.h = 1
                    break


game1 = Game()
game1.new_game()
mainloop()
