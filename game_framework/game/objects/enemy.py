import turtle


class Enemy:
    def __init__(self, x, y, shape="square", color="red", width=20, height=20, gravity=0, move_speed=0):
        self.turtle = turtle.Turtle()
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.width = width
        self.height = height

    def update(self, platforms):
        # Move the enemy
        pass

        # Check for collision with platforms





    def reset_position(self):
        pass