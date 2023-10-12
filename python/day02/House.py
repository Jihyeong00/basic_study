# 과제 2

import turtle as t


def move_position(x, y):
    t.up()
    t.goto(x, y)
    t.down()


# 도형 만들기 함수
def make_figure(figure_width, count):
    for i in range(count):
        t.forward(figure_width)
        t.left(360 / count)


width = int(input("집의 크기는 얼마로 할까요?"))
t.shape("turtle")
move_position(0, width)
make_figure(width, 3)
move_position(0, 0)
make_figure(width, 4)
t.done()
