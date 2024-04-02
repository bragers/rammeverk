from game_framework.game.game import Game
from game_framework.game.objects.player import Player
from game_framework.game.objects.platform import Platform
from game_framework.game.objects.enemy import Enemy


def main():
    # Create a game instance
    game_instance = Game()

    # Create game objects
    player = Player(100, 100, 50, 50)
    platform = Platform(200, 300, 200, 30)
    enemy = Enemy(400, 200, 50, 50)

    # Add game objects to the game
    game_instance.add_game_object(player)
    game_instance.add_game_object(platform)
    game_instance.add_game_object(enemy)

    # Run the game
    game_instance.run()


if __name__ == "__main__":
    main()
