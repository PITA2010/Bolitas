from graphics import *

ventana=GraphWin("CIRCULO",500,500)
Circulo=Circle(Point(40,40),40)
Circulo.draw(ventana)
Circulo.setFill("blue")

while 1==1:
    for i in range (0,84):
        Circulo.move(5,5)
        time.sleep(0.05)

    for j in range (0,84):
        Circulo.move(0,-5)
        time.sleep(0.05)

    for k in range (0,84):
        Circulo.move(-5,5)
        time.sleep(0.05)

    for i in range (0,84):
        Circulo.move(0,-5)
        time.sleep(0.05)

time.sleep(10)