import os
import random
import game_cofig as gc

from pygame import image, transform

animals_count = dict((a, 0) for a in gc.ASSET_FILES)

def available_animals():
    return [a for a, c in animals_count.items() if c < 2]

class Animal:
    def __init__(self, index):
        self.index= index
        self.row = index//gc.NUM_TILES_SIDE
        self.col= index % gc.NUM_TILES_SIDE
        self.name = random.choice(available_animals())
        animals_count[self.name]+=1

        self.image_path=os.path.join(gc.ASSET_DIR, self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2*gc.MARGIN, gc.IMAGE_SIZE - 2*gc.MARGIN))
        self.box=self.image.copy()
        self.box.fill((200,200,200))
        self.skip = False