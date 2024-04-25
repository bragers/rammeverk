import turtle
from game_framework.game.objects.player import Player
from game_framework.game.objects.platform import Platform
from game_framework.game.objects.enemy import Enemy


class Game:
    widthVar = 0
    heightVar = 0

    def start_game(self, width, height):
        self.widthVar = width
        self.heightVar = height
        self.screen = turtle.Screen()
        self.screen.setup(width=width, height=height)
        self.screen.title("2D Platformer Game")
        self.screen.bgcolor("black")

        self.player = Player.create_player(x=-100, y=25, jump_speed=15)  # Adjust player initial position

        # Create platforms
        self.platforms = [
            Platform(x=-100, y=-60, width=2000, height=40),
            Platform(x=0, y=100, width=150, height=20),
            Platform(x=150, y=120, width=150, height=20),
            # Add more platforms as needed
        ]

        # Create enemies
        self.enemies = [
            Enemy(x=-50, y=-30),
            Enemy(x=0, y=-30),
            Enemy(x=-200, y=-30),
            Enemy(x=100, y=-30),
            Enemy(x=200, y=-30),
            Enemy(x=-200, y=-30),
            # Add more enemies as needed
        ]

    def __init__(self, width, height):
        self.player = None
        self.screen = None
        self.enemies = None
        self.platforms = None
        self.start_game(width, height)

    def update(self):
        # Runs the player.update function, using self.platforms as a parameter to tell it what platforms exist for
        # collision purposes
        self.player.update(self.platforms)

        for enemy in self.enemies:
            if self.player.collide_with_enemy(enemy):
                self.restart_game()

    def restart_game(self):
        # Reset player and enemies to initial positions
        # self.player.turtle.goto(-100, 25)
        self.screen.clear()
        self.start_game(self.widthVar, self.heightVar)

    def run(self):

        jump_count = 0

        while True:
            self.update()
            self.screen.update()


if __name__ == "__main__":
    game = Game(width=800, height=600)
    game.run()
