
import time

from turtle import Screen
from snake import Snake
screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
game_on = True

def end_game()->bool:
    if snake.head.xcor() >= 250:
        return True
    return False
while game_on:
    time.sleep(0.1)
    screen.update()
    if end_game():
        game_on = False
    snake.move()
screen.exitonclick()