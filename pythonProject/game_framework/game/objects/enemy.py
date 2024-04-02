from game_framework.game.objects.game_object import GameObject


class Enemy(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def update(self):
        # Add enemy-specific update logic here
        pass

    def draw(self):
        # Add enemy-specific drawing logic here
        pass
