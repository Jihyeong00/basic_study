import turtle as t

t.shape("turtle")

"""
도형 종류와 크기, 색깔을 물어보고 요구사항에 맞게 화면 중앙에 그림을 그리는 프로그램

요구사항 정리

 1. 도형의 종류를 입력을 받아야합니다.
 2. 도형의 크기를 입력을 받습니다.
 3. 도형의 색깔을 입력을 받습니다.
 4. 도형을 그립니다.
"""

COLOR_ARRAY = ['red', 'yellow', 'blue', 'green', 'black']
ERROR_NUMBER = [1, 2, 7]


def move_position(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def make_figure(figure_color, width, count):
    t.left(0)
    t.fillcolor(figure_color)
    t.begin_fill()
    for i in range(count):
        t.forward(width)
        t.left(360 / count)
    t.end_fill()


def make_circle(circle_size, circle_color):
    t.fillcolor(circle_color)
    t.begin_fill()
    t.circle(circle_size)


# 1. 도형의 종류를 입력을 받아야합니다.
def set_figure_type():
    num_input = int(t.textinput("", "도형을 어떻게 그릴까요? 0 ~ 8중 1, 2, 7을 제외한 숫자를 입력할 수 있습니다."))
    if num_input in ERROR_NUMBER:
        return "[ERROR]"
    if num_input == 0:
        return "circle"
    return num_input


# 2. 도형의 크기를 입력을 받습니다.
def set_color_type():
    num_input = int(t.textinput("", "어떤 색깔로 그릴까요? 1:red 2:yellow 3:blue 4:green 5: black"))
    return COLOR_ARRAY[num_input]


# 3. 도형의 색깔을 입력을 받습니다.
def set_size():
    num_input = int(t.textinput("", "도형의 크기를 어떻게 할까요?"))
    return num_input


# 4. 도형을 그립니다.
def play():
    figure_type = set_figure_type()
    color = set_color_type()
    size = set_size()

    if figure_type == "[ERROR]":
        return

    if figure_type == 0:
        return make_circle(size, color)

    return make_figure(color, size, figure_type)


play()

t.done()
