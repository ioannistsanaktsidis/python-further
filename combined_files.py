import sys

import pyglet

from math import cos, pi, sin, sqrt


class Particle(object):
    """docstring for ClassName"""
    window = pyglet.window.Window(600, 400)
    fps_display = pyglet.clock.ClockDisplay()
    twopi = 2 * pi

    def __init__(self, r, (x, y), (vx, vy)):
        self.r = r
        self.x, self.y = (x, y)
        self.vx, self.vy = (vx, vy)

    @window.event
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

    def move(self, dt):
        # global x, y, vx, vy
        self.x += self.vx * dt
        self.y += self.vy * dt

    def bounce(self, bounding_box):
        xmin, xmax, ymin, ymax = bounding_box

        excess = self.x + self.r - xmax
        if excess > 0:
            self.x -= excess * 2
            self.vx = - self.vx

        excess = self.x - self.r - xmin
        if excess < 0:
            self.x -= excess * 2
            self.vx = - self.vx

        excess = self.y + self.r - ymax
        if excess > 0:
            self.y -= excess * 2
            self.vy = - self.vy

        excess = self.y - self.r - ymin
        if excess < 0:
            self.y -= excess * 2
            self.vy = - self.vy

    # pyglet.clock.schedule_interval(update, 1 / 60.0)

    # pyglet.app.run()

# elif sys.argv[1] == 'tk':
#     import Tkinter as tk

#     master = tk.Tk()

#     w = tk.Canvas(master, width=600, height=400, bg='black')
#     w.pack()

#     x, y = w.winfo_height() / 2, w.winfo_width() / 2
#     vx, vy = 80.0, 150.0

#     diameter = 60

#     particle = w.create_oval(x, y, diameter, diameter, outline='yellow')

#     def update(dt):
#         global x, y, vx, vy
#         oldx, oldy = x, y
#         x += vx * dt
#         y += vy * dt

#         if x + 60 > w.winfo_width():
#             x = w.winfo_width() - 60
#             vx = - vx

#         if x < 0:
#             x = 0
#             vx = - vx

#         if y + 60 > w.winfo_height():
#             y = w.winfo_height() - 60
#             vy = - vy

#         if y < 0:
#             y = 0
#             vy = - vy

#         w.move(particle, x - oldx, y - oldy)
#         w.update()
#         w.after(17, update, 1 / 60.0)

#     update(0)

#     tk.mainloop()
