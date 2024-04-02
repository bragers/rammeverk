import turtle
from game_framework.game.objects.player import Player
from game_framework.game.objects.platform import Platform


class Game:
    def __init__(self, width, height):
        self.screen = turtle.Screen()
        self.screen.setup(width=width, height=height)
        self.screen.title("2D Platformer Game")
        self.screen.bgcolor("black")

        self.player = Player.create_player(x=-100, y=25)  # Adjust player initial position

        # Create platforms
        self.platforms = [
            Platform(x=-100, y=-50, width=200, height=20),
            Platform(x=0, y=100, width=150, height=20),
            # Add more platforms as needed
        ]

    def update(self):
        # Runs the player.update function, using self.platforms as a parameter to tell it what platforms exist for collision purposes
        self.player.update(self.platforms)

    def draw(self):
        self.player.draw()
        for platform in self.platforms:
            platform.draw()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.screen.update()


if __name__ == "__main__":
    game = Game(width=800, height=600)
    game.run()
