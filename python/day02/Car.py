# 과제 3

import turtle as t


# 좌표 이동 함수
def move_position(x, y):
    t.up()
    t.goto(x, y)
    t.down()


# 도형만들기 함수
def make_figure(figure_width, figure_height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(figure_width)
    t.left(90)
    t.forward(figure_height)
    t.left(90)
    t.forward(figure_width)
    t.left(90)
    t.forward(figure_height)
    t.left(90)
    t.end_fill()


#  원그리기 함수
def make_color_circle(color, size):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


t.shape("turtle")

head_width = 200
head_height = 100

body_width = 400
body_height = 200

circle_size = 40

move_position(-(body_width / 4), (body_height / 2))
make_figure(head_width, head_height, "yellow")
move_position(-(body_width / 2), -(body_height / 2))
make_figure(body_width, body_height, "red")
move_position(-(body_width / 4), -(body_height / 2) - circle_size)
make_color_circle("black", circle_size)
move_position((body_width / 4), -(body_height / 2) - circle_size)
make_color_circle("black", circle_size)
t.done()
