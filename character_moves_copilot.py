from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def move_top():
    print('Moving top')
    for x in range(0, 800, 5):
        draw(x, 550)

def move_right():
    print('Moving right')
    for y in range(550, 50, -5):
        draw(800, y)

def move_bottom():
    print('Moving bottom')
    for x in range(800, 0, -5):
        draw(x, 50)

def move_left():
    print('Moving left')
    for y in range(50, 550, 5):
        draw(0, y)

def move_rectangle():
    print("Move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_triangle():
    print("Move triangle")
    # 삼각형의 세 꼭지점
    points = [(400, 500), (100, 100), (700, 100)]

    # 각 변을 따라 이동
    for i in range(3):
        start = points[i]
        end = points[(i + 1) % 3]

        steps = 100
        for t in range(steps):
            x = start[0] + (end[0] - start[0]) * t / steps
            y = start[1] + (end[1] - start[1]) * t / steps
            draw(x, y)

def move_circle():
    print("Move circle")
    r = 200
    for deg in range(0, 360, 2):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw(x, y)

def draw(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
