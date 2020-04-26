# Explosion
# Demonstrates creating an animation

import sys, os, math
from superwires import games
from spriteUtils import *

filename = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

games.init(screen_width =  640, screen_height = 480, fps = 50)

animation_list = load_2d_sheets(x, y, filename)
print(animation_list)

# print(str(animation_list))


