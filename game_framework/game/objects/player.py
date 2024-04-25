import turtle
from functools import partial


class Player:
    def __init__(self, x=0, y=0, shape="square", color="white", width=20, height=20, gravity=1, jump_speed=10, max_jumps=2, move_speed=10):
        self.screen = None
        self.turtle = turtle.Turtle()
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.width = width
        self.height = height
        self.gravity = gravity
        self.jump_speed = jump_speed
        self.jump_count = 0
        self.max_jumps = max_jumps
        self.is_jumping = False
        self.y_velocity = 0
        self.jump_start_y = 0
        self.x_velocity = 0
        self.setup_input_handling(move_speed)
        self.is_grounded = False
        self.last_platform = None

    def setup_input_handling(self, speed):
        self.screen = self.turtle.getscreen()
        self.screen.onkeypress(partial(self.move_left, -speed), "Left")
        self.screen.onkey(self.move_stop, "Left")
        self.screen.onkeypress(partial(self.move_right, speed), "Right")
        self.screen.onkey(self.move_stop, "Right")
        self.screen.onkeypress(self.jump, "Up")
        self.screen.listen()

    def move_left(self, speed):
        self.x_velocity = speed

    def move_right(self, speed):
        self.x_velocity = speed

    def move_stop(self):
        self.x_velocity = 0

    def apply_gravity(self):
        if not self.is_grounded:  # Apply gravity only if the player is not grounded
            self.y_velocity = self.y_velocity - self.gravity

    def update(self, platforms):
        # Apply gravity
        self.apply_gravity()

        # Update player horizontal position
        new_x = self.turtle.xcor() + self.x_velocity
        max_x = self.screen.window_width() / 2 - self.width / 2
        min_x = -self.screen.window_width() / 2 + self.width / 2

        if min_x <= new_x <= max_x:
            # Check for collision with platforms horizontally
            for platform in platforms:
                if platform.intersects_horizontal(self, new_x):
                    # Calculate available space to move
                    available_space = min(abs(platform.left_edge() - self.turtle.xcor()),
                                          abs(platform.right_edge() - self.turtle.xcor())) - self.width / 2
                    if available_space <= abs(self.x_velocity):
                        # Adjust new_x to move only available space
                        new_x = self.turtle.xcor() + available_space * (self.x_velocity / abs(self.x_velocity))
                    break
            self.turtle.setx(new_x)

        # Update player vertical position
        new_y = self.turtle.ycor() + self.y_velocity
        self.turtle.sety(new_y)

        # Check for collision with platforms
        for platform in platforms:
            if platform.intersects_vertical(self):
                if self.y_velocity < 0:  # Player is moving downwards
                    self.is_grounded = True
                    self.jump_count = 0
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

    def jump(self):
        if not self.is_jumping and self.jump_count < self.max_jumps:
            self.is_grounded = False
            self.jump_start_y = self.turtle.ycor()
            self.y_velocity = self.jump_speed
            self.jump_count += 1

    def collide_with_enemy(self, enemy):
        player_left = self.turtle.xcor() - self.width / 2
        player_right = self.turtle.xcor() + self.width / 2
        player_top = self.turtle.ycor() + self.height / 2
        player_bottom = self.turtle.ycor() - self.height / 2

        enemy_left = enemy.turtle.xcor() - enemy.width / 2
        enemy_right = enemy.turtle.xcor() + enemy.width / 2
        enemy_top = enemy.turtle.ycor() + enemy.height / 2
        enemy_bottom = enemy.turtle.ycor() - enemy.height / 2

        # Check for intersection between player and enemy hitboxes
        return (player_left <= enemy_right and player_right >= enemy_left and
                player_bottom <= enemy_top and player_top >= enemy_bottom)

    @classmethod
    def create_player(cls, **kwargs):
        return cls(**kwargs)
