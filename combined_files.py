import Tkinter as tk
import pyglet

from math import cos, pi, sin

from Colour import Color, Colour


class Display(object):
    """docstring for Display"""

    def __init__(self, r, x, y, vx, vy):
        self.r = r
        self.x, self.y = (x, y)
        self.vx, self.vy = (vx, vy)

    def update(self, dt, window_width, window_height):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x + self.r > window_width:
            self.x = window_width - self.r
            self.vx = - self.vx

        if self.x - self.r < 0:
            self.x = self.r
            self.vx = - self.vx

        if self.y + self.r > window_height:
            self.y = window_height - self.r
            self.vy = - self.vy

        if self.y - self.r < 0:
            self.y = self.r
            self.vy = - self.vy


class PygletDisplay(Display):
    """docstring for ClassName"""

    def __init__(self, r, x, y, vx, vy):
        super(PygletDisplay, self).__init__(r, x, y, vx, vy)
        self.window = pyglet.window.Window(600, 400)
        self.fps_display = pyglet.clock.ClockDisplay()
        self.twopi = 2 * pi
        self.window.event(self.on_draw)

    def on_draw(self):
        self.window.clear()

        def circle_vertices():
            delta_angle = self.twopi / 20
            angle = 0
            while angle < self.twopi:
                yield self.x + self.r * cos(angle)
                yield self.y + self.r * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))

        self.fps_display.draw()

    def update(self, dt):
        super(PygletDisplay, self).update(
            dt, self.window.width, self.window.height)

    # def move(self, dt):
    #     # global x, y, vx, vy
    #     self.x += self.vx * dt
    #     self.y += self.vy * dt

    # def bounce(self, bounding_box):
    #     xmin, xmax, ymin, ymax = bounding_box

    #     excess = self.x + self.r - xmax
    #     if excess > 0:
    #         self.x -= excess * 2
    #         self.vx = - self.vx

    #     excess = self.x - self.r - xmin
    #     if excess < 0:
    #         self.x -= excess * 2
    #         self.vx = - self.vx

    #     excess = self.y + self.r - ymax
    #     if excess > 0:
    #         self.y -= excess * 2
    #         self.vy = - self.vy

    #     excess = self.y - self.r - ymin
    #     if excess < 0:
    #         self.y -= excess * 2
    #         self.vy = - self.vy


class TkinterDisplay(Display):
    """docstring for TkinterDisplay"""

    def __init__(self, r, x, y, vx, vy):
        super(TkinterDisplay, self).__init__(r, x, y, vx, vy)
        self.master = tk.Tk()
        self.window = tk.Canvas(self.master, width=600, height=400, bg='black')
        self.window.pack()

    def particle(self):
        return self.window.create_oval(
            self.x, self.y, self.x + self.r, self.y + self.r, outline='yellow')

    def update(self, dt):
        oldx, oldy = self.x, self.y
        super(TkinterDisplay, self).update(
            dt, self.window.winfo_width(), self.window.winfo_height())

        self.window.delete(tk.ALL)
        self.window.move(self.particle(), self.x - oldx, self.y - oldy)
        self.window.update()
        self.window.after(17, self.update, 1 / 60.0)


function_choice = raw_input(
    "Please choose function: 1 -> PyGlet or 2 -> Tkinter. Input: ")

while (not function_choice.isdigit() or int(function_choice) not in (1, 2)):
    print("Illegal character - Please choose between 1 and 2")
    function_choice = raw_input(
        "Please choose function: 1 -> PyGlet | 2 -> Tkinter. Input: ")

result = int(function_choice)

if result == 1:
    p = PygletDisplay(30, 300, 200, 80.0, 150.0)
    pyglet.clock.schedule_interval(p.update, 1 / 60.0)
    pyglet.app.run()
elif result == 2:
    t = TkinterDisplay(60, 300, 200, 80.0, 150.0)
    t.update(0)
    tk.mainloop()
