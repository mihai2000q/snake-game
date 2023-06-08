import turtle


def defaultPencil():
    pencil = turtle.Turtle()
    pencil.shape('circle')
    pencil.color('red')
    pencil.pensize(20)
    pencil.penup()
    return pencil


def drawGameOver(x, y):
    _drawG(x, y)
    _drawA(x + 115, y)
    _drawM(x + 115 * 2, y)
    _drawE(x + 115 * 3 + 40, y)

    x = x + x * 0.25
    y = y - y * 1.8
    _drawO(x, y)
    y = y - y * 1
    _drawV(x - x * 0.63, y)
    _drawE(x - x * 1.6, y)
    _drawR(x - x * 2.35, y)

    _drawLine(x - 75, y - 250)


def _drawA(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.left(245)
    pencil.forward(175)
    pencil.penup()
    pencil.goto(x, y)
    pencil.pendown()
    pencil.right(245 + 65)
    pencil.forward(175)
    pencil.penup()

    pencil.left(65 + 90)
    pencil.forward(57)
    pencil.left(90)
    pencil.forward(27)

    pencil.pendown()
    pencil.forward(84)

    pencil.penup()
    pass


def _drawE(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.right(90)
    pencil.forward(160)
    pencil.left(90)
    pencil.forward(70)
    pencil.penup()

    pencil.left(90)
    pencil.forward(80)
    pencil.left(90)
    pencil.forward(15)
    pencil.pendown()
    pencil.forward(55)

    pencil.penup()
    pencil.right(90)
    pencil.forward(80)
    pencil.right(90)
    pencil.pendown()
    pencil.forward(70)

    pencil.penup()


def _drawG(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.right(180)
    pencil.forward(35)
    pencil.left(180)
    pencil.circle(-80, -180)
    pencil.right(180)
    pencil.forward(38)
    pencil.left(90)
    pencil.forward(67)
    pencil.left(90)
    pencil.forward(50)

    pencil.penup()


def _drawM(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.right(90)
    pencil.forward(158)
    pencil.penup()
    pencil.goto(x, y)
    pencil.pendown()
    pencil.left(35)
    pencil.forward(100)
    pencil.left(35 + 75)
    pencil.forward(100)
    pencil.right(45 + 100)
    pencil.forward(158)

    pencil.penup()


def _drawO(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.circle(87)

    pencil.penup()


def _drawR(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.right(180)
    pencil.forward(20)
    pencil.left(180)

    pencil.right(90)
    pencil.forward(165)

    pencil.penup()
    pencil.left(90)
    pencil.forward(165)
    pencil.left(180)
    pencil.forward(156)
    pencil.left(180)
    pencil.left(90)
    pencil.forward(85)
    pencil.right(90)
    pencil.pendown()
    pencil.penup()
    pencil.pendown()

    pencil.forward(20)
    pencil.circle(40, 180)
    pencil.penup()
    pencil.forward(15)
    pencil.left(90)
    pencil.forward(75)
    pencil.right(90)
    pencil.forward(10)
    pencil.left(90)
    pencil.pendown()
    pencil.left(38)
    pencil.forward(113)

    pencil.penup()


def _drawV(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.right(68)
    pencil.forward(175)
    pencil.left(68 + 68)
    pencil.forward(175)

    pencil.penup()


def _drawLine(x, y):
    pencil = defaultPencil()
    pencil.goto(x, y)
    pencil.pendown()

    pencil.left(135)
    pencil.forward(50)
    pencil.right(135)
    pencil.forward(750)

    pencil.penup()
