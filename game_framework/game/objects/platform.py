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

    def intersects_vertical(self, other):
        # Check if the bounding boxes of the two objects intersect
        return (abs(self.turtle.xcor() - other.turtle.xcor()) * 2 < (self.width + other.width)) and \
            (abs(self.turtle.ycor() - other.turtle.ycor()) * 2 < (self.height + other.height))

    def intersects_horizontal(self, other, new_x):
        # Check if the player intersects horizontally with the platform
        return (abs(self.turtle.ycor() - other.turtle.ycor()) * 2 < (self.height + other.height)) and \
            (abs(new_x - self.turtle.xcor()) * 2 < (self.width + other.width))

    def left_edge(self):
        return self.turtle.xcor() - self.width / 2

    def right_edge(self):
        return self.turtle.xcor() + self.width / 2

    def top_height(self):
        return self.turtle.ycor() + self.height / 2

    def bottom_height(self):
        return self.turtle.ycor() - self.height / 2
