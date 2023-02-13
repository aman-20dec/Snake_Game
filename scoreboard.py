from tkinter import font
from turtle import Turtle

FILE = "data.txt"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.print_score()
        self.hideturtle()
        
     
    def increase_score(self):
        
        self.score += 1
        self.print_score()
        
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE, mode="w") as file:
                file.write(f"{self.high_score}")

        # self.goto(0,0)
        # self.write(f"GAME OVER.",  align="center", font= ("Arial", 24, "normal"))

    def read_high_score(self):
        with open(FILE) as file:
            self.high_score =  int(file.read())

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}",  align="center", font= ("Arial", 24, "normal"))

