# 과제 1

import turtle as t


# 좌표 이동 함수
def move_position(x, y):
    t.up()
    t.goto(x, y)
    t.down()


# 도형 만들기 함수
def make_figure(color, width, count):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(count):
        t.forward(width)
        t.left(360 / count)
    t.end_fill()


# 요구 사항 1.사각형
move_position(-50, 200)
make_figure('red', 100, 4)

# 요구 사항 2.삼각형
move_position(-50, 0)
make_figure('blue', 100, 3)

# 요구 사항 3. 육각형
move_position(-45, -300)
make_figure('green', 75, 6)

t.done()
