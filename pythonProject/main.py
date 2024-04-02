from game_framework.game_window import GameWindow


def main():
    # Create a GameWindow instance
    game_window = GameWindow(width=800, height=600)

    # Run the game
    game_window.run()


if __name__ == "__main__":
    main()
