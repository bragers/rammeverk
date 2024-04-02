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
        # Shrink the collision border by a certain factor (e.g., 0.9)
        shrink_factor = 0.9
        x_overlap = (abs(self.turtle.xcor() - other.turtle.xcor()) * 2 < (self.width * shrink_factor +
                                                                          other.width * shrink_factor))
        y_overlap = (abs(self.turtle.ycor() - other.turtle.ycor()) * 2 < (self.height * shrink_factor +
                                                                          other.height * shrink_factor))
        return x_overlap and y_overlap

    def draw(self):
        # No need to draw the platform separately since it's a turtle
        pass
