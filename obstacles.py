from turtle import Turtle

colors = ["blue", "green", "red", "yellow"]


class Blocks(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.penup()
        self.goto(position)
        self.x_pos = -335
        self.y_pos = 50
