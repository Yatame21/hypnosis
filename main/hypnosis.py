from turtle import *

bgcolor('black')
hideturtle()
speed(10)

for i in range(120):
    if i % 2 == 0:
        color('white')
    else:
        color('red')
    forward(i * 3)
    left(91)
done()