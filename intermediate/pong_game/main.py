from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from turtle import Screen
import time
import random
import configFile

GAMEBOARD_W = configFile.GAMEBOARD_W
GAMEBOARD_H = configFile.GAMEBOARD_H
SLEEP_TIME = configFile.SLEEP_TIME


def main():
    score_L = 0
    score_R = 0
    gameboard = Screen()
    gameboard.setup(width=GAMEBOARD_W, height=GAMEBOARD_H)
    gameboard.bgcolor("light steel blue")
    gameboard.title("PONG GAME")
    gameboard.tracer(0)

    ball = Ball()
    scoreboard = Scoreboard()

    paddle_R = Paddle(X=GAMEBOARD_W/2-20, Y=0)
    paddle_L = Paddle(X=-GAMEBOARD_W/2+20, Y=0)

    gameboard.listen()
    gameboard.onkeypress(paddle_R.move_up, "Up")
    gameboard.onkeypress(paddle_R.move_down, "Down")
    gameboard.onkeypress(paddle_L.move_up, "w")
    gameboard.onkeypress(paddle_L.move_down, "s")

    game_is_on = True

    speed_x = 1
    speed_y = 1
    ball.heading = random.randrange(0, 360, 45)
    while(game_is_on):
        new_x = ball.pos()[0]
        new_y = ball.pos()[1]
        wall_hit, hit = ball.detect_wall_collision()
        is_goal, goal_owner = ball.check_goal()
        gameboard.update()
        if(wall_hit):
            new_x, new_y, speed_x, speed_y = ball.bounce_on_wall(
                hit,  new_x, new_y, speed_x, speed_y)
        elif(is_goal):
            print(" >>  Restarting game")
            if(goal_owner == "R"):
                score_R += 1
            elif(goal_owner == "L"):
                score_L += 1
            ball.setpos(0, 0)
            scoreboard.goal_done(score_l=score_L, score_r=score_R)
        else:
            hit_on_paddle = ball.check_paddle_hit(
                paddle_R.pos(), paddle_L.pos())
            if(hit_on_paddle == "hit_R_paddle"):
                new_x, new_y, speed_x, speed_y = ball.bounce_from_paddle(
                    "R",  new_x, new_y, speed_x, speed_y)
            elif(hit_on_paddle == "hit_L_paddle"):
                new_x, new_y, speed_x, speed_y = ball.bounce_from_paddle(
                    "L",  new_x, new_y, speed_x, speed_y)
            else:
                new_x += speed_x
                new_y += speed_y
                print(" >>  ball running")
                ball.update_movement(new_x, new_y)

        time.sleep(SLEEP_TIME)

    gameboard.exitonclick()


# MAIN:
if __name__ == '__main__':
    main()
