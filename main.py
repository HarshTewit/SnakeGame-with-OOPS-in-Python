import time
from snake import Snake
from turtle import Screen
from turtle import Turtle
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("Black")
screen.title("My Snake Game")
my_score = ScoreBoard()

screen.tracer(0)


snake = Snake()


game_is_on = True
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.segments[0].distance(food.xcor(), food.ycor()) < 20:
        food.refresh()
        snake.extend()
        my_score.clear()
        my_score.increase_score()

        print('nom')

    if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280 or snake.segments[0].xcor() < -280:
        my_score.gameOver()
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:

            game_is_on = False

            my_score.gameOver()














screen.exitonclick()

