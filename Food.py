import turtle

import Utils
from Constants import FOOD_SIZE, FOOD_COLOR, FOOD_SHAPE


def getFoodPencil():
    pencil = turtle.Turtle()
    pencil.shape(FOOD_SHAPE)
    pencil.color(FOOD_COLOR)
    pencil.pensize(round(FOOD_SIZE / 20))
    return pencil


def drawFood(foodPencil):
    foodPos = Utils.getRandomFoodPos()
    foodPencil.penup()
    foodPencil.goto(foodPos)
    return foodPos
