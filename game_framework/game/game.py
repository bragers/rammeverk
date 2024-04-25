class Game:
    def __init__(self):
        self.game_objects = []

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def update(self):
        for obj in self.game_objects:
            obj.update()

    def draw(self):
        for obj in self.game_objects:
            obj.draw()

    def run(self):
        running = True
        while running:
            self.update()
            self.handle_collisions()
            self.draw()
