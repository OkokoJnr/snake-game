
import time

from turtle import Screen
from snake import Snake
screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    snake.move()
screen.exitonclick()