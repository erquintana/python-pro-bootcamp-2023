from turtle import Turtle
import configFile
import time

ALIGNMENT = "center"
FONT_TYPE = "Arial"
FONT_SIZE = 9
FORT_STYLE = "bold"
GAMEBOARD_W = configFile.GAMEBOARD_W
GAMEBOARD_H = configFile.GAMEBOARD_H


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.clear()
        self.goto(-GAMEBOARD_W/4, 270)
        self.write(f"SCORE L player: 0", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))
        self.goto(GAMEBOARD_W/4, 270)
        self.write(f"SCORE R player: 0", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))
        self.hideturtle()

    def update_score(self, score_l, score_r):
        self.goto(GAMEBOARD_W/4, 270)
        self.write(f"SCORE R player: {score_r}", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))
        self.goto(-GAMEBOARD_W/4, 270)
        self.write(f"SCORE R player: {score_l}", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))

    # TODO: here we should know how goals
    def goal_done(self, score_l, score_r):
        self.goto(0, 0)
        self.write(f"GOOOOAL!!! Let's go again!", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE*3, FORT_STYLE))
        time.sleep(3)
        self.clear()
        self.update_score(score_l, score_r)
