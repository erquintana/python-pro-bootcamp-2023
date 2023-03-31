from turtle import Turtle
ALIGNMENT = "center"
FONT_TYPE = "Arial"
FONT_SIZE = 9
FORT_STYLE = "bold"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.goto(0, 270)
        self.penup()
        self.clear()
        self.write(f"SCORE: 0", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))
        self.hideturtle()

    def update_score(self, cnt):
        self.clear()
        self.write(f"SCORE: {cnt}", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE, FORT_STYLE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT,
                   font=(FONT_TYPE, FONT_SIZE*3, FORT_STYLE))
