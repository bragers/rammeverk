import turtle  # Importing the turtle module for graphics


class Platform:
    def __init__(self, x, y, width, height, color="gray"):
        """
        Constructor for the Platform class.

        Args:
        x (int): x-coordinate for the platform's starting position.
        y (int): y-coordinate for the platform's starting position.
        width (int): Width of the platform.
        height (int): Height of the platform.
        color (str): The color of the platform (default is "gray").
        """
        # Creating a turtle object for the platform
        self.turtle = turtle.Turtle()

        # Setting the shape, color, and initial position of the platform
        self.turtle.shape("square")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)

        # Scaling the platform to the specified width and height
        self.turtle.shapesize(stretch_wid=height / 20, stretch_len=width / 20)

        # Storing width and height for potential future use
        self.width = width
        self.height = height

    def intersects_vertical(self, other):
        """
        Check if the platform intersects vertically with another object.

        Args:
        other (Platform): Another platform object to check intersection with.

        Returns:
        bool: True if the platforms intersect vertically, False otherwise.
        """
        # Check if the bounding boxes of the two objects intersect vertically
        return (abs(self.turtle.xcor() - other.turtle.xcor()) * 2 < (self.width + other.width)) and \
            (abs(self.turtle.ycor() - other.turtle.ycor()) * 2 < (self.height + other.height))

    def intersects_horizontal(self, other, new_x):
        """
        Check if the platform intersects horizontally with another object.

        Args:
        other (Platform): Another platform object to check intersection with.
        new_x (int): The x-coordinate of the object after a potential horizontal movement.

        Returns:
        bool: True if the platforms intersect horizontally, False otherwise.
        """
        # Check if the bounding boxes of the two objects intersect horizontally
        return (abs(self.turtle.ycor() - other.turtle.ycor()) * 2 < (self.height + other.height)) and \
            (abs(new_x - self.turtle.xcor()) * 2 < (self.width + other.width))

    def left_edge(self):
        """
        Get the x-coordinate of the left edge of the platform.

        Returns:
        int: The x-coordinate of the left edge.
        """
        return self.turtle.xcor() - self.width / 2

    def right_edge(self):
        """
        Get the x-coordinate of the right edge of the platform.

        Returns:
        int: The x-coordinate of the right edge.
        """
        return self.turtle.xcor() + self.width / 2

    def top_height(self):
        """
        Get the y-coordinate of the top edge of the platform.

        Returns:
        int: The y-coordinate of the top edge.
        """
        return self.turtle.ycor() + self.height / 2

    def bottom_height(self):
        """
        Get the y-coordinate of the bottom edge of the platform.

        Returns:
        int: The y-coordinate of the bottom edge.
        """
        return self.turtle.ycor() - self.height / 2
