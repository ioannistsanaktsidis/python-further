import pyglet

from math import cos, pi, sin, sqrt
twopi = 2 * pi

window = pyglet.window.Window(600, 400)
fps_display = pyglet.clock.ClockDisplay()

x, y = window.width / 2, window.height / 2
vx, vy = 80.0, 150.0

radius = 30


@window.event
def on_draw():
    window.clear()

    def circle_vertices():
        delta_angle = twopi / 20
        angle = 0
        while angle < twopi:
            yield x + radius * cos(angle)
            yield y + radius * sin(angle)
            angle += delta_angle

    pyglet.gl.glColor3f(1.0, 1.0, 0)
    pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))

    fps_display.draw()


def update(dt):
    global x, y, vx, vy
    x += vx * dt
    y += vy * dt

    if x + radius > window.width:
        x = window.width - radius
        vx = - vx

    if x - radius < 0:
        x = radius
        vx = - vx

    if y + radius > window.height:
        y = window.height - radius
        vy = - vy

    if y - radius < 0:
        y = radius
        vy = - vy


pyglet.clock.schedule_interval(update, 1 / 60.0)

pyglet.app.run()
