from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
player = load_image('character.png')
x=0
def square():
    for x in range(400,750,5):
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,90)
        delay(0.01)
    for y in range(90,540,5):
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(750,y)
        delay(0.01)
    for x in range(750,50,-5):
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,540)
        delay(0.01)
    for y in range(540,90,-5):
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(50,y)
        delay(0.01)
    for x in range(0,400,5):
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,90)
        delay(0.01)
def circle():
    for dig in range(270,360+270):
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(400 + (math.cos(math.radians(dig))) * 200 , 300 + math.sin(math.radians(dig))*200)
        delay(0.01)
while(True):
    square()
    circle()
