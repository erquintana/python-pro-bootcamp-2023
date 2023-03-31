import snake
from turtle import Screen
import time
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

screen.update()

game_in_on = True
game_score = 0
while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision snake-food
    if(snake.head.distance(food)) < 15:
        food.refresh_food()
        snake.extend()
        game_score += 1
        scoreboard.update_score(game_score)

    # Detect wall collision
    if(snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280):
        game_in_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if(snake.head.distance(segment) < 10):
            game_in_on = False
            scoreboard.game_over()
            
screen.exitonclick()
