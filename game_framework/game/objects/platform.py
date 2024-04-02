from game_framework.game.objects.game_object import GameObject

import turtle


class Platform:
    def __init__(self, x, y, width, height, color="gray"):
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.shapesize(stretch_wid=height / 20, stretch_len=width / 20)
        self.width = width
        self.height = height

    def intersects(self, other):
        # Check if the bounding boxes of the two objects intersect
        return (abs(self.turtle.xcor() - other.turtle.xcor()) * 2 < (self.width + other.width)) and \
            (abs(self.turtle.ycor() - other.turtle.ycor()) * 2 < (self.height + other.height))

    def draw(self):
        # No need to draw the platform separately since it's a turtle
        pass
