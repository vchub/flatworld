import random
import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(10)
food = turtle.Turtle()


def init(t, food):
    # init state
    x = random.randint(100, 150)
    y = random.randint(100, 150)
    x1 = random.randint(-150, -100)
    y1 = random.randint(-150, -110)
    t.up()
    food.up()
    t.goto(x, y)
    food.goto(x1, y1)
    t.down()


def random_step(t) -> int:
    s = random.randint(0, 50)
    ang = random.randint(0, 360)
    t.left(ang)
    t.forward(s)
    return s


def continue_step(t, s):
    t.forward(s)


def find_dir(t, a):
    s = 0
    while t.distance(food) > a:
        s = random_step(t)
        if t.distance(food) > a:
            t.back(s)
    return s


def dist():
    return t.distance(food)


def run_world(h):
    init(t, food)
    a = t.distance(food)

    # this step should decrease when you closer to the food
    s = 25
    while dist() > h:
        t.forward(s)
        # print(a, dist())
        if a < dist():
            s = find_dir(t, a)
        a = dist()

    # продолжает шагать,пока запах не станет меньше
    # если станет меньше,ищет новое направление
    # когда найдёт,продолжает шагать(строка 1)

    # init(t, food)

    # for _ in range(20):

    #     t.left(ang)
    #     t.forward(len)
    #     if t.distance(food) < d0:
    #         t.forward(len)
    # x3, y3 = t.pos()


run_world(10)

wn.exitonclick()
