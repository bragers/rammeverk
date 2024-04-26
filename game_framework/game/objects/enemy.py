import turtle  # Importing the turtle module for graphics


class Enemy:
    def __init__(self, x, y, shape="square", color="red", width=20, height=20):
        """
        Constructor for the Enemy class.

        Args:
        x (int): x-coordinate for the enemy's starting position.
        y (int): y-coordinate for the enemy's starting position.
        shape (str): The shape of the enemy (default is "square").
        color (str): The color of the enemy (default is "red").
        width (int): Width of the enemy's shape (default is 20).
        height (int): Height of the enemy's shape (default is 20).
        """
        # Creating a turtle object for the enemy
        self.turtle = turtle.Turtle()

        # Setting the shape, color, width, and height of the enemy
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.penup()

        # Moving the enemy to its initial position
        self.turtle.goto(x, y)

        # Storing width and height for potential future use
        self.width = width
        self.height = height

