import math
from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def draw(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    for x in range(0, 800, 5):
        draw(x, 80)
    for y in range(80, 550, 5):
        draw(800, y)
    for x in range(800, 0, -5):
        draw(x, 550)
    for y in range(550, 80, -5):
        draw(0, y)

def move_triangle():
    points = [(400, 550), (100, 80), (700, 80)]
    for i in range(3):
        start = points[i]
        end = points[(i + 1) % 3]
        steps = 100
        for t in range(steps):
            x = start[0] + (end[0] - start[0]) * t / steps
            y = start[1] + (end[1] - start[1]) * t / steps
            draw(x, y)

def move_circle():
    r = 200
    center_y = 80 + r
    for deg in range(0, 360, 2):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + center_y
        draw(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()


