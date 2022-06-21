from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score_l = 0
        self.score_r = 0
        self.color('white')
        self.goto(x=0, y=330)
        self.write(arg=f"Score {self.score_l}:{self.score_r}", align='center', font=('OCR-B 10 BT', 14, 'normal'))

    def point_to_l(self):
        self.score_l += 1
        self.clear()
        self.write(arg=f"Score {self.score_l}:{self.score_r}", align='center', font=('OCR-B 10 BT', 14, 'normal'))

    def point_to_r(self):
        self.score_r += 1
        self.clear()
        self.write(arg=f"Score {self.score_l}:{self.score_r}", align='center', font=('OCR-B 10 BT', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Score {self.score_l}:{self.score_r}", align='center', font=('OCR-B 10 BT', 14, 'normal'))
