from turtle import Turtle
from snake import Snake
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    
    def refresh(self):
        rand_x = random.randint(-280/20, 280/20)
        rand_y = random.randint(-280/20, 280/20)
        self.goto(rand_x*20, rand_y*20)