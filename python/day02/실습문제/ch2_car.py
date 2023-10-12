# 9번, 자동차 크기를 점점 키워 같은 자리에 그리기, 변수사용🡪 ch2_car.py

# 과제 3

import turtle as t

# 스피드 속도 조절 낮을 수록 빠름
t.speed(0)


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

first_head_width = 75
first_head_height = 25

first_body_width = 150
first_body_height = 50

first_circle_size = 10

increase_value = 3

for i in range(100):
    body_width = first_body_width + (i * increase_value)
    body_height = first_body_height + (i * increase_value)
    head_width = first_head_width + (i * increase_value / 2)
    head_height = first_head_height + (i * increase_value / 2)
    circle_size = first_circle_size + (i * increase_value / 5)

    move_position(-(body_width / 4), (body_height / 2))
    make_figure(head_width, head_height, "yellow")
    move_position(-(body_width / 2), -(body_height / 2))
    make_figure(body_width, body_height, "red")
    move_position(-(body_width / 4), -(body_height / 2) - circle_size)
    make_color_circle("black", circle_size)
    move_position((body_width / 4), -(body_height / 2) - circle_size)
    make_color_circle("black", circle_size)
t.done()
