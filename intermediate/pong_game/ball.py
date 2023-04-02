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

        if(d_x_R and d_y_R):
            # HIT R
            return "hit_R_paddle"
        elif(d_x_L and d_y_L):
            # HIT L:
            return "hit_L_paddle"
        pass

    def bounce_from_paddle(self, bounce_side, new_x, new_y, speed_x, speed_y):
        if(bounce_side == "R" or bounce_side == "L"):
            speed_x *= -1
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
import random
from turtle import Turtle
import configFile

# Load configuration values from configFile
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

    def detect_wall_collision(self):
        """Detects collision with top or bottom walls."""
        if self.pos()[1] >= GAMEBOARD_H/2-10:
            return True, "up_hit"
        elif self.pos()[1] <= -GAMEBOARD_H/2+10:
            return True, "down_hit"
        else:
            return False, None

    def bounce_on_wall(self, hit, new_x, new_y, speed_x, speed_y):
        """Calculates new position and speed after bouncing on a wall."""
        new_x = self.pos()[0]
        new_y = self.pos()[1]

        if hit == "up_hit" or hit == "down_hit":
            speed_y *= -1

        new_x += speed_x
        new_y += speed_y
        self.update_movement(new_x, new_y)

        return new_x, new_y, speed_x, speed_y

    def check_paddle_hit(self, pad_pos_R, pad_pos_L):
        """Checks if the ball has hit either paddle."""
        d_x_R = self.pos()[0] == pad_pos_R[0]-10
        d_x_L = self.pos()[0] == pad_pos_L[0]+10

        d_y_R = (self.pos()[1] < pad_pos_R[1] + 20 * PADDLE_H-35 and
                 self.pos()[1] > pad_pos_R[1] - 20 * PADDLE_H+35)
        d_y_L = (self.pos()[1] < pad_pos_L[1] + 20 * PADDLE_H-35 and
                 self.pos()[1] > pad_pos_L[1] - 20 * PADDLE_H+35)

        if d_x_R and d_y_R:
            return "hit_R_paddle"
        elif d_x_L and d_y_L:
            return "hit_L_paddle"

    def bounce_from_paddle(self, bounce_side, new_x, new_y, speed_x, speed_y):
        """Calculates new position and speed after bouncing off a paddle."""
        if bounce_side == "R" or bounce_side == "L":
            speed_x *= -1

        new_y += speed_y
        new_x += speed_x
        self.update_movement(new_x, new_y)

        return new_x, new_y, speed_x, speed_y

    def update_movement(self, new_x, new_y):
        """Updates the ball's position on the screen."""
        self.setpos(new_x, new_y)

    def check_goal(self):
        """Checks if a goal has been scored by either player."""
        if self.pos()[0] > GAMEBOARD_W/2:
            return True, "L"
        elif self.pos()[0] < -GAMEBOARD_W/2:
            return True, "R"
        else:
            return False, None
