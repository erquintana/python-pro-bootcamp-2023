import random
from turtle import Turtle
import configFile

BALL_W = configFile.BALL_W
BALL_H = configFile.BALL_H
BALL_SPEED = configFile.BALL_SPEED
GAMEBOARD_W = configFile.GAMEBOARD_W
GAMEBOARD_H = configFile.GAMEBOARD_H
PADDLE_H = configFile.PADDLE_H
PADDLE_W = configFile.PADDLE_W


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("navy")
        self.speed(BALL_SPEED)
        self.setpos(0, 0)

    # def wall_bounce(self, ball_x, ball_y, speed_x, speed_y):
    #     if(ball_x < -GAMEBOARD_W/2+10 or ball_x > GAMEBOARD_W/2):
    #         speed_x *= -1
    #     if(ball_y < -GAMEBOARD_H/2 or ball_y > GAMEBOARD_H/2):
    #         speed_y *= -1
    #     ball_x += speed_x
    #     ball_y += speed_y
    #     self.setpos(ball_x, ball_y)
    #     return speed_x, speed_y

    def detect_wall_collision(self):
        # if hit wall:
        if(self.pos()[1] >= GAMEBOARD_H/2):
            print(" >>  Up wall collision")
            return True, "up_hit"
        elif(self.pos()[1] <= -GAMEBOARD_H/2):
            print(" >>  Down wall collision")
            return True, "down_hit"
        else:
            return False, None

    def bounce_on_wall(self, hit, new_x, new_y, speed_x, speed_y):
        new_x = self.pos()[0]
        new_y = self.pos()[1]
        if(hit == "up_hit" or hit == "down_hit"):
            print(" >>  bouncing on wall")
            speed_y *= -1
        new_x += speed_x
        new_y += speed_y
        self.update_movement(new_x, new_y)
        return new_x, new_y, speed_x, speed_y

    def check_paddle_hit(self, pad_pos_R, pad_pos_L):
        d_x_R = (self.pos()[0] == pad_pos_R[0])
        d_x_L = (self.pos()[0] == pad_pos_L[0])

        d_y_R = (self.pos()[1] < pad_pos_R[1] + 20 *
                 PADDLE_H and self.pos()[1] > pad_pos_R[1] - 20*PADDLE_H)
        d_y_L = (self.pos()[1] < pad_pos_L[1] + 20 *
                 PADDLE_H and self.pos()[1] > pad_pos_L[1] - 20*PADDLE_H)

       # print(f"\td_x : {d_x}\t,\td_y : {d_y}")
        if(d_x_R and d_y_R):
            # HIT R
            return "hit_R_paddle"
        elif(d_x_L and d_y_L):
            # HIT L:
            return "hit_L_paddle"
        pass

    def bounce_from_paddle(self, bounce_side, new_x, new_y, speed_x, speed_y):
        if(bounce_side == "R" or bounce_side == "L"):
            speed_x *= -1*random.randint(1, 3)
            print(" >>  Hit paddle!!")
        new_y += speed_y
        new_x += speed_x
        self.update_movement(new_x, new_y)
        return new_x, new_y, speed_x, speed_y

    def update_movement(self, new_x, new_y):
        self.setpos(new_x, new_y)

    def check_goal(self):
        if(self.pos()[0] > GAMEBOARD_W/2):
            print(" >>>  LEFT PLAYER GOAL!!")
            return True, "L"
        elif(self.pos()[0] < -GAMEBOARD_W/2):
            print(" >>>  RIGHT PLAYER GOAL!!")
            return True, "R"
        else:
            return False, None
