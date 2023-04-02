from turtle import Turtle
import configFile

# Import paddle and gameboard dimensions from the configuration file
PADDLE_H = configFile.PADDLE_H
PADDLE_W = configFile.PADDLE_W
GAMEBOARD_W = configFile.GAMEBOARD_W
GAMEBOARD_H = configFile.GAMEBOARD_H


class Paddle(Turtle):
    """
    Paddle class represents a paddle in the game.
    Inherits from the Turtle class.
    """

    def __init__(self, X, Y):
        """
        Initialize a new paddle instance.

        :param X: x-coordinate of the paddle
        :param Y: y-coordinate of the paddle
        """
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=PADDLE_W / 2, stretch_wid=PADDLE_H)
        self.X = X
        self.Y = Y
        self.setpos(self.X, self.Y)

    def move_up(self):
        """
        Move the paddle up by 10 units if it is within the gameboard.
        """
        new_x = self.pos()[0]
        if self.pos()[1] >= GAMEBOARD_H / 2 - PADDLE_H * 20 / 2:
            new_y = self.pos()[1]
        else:
            new_y = self.pos()[1] + 10

        self.setpos(new_x, new_y)

    def move_down(self):
        """
        Move the paddle down by 10 units if it is within the gameboard.
        """
        new_x = self.pos()[0]
        if self.pos()[1] <= -GAMEBOARD_H / 2 + PADDLE_H * 20 / 2:
            new_y = self.pos()[1]
        else:
            new_y = self.pos()[1] - 10
        self.setpos(new_x, new_y)
