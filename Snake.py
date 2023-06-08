import turtle

from Constants import SNAKE_COLOR, SNAKE_SHAPE


def getSnakePencil():
    pencil = turtle.Turtle()
    pencil.shape(SNAKE_SHAPE)
    pencil.color(SNAKE_COLOR)
    pencil.penup()
    return pencil


def drawSnake(snakePencil, snake):
    for segment in snake:
        snakePencil.goto(segment[0], segment[1])
        snakePencil.stamp()
