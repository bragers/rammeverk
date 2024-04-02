from game_framework.game.objects.game_object import GameObject


class Platform(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def update(self):
        # Add platform-specific update logic here
        pass

    def draw(self):
        # Add platform-specific drawing logic here
        pass
