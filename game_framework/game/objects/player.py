from game_framework.game.objects.game_object import GameObject

import turtle


class Player:
    def __init__(self, x=0, y=0, width=20, height=20, color="white"):
        self.screen = None
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.width = width
        self.height = height
        self.jump_speed = 10  # Adjust jump speed as needed
        self.gravity = 0.5  # Adjust gravity as needed
        self.is_jumping = False
        self.y_velocity = 0

        self.setup_input_handling()

    def setup_input_handling(self):
        self.screen = self.turtle.getscreen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.jump, "Up")
        self.screen.listen()

    def move_left(self):
        self.turtle.setx(self.turtle.xcor() - 10)  # Adjust the movement speed as needed

    def move_right(self):
        self.turtle.setx(self.turtle.xcor() + 10)  # Adjust the movement speed as needed

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = self.jump_speed

    def update(self):
        if self.is_jumping:
            self.turtle.sety(self.turtle.ycor() + self.y_velocity)
            self.y_velocity -= self.gravity
            if self.turtle.ycor() <= 0:  # Adjust the condition as needed
                self.is_jumping = False
                self.turtle.sety(0)

    def draw(self):
        # No need to draw the player separately since it's a turtle
        pass

    @classmethod
    def create_player(cls):
        return cls()
