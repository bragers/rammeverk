import turtle
from game_framework.game.objects.player import Player


class Game:
    def __init__(self, width, height):
        self.screen = turtle.Screen()
        self.screen.setup(width=width, height=height)
        self.screen.title("2D Platformer Game")
        self.screen.bgcolor("black")

        self.player = Player.create_player()  # Create player object using class method

    def update(self):
        # Update game state
        self.player.update()
        # Add more update logic for other game objects

    def draw(self):
        self.player.draw()
        # Add more drawing logic for other game objects

    def run(self):
        while True:
            self.update()
            self.draw()
            self.screen.update()


if __name__ == "__main__":
    game = Game(width=800, height=600)
    game.run()
