import pygame
from pygame import *

import os, math

# def load_sliced_sprites(w, h, filename):
#     '''
#     Specs :
#     	Master can be any height.
#     	Sprites frames width must be the same width
#     	Master width must be len(frames)*frame.width
#     Assuming you ressources directory is named "ressources"
#     '''
#     images = []
#     master_image = pygame.image.load(os.path.join('sprites', filename)).convert_alpha()

#     master_width, master_height = master_image.get_size()
#     for i in range(int(master_width/w)):
#     	images.append(master_image.subsurface((i*w,0,w,h)))
#     return images

def load_2d_sheets(w, h, filename):
    '''
    Specs :
    	Sprites frames width must be the same width
    	Master height must be height(frames)*frame.height
    	Master width must be len(frames)*frame.width
    Assuming you ressources directory is named "ressources"
    '''
    images = []
    master_image = pygame.image.load(os.path.join('sprites', filename)).convert_alpha()

    cnt = 0
    master_width, master_height = master_image.get_size()
    print(master_width, ":", master_height, "->", int(master_width/w), ":", int(master_height/h))
    for j in range(int(master_height/h)):
        for i in range(int(master_width/w)):
            print(j, ":", i)
            images.append(master_image.subsurface((i*w,j*h,w,h)))
    
    for img in images:
        cnt+=1
        print(cnt)
        fileName = "image#" + str(cnt) + ".bmp"
        pygame.image.save(img, fileName)
    
    return images
