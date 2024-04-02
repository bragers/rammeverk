import turtle


class GameWindow:
    def __init__(self, width, height, title="Simple Game", bgcolor="black"):
        self.window = turtle.Screen()
        self.window.title(title)
        self.window.setup(width=width, height=height)
        self.window.bgcolor(bgcolor)
        self.window.tracer(0)  # Disable automatic window updates

        self.turtle = turtle.Turtle()
        self.turtle.color("white")  # Set turtle color to white
        self.turtle.penup()  # Lift pen to avoid drawing lines initially
        self.turtle.goto(0, 0)  # Move turtle to the center of the screen
        self.turtle.shape("turtle")

    def update(self):
        self.window.update()

    def run(self):
        while True:
            self.update()
            # Add your game logic here
