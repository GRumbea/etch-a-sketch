from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def counter_clockwise():
    t.left(10)


def clockwise():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()


screen.listen()
screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=counter_clockwise, key='a')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=clear, key='c')


screen.exitonclick()
