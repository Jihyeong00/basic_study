'''
<실기문제 #3>
1. 도형의 종류 : 원, 삼각형, 사각형, 오각형중 임의로 하나의 도형 선택 

2. 도형의 한 변의 길이나 원의 반지름은 10~100사이의 값중 임의 크기로 선택

3. 도형을 채울 색깔은 다음중 하나를 무작위로 고른다.
   “red”, “yellow”, ‘green“, ”blue“, ”purple“

4. 도형을 그리기 시작하는 x,y좌표는 –200 ~ +200 중에서 무작위로 선택한다.

5. 1~4에서 선택한 조건으로 도형을 그린다.

6. 위의 1~5번 과정을 10번 반복한다.
'''
import random as r
import turtle as t

color_list = ["red", "yellow", "green", "purple"]


def get_random_length_and_color():
    length = r.randint(10, 100)
    color = r.choice(color_list)
    return [length, color]


def get_random_kind():
    kind = r.choice([0, 3, 4, 5])
    return kind


def fill_color(color):
    t.fillcolor(color)
    t.begin_fill()


def is_circle(kind):
    return kind == 0


def draw_circle(length):
    t.circle(length)


def draw_figure(kind, length, angle):
    for j in range(kind):
        t.fd(length)
        t.left(angle)


def random_move():
    x = r.randint(-200, 200)
    y = r.randint(-200, 200)

    t.up()
    t.goto(x, y)
    t.down()


def play_draw():
    kind = get_random_kind()

    [length, color] = get_random_length_and_color()

    random_move()

    fill_color(color)

    if is_circle(kind):
        draw_circle(length)
    else:
        angle = 360 / kind
        draw_figure(kind, length, angle)

    t.end_fill()


def q3():
    for i in range(10):
        play_draw()

    t.done()


q3()

