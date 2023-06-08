import Values
from Utils import Direction


def bindKeys(screen):
    screen.listen()
    screen.onkey(lambda: goDirection(Direction.UP), 'Up')
    screen.onkey(lambda: goDirection(Direction.DOWN), 'Down')
    screen.onkey(lambda: goDirection(Direction.LEFT), 'Left')
    screen.onkey(lambda: goDirection(Direction.RIGHT), 'Right')


def goDirection(direction):
    if Values.SnakeDirection != reversed(direction):
        Values.SnakeDirection = direction
