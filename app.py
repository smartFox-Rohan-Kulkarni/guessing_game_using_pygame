import pygame
from pygame import display, event, image
import game_cofig as gc
from animal import Animal
from time import sleep

def find_index(x, y):
    row= y // gc.IMAGE_SIZE
    col= x // gc.IMAGE_SIZE
    index = row *gc.NUM_TILES_SIDE+col
    return index

pygame.init()

display.set_caption("The Memory Game")

screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))

#load image as surface object
matched = image.load("other_assets/matched.png")
#paste surface matched on surface screen
#screen.blit(matched, (0, 0))
#refresh the screen
#display.flip()



#game loop
Running=True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images = []

while Running :
    cur_events= event.get()

    for e in cur_events:
        if e.type == pygame.QUIT:
            Running=False
    
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                Running = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y =pygame.mouse.get_pos()
            index= find_index(mouse_x, mouse_y)
            #print(index)
            if index in current_images:
                current_images.remove(index)
            else:
#                if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2 :
                current_images= current_images[1:]

    screen.fill((255,255,255))

    total_skipped = 0

    for i, tile in enumerate(tiles):
        image_i =tile.image if i in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col* gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped+=1
    display.flip()

    if len(current_images) ==2:
        idx1, idx2 =current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip=True
            tiles[idx2].skip=True
            sleep(0.4)
            screen.blit(matched,(0 ,0))
            display.flip()
            sleep(0.4)
            current_images=[]    
    
    if total_skipped==len(tiles):
        screen.fill((64,255,25))
        display.flip()
        Running=False

print("Game terminated!")