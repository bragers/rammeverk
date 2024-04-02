import turtle


class GameWindow:
    def __init__(self, width, height, title="Simple Game", bgcolor="black"):
        self.window = turtle.Screen()
        self.window.title(title)
        self.window.setup(width=width, height=height)
        self.window.bgcolor(bgcolor)
        self.window.tracer(0)  # Disable automatic window updates
