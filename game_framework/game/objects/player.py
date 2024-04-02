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
        self.fall_speed = -5  # Constant downward velocity
        self.max_jump_height = 100  # Maximum height of the jump
        self.is_jumping = False
        self.y_velocity = 0
        self.jump_start_y = 0

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
            self.jump_start_y = self.turtle.ycor()
            self.y_velocity = self.jump_speed

    def apply_gravity(self):
        if not self.is_jumping:
            self.y_velocity = max(self.fall_speed, self.y_velocity - self.gravity)

    def update(self, platforms):
        # Apply gravity
        self.apply_gravity()

        # Update player position
        new_y = self.turtle.ycor() + self.y_velocity
        if new_y > -self.screen.window_height() / 2 + self.height / 2:
            self.turtle.sety(new_y)
        else:
            self.is_jumping = False  # Stop jumping if reaching the top edge of the window
            self.turtle.sety(-self.screen.window_height() / 2 + self.height / 2)

        # Check for collision with platforms
        for platform in platforms:
            if platform.intersects(self):
                self.is_jumping = False
                self.y_velocity = 0  # Stop falling when hitting a platform
                self.turtle.sety(platform.turtle.ycor() + platform.height / 2 + self.height / 2)

        # Adjust jumping behavior
        if self.is_jumping and self.turtle.ycor() - self.jump_start_y >= self.max_jump_height:
            self.is_jumping = False
            self.y_velocity = 0

    def draw(self):
        pass

    @classmethod
    def create_player(cls, **kwargs):
        return cls(**kwargs)
