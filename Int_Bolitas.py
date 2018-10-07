from graphics import *

ventana=GraphWin("CIRCULO",500,500)
Circulo=Circle(Point(40,50),40)
Circulo.draw(ventana)
Circulo.setFill("blue")

'''while 1==1:
    r=(500-())
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
        time.sleep(0.05)'''
x=40
y=50
while 1==1:
    for i in range (0,10000):
        if x<=460 and y<=50:
            for i in range (0,(int((500 - (y + 50)) / 5))):
                Circulo.move(5,5)
                time.sleep(0.05)
                x=x+5
                y=y+5

        if x<=460 and y>=450:
            for i in range (0,(int((500 - (x + 40)) / 5))):
                Circulo.move(5,-5)
                time.sleep(0.05)
                x=x+5
                y=y-5

        if x>=460 and y<=450:
            for i in range (0,(int((y-50)/5))):
                Circulo.move(-5,-5)
                time.sleep(0.05)
                x=x-5
                y=y-5

        if x<=460 and y<=50:
            for i in range (0,(int((x-40)/5))):
                Circulo.move(-5,5)
                time.sleep(0.05)
                x=x-5
                y=y+5

        if x<=40 and y<=450:
            for i in range (0,(int((500 - (y + 50)) / 5))):
                Circulo.move(5,5)
                time.sleep(0.05)
                x=x+5
                y=y+5

time.sleep(5)
