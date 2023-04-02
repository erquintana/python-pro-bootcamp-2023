# Import necessary modules and classes
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from turtle import Screen, Turtle
import time
import random
import configFile

# Get game configuration values from configFile
GAMEBOARD_W = configFile.GAMEBOARD_W
GAMEBOARD_H = configFile.GAMEBOARD_H
SLEEP_TIME = configFile.SLEEP_TIME

def draw_board():
    liner = Turtle()
    liner.hideturtle()
    liner.penup()
    liner.goto(0, -GAMEBOARD_H/2)
    liner.color("white")
    liner.pensize(6)
    space = 0
    while(liner.pos()[1] < GAMEBOARD_H/2):
        liner.pendown()
        liner.goto(0, -GAMEBOARD_H/2+space*GAMEBOARD_H/25)
        liner.penup()
        liner.goto(0, -GAMEBOARD_H/2+(space+1)*GAMEBOARD_H/25)
        space += 2
    liner.pendown()
    liner.pensize(10)
    liner.goto(-GAMEBOARD_W/2,GAMEBOARD_H/2)
    liner.goto(-GAMEBOARD_W/2,-GAMEBOARD_H/2)
    liner.goto(GAMEBOARD_W/2,-GAMEBOARD_H/2)
    liner.goto(GAMEBOARD_W/2,GAMEBOARD_H/2)
    liner.goto(0,GAMEBOARD_H/2)


def main():
    """Main function that runs the Pong game."""
    # Initialize scores for both players
    score_L = 0
    score_R = 0

    # Set up game screen
    gameboard = Screen()

    gameboard.setup(width=GAMEBOARD_W+75, height=GAMEBOARD_H+75)
    gameboard.bgcolor("light steel blue")
    gameboard.title("PONG GAME")
    gameboard.tracer(0)

    # Create instances of Ball and Scoreboard
    ball = Ball()
    scoreboard = Scoreboard()
    draw_board()


    # Create instances of Paddle for both players
    paddle_R = Paddle(X=GAMEBOARD_W/2-75, Y=0)
    paddle_L = Paddle(X=-GAMEBOARD_W/2+75, Y=0)

    # Set up keyboard controls
    gameboard.listen()
    gameboard.onkeypress(paddle_R.move_up, "Up")
    gameboard.onkeypress(paddle_R.move_down, "Down")
    gameboard.onkeypress(paddle_L.move_up, "w")
    gameboard.onkeypress(paddle_L.move_down, "s")

    # Initialize game loop
    game_is_on = True

    # Initialize ball movement variables
    speed_x = 1
    speed_y = 1
    speed_x = random.randrange(1, 2, 1)
    speed_y = random.randrange(1, 2, 1)
    # Game loop
    while(game_is_on):
        # Get current ball position
        new_x = ball.pos()[0]
        new_y = ball.pos()[1]

        # Detect wall collision
        wall_hit, hit = ball.detect_wall_collision()

        # Check if the ball is in a goal
        is_goal, goal_owner = ball.check_goal()
        gameboard.update()

        # Bounce on wall collision
        if(wall_hit):
            new_x, new_y, speed_x, speed_y = ball.bounce_on_wall(
                hit,  new_x, new_y, speed_x, speed_y)

        # Handle goal events
        elif(is_goal):
            print(" >>  Restarting game")

            # Update scores
            if(goal_owner == "R"):
                score_R += 1
            elif(goal_owner == "L"):
                score_L += 1

            # Reset ball position and update scoreboard
            ball.setpos(0, 0)
            speed_x = random.randrange(-2, 2, 1)
            speed_y = random.randrange(-3, 3, 1)
            scoreboard.goal_done(score_l=score_L, score_r=score_R)
            if(speed_x == 0):
                speed_x += 1
            if(speed_y == 0):
                speed_y -= 1
        # Check paddle collisions
        else:
            hit_on_paddle = ball.check_paddle_hit(
                paddle_R.pos(), paddle_L.pos())

            # Bounce on paddle collision
            if(hit_on_paddle == "hit_R_paddle"):
                new_x, new_y, speed_x, speed_y = ball.bounce_from_paddle(
                    "R",  new_x, new_y, speed_x, speed_y)
            elif(hit_on_paddle == "hit_L_paddle"):
                new_x, new_y, speed_x, speed_y = ball.bounce_from_paddle(
                    "L",  new_x, new_y, speed_x, speed_y)

            # Update ball position
            else:
                new_x += speed_x
                new_y += speed_y
                print(" >>  ball running")
                ball.update_movement(new_x, new_y)

        # Add a sleep time to control the speed of the game loop
        time.sleep(SLEEP_TIME)

    # Close the game window when the game loop ends
    gameboard.exitonclick()

# MAIN:
if __name__ == '__main__':
    # Run the main function to start the game
    main()