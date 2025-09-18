from pico2d import *

open_canvas()

boy=load_image('character.png')
grass=load_image('grass.png')


def move_top():
    print('Moving top')
    for x in range(10,780,5):
        draw(x,550)


    pass


def move_right():
    print('Moving right')
    for y in range(550,90,-5):
        draw(780,y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(780,10,-5):
        draw(x,90)
    pass


def move_left():
    print('Moving left')
    for y in range(90,550,5):
        draw(10,y)
    pass


def move_rectangle():
    print("Move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("Move circle")
    r=210
    for deg in range(0,360):
        x= r * math.cos(math.radians(deg))+400
        y= r * math.sin(math.radians(deg))+300
        draw(x, y)
    pass


def draw(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)


def move_triangle_point1():
    for x in range(100,700,2):
        draw(x,90)
    pass


def move_triangle_point2():
    x=700
    y=90
    while (x>=400 and y<=400):
        draw(x,y)
        x=x-2
        y=y+2

    pass


def move_triangle_point3():
    x=400
    y=400
    while(x>=100 and y>=90):
        draw(x,y)
        x=x-2
        y=y-2
    pass


def move_triangle2():
    print("Move triangle2")
    move_triangle_point1()
    move_triangle_point2()
    move_triangle_point3()
    pass


while True:
    # move_rectangle()
    # move_triangle2()
    move_circle()



    break
    pass


close_canvas()
