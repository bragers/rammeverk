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
        self.gravity = 1  # Adjust gravity as needed
        self.fall_speed = -5  # Constant downward velocity
        self.max_jump_height = 100  # Maximum height of the jump
        self.is_jumping = False
        self.y_velocity = 0
        self.jump_start_y = 0
        self.x_velocity = 0
        self.setup_input_handling()
        self.is_grounded = False
        self.last_platform = None

    def setup_input_handling(self):
        self.screen = self.turtle.getscreen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkey(self.move_stop, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkey(self.move_stop, "Right")
        self.screen.onkeypress(self.jump, "Up")
        self.screen.listen()

    def move_left(self):
        self.x_velocity = -15

    def move_right(self):
        self.x_velocity = 15

    def move_stop(self):
        self.x_velocity = 0

    def apply_gravity(self):
        if not self.is_grounded:  # Apply gravity only if the player is not grounded
            self.y_velocity = max(self.fall_speed, self.y_velocity - self.gravity)

    def update(self, platforms):
        # Apply gravity
        self.apply_gravity()

        # Update player horizontal position
        new_x = self.turtle.xcor() + self.x_velocity
        max_x = self.screen.window_width() / 2 - self.width / 2
        min_x = -self.screen.window_width() / 2 + self.width / 2

        if min_x < new_x < max_x:
            self.turtle.setx(new_x)

        # Update player vertical position
        new_y = self.turtle.ycor() + self.y_velocity
        self.turtle.sety(new_y)

        # Check for collision with platforms
        for platform in platforms:
            if platform.intersects(self):
                if self.y_velocity < 0:  # Player is moving downwards
                    self.is_grounded = True
                    self.is_jumping = False
                    self.y_velocity = 0
                    self.turtle.sety(platform.top_height() + self.height / 2)
                    self.last_platform = platform  # Update last platform
                elif self.y_velocity > 0:  # Player is moving upwards
                    self.is_grounded = False
                    self.y_velocity = 0
                    self.turtle.sety(platform.bottom_height() - self.height / 2)

                # Check if player is still on the platform horizontally
                if not (platform.left_edge() < self.turtle.xcor() < platform.right_edge()):
                    self.is_grounded = False

        # Activate gravity if not on the last platform horizontally
        if self.last_platform:
            if not (self.last_platform.left_edge() < self.turtle.xcor() < self.last_platform.right_edge()):
                self.is_grounded = False
                self.last_platform = None

        # Adjust jumping behavior
        if self.is_jumping and self.turtle.ycor() >= self.jump_start_y + self.max_jump_height:
            self.is_jumping = False
            self.is_grounded = False

    def jump(self):
        self.is_jumping = True
        self.jump_start_y = self.turtle.ycor()
        self.y_velocity = self.jump_speed

    def draw(self):
        pass

    @classmethod
    def create_player(cls, **kwargs):
        return cls(**kwargs)
