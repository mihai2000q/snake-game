import turtle

import Artist
import Constants
import Food
import KeyBinder
import Snake
import Values
import Utils
from Utils import *


def gameLoop(snake):
    clearScreen()

    newHead = snake[-1].copy()
    newHead[0] += Values.SnakeDirection.value[0]
    newHead[1] += Values.SnakeDirection.value[1]

    # collision with walls and snake head on tail
    if newHead in snake or newHead[0] < - WIDTH / 2 or newHead[0] > WIDTH / 2 \
            or newHead[1] < - HEIGHT / 2 or newHead[1] > HEIGHT / 2:
        gameOver()
        return

    snake.append(newHead)
    if not foodCollision(snake):
        snake.pop(0)  # keeps the snake the same length, unless fed
    Snake.drawSnake(snakePencil, snake)

    screen.title(f"{TITLE}, Score: {Values.Score}")
    screen.update()
    turtle.ontimer(lambda: gameLoop(snake), DELAY)


def reset():
    global foodPos
    snake = [[i * SNAKE_SIZE, 0] for i in range(SNAKE_STARTING_LENGTH)]
    Values.SnakeDirection = Values.InitialSnakeDirection
    Values.Score = Values.InitialScore
    Snake.drawSnake(snakePencil, snake)
    foodPos = Food.drawFood(foodPencil)
    gameLoop(snake)
    return foodPos


def gameOver():
    turtle.clearscreen()
    turtle.bgcolor(Constants.BACKGROUND_COLOR)
    Artist.drawGameOver(0 - WIDTH * 0.12, 0 + HEIGHT * 0.3)
    turtle.done()
    # reset()


def foodCollision(snake):
    global foodPos
    if getDistance(snake[-1], foodPos) < 20:
        onFoodCollision()
        return True
    return False


def onFoodCollision():
    global foodPos
    foodPos = Utils.getRandomFoodPos()
    foodPencil.goto(foodPos)
    Values.Score += 1
    Constants.DELAY *= 2


def clearScreen():
    snakePencil.clearstamps()
    foodPencil.clearstamps()


screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title(TITLE)
screen.bgcolor(BACKGROUND_COLOR)
screen.tracer(0)

# Event handlers
KeyBinder.bindKeys(screen)

snakePencil = Snake.getSnakePencil()
foodPencil = Food.getFoodPencil()
foodPos = reset()

turtle.done()
