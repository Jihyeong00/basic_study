# 5번, 반지름초기값 50 을 radiu변수에 저장,
#
# (0.0) (100,0), (200,0) 좌표에 반지름을 20씩 증가하면서 원 3개 그리기🡪draw_circle.py
import turtle as t

radius = 50

def make_circle(size):
    t.circle(size)

def move_position(x, y):
    t.up()
    t.goto(x, y)
    t.down()


for i in range(3):
    move_position(i * 100, 0)
    make_circle(radius)
    radius += 20

t.done()
