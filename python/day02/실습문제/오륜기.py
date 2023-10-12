# 8번, 오륜기 색깔 채워 그리기
import turtle as t

t.shape("turtle")
t.width(10)
t.speed(0.5)


def make_color_circle(color, size):
    t.color(color)
    t.circle(size)


def move_position(x, y):
    t.up()
    t.goto(x, y)
    t.down()


# 하늘 노랑 검은 초록 빨강

COLOR_ARRAY = ["deepskyblue", "gold", "black", "forestgreen", "red"]

RADIUS = 100

position_x = -(len(COLOR_ARRAY) / 2 * RADIUS)
position_y = 0

for i in range(5):
    if i % 2 == 0:
        position_y = 0
    else:
        position_y = -RADIUS
    move_position(position_x, position_y)
    make_color_circle(COLOR_ARRAY[i], RADIUS)
    position_x += RADIUS + 10
t.done()
