class Game:
    def __init__(self):
        """
        Constructor for the Game class.
        """
        # List to store game objects
        self.game_objects = []

    def add_game_object(self, game_object):
        """
        Add a game object to the game.

        Args:
        game_object: An object representing a game element.
        """
        # Append the game object to the list
        self.game_objects.append(game_object)

    def update(self):
        """
        Update the state of all game objects.
        """
        # Iterate over each game object and update its state
        self.game_objects = []

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def update(self):
        for obj in self.game_objects:
            obj.update()

    def draw(self):
        """
        Draw all game objects.
        """
        # Iterate over each game object and draw it
        for obj in self.game_objects:
            obj.draw()

    def run(self):
        """
        Run the game loop.
        """
        running = True
        while running:
            # Update the game state
            self.update()

            # Draw the game objects
        running = True
        while running:
            self.update()
            self.draw()
