import turtle  # Importing the turtle module for graphics


class GameWindow:
    def __init__(self, width, height, title="Simple Game", bgcolor="black"):
        """
        Constructor for the GameWindow class.

        Args:
        width (int): Width of the game window.
        height (int): Height of the game window.
        title (str): Title of the game window (default is "Simple Game").
        bgcolor (str): Background color of the game window (default is "black").
        """
        # Creating the game window
        self.window = turtle.Screen()

        # Setting window title, size, and background color
        self.window.title(title)
        self.window.setup(width=width, height=height)
        self.window.bgcolor(bgcolor)
