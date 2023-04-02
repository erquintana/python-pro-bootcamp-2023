from turtle import Turtle
import configFile
import time

# Import configuration values from the configFile
ALIGNMENT = configFile.ALIGNMENT
FONT_TYPE = configFile.FONT_TYPE
FONT_SIZE = configFile.FONT_SIZE
FORT_STYLE = configFile.FORT_STYLE
GAMEBOARD_W = configFile.GAMEBOARD_W
GAMEBOARD_H = configFile.GAMEBOARD_H


class Scoreboard(Turtle):
    """
    A class representing the scoreboard for the game.
    Inherits from Turtle class.
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.clear()
        self.goto(-GAMEBOARD_W/4, 270)
        # Display the initial score for the left player
        self.write(f"SCORE L player: 0", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))
        self.goto(GAMEBOARD_W/4, 270)
        # Display the initial score for the right player
        self.write(f"SCORE R player: 0", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))
        self.hideturtle()

    def update_score(self, score_l, score_r):
        """
        Update the scores displayed on the scoreboard.

        :param score_l: The score of the left player.
        :param score_r: The score of the right player.
        """
        self.goto(GAMEBOARD_W/4, 270)
        self.write(f"SCORE R player: {score_r}", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))
        self.goto(-GAMEBOARD_W/4, 270)
        self.write(f"SCORE R player: {score_l}", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))

    def goal_done(self, score_l, score_r):
        """
        Display a message when a goal is scored and update the scoreboard.

        :param score_l: The score of the left player.
        :param score_r: The score of the right player.
        """
        self.goto(0, 0)
        self.write(f"GOOOOAL!!! Let's go again!", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE*3, FORT_STYLE))
        time.sleep(3)  # Wait for 3 seconds
        self.clear()  # Clear the screen
        self.update_score(score_l, score_r)  # Update the scoreboard with new scores
