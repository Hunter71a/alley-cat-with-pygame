# Carl Olson   Python
# CSCI-1511
# Project 1:    Playful kitten sprite
#
# A kitten can move about an alleyway


from superwires import games, color
import math
import os
import random
from pygame import *

games.init(screen_width=1200, screen_height=600, fps=50)


def load_images(path):
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The relative or absolute path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    for file_name in os.listdir(path):
        each_image = games.load_image(path + os.sep + file_name).convert()
        images.append(each_image)
    return images


class SpriteCorral(games.Sprite):
    def update(self):
        """ Wrap sprite around screen. """
        if self.top < games.screen.height * 3/5:
            self.top = games.screen.height * 3/5

        if self.bottom > games.screen.height - 20:
            self.bottom = games.screen.height - 20

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Destroy self """
        self.destroy()


class CatStretch(games.Animation):
    """" cat stretching """

    def __init__(self, x, y):
        super(CatStretch, self).__init__(
            images=Game.stretch,
            x=x,
            y=y,
            repeat_interval=4,
            n_repeats=1,
            is_collideable=False)

        CatSprite.meow.play()


class CatSprite(games.Sprite):
    """ create animated cat running """
    sit = games.load_image("img/sliced_sprites/stretching_cat/image#4.bmp")
    sit_right = games.load_image("img/cat_sitting_right.bmp")
    meow = games.load_sound("audio/mew.wav")

    JUMP_WAIT = 20
    MEOW_RATE_MULTIPLIER = 10
    JUMP_ARC = [-8, -4, -3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 8]



    def __init__(self, game, x, y, images):
        super(CatSprite, self).__init__(
            x=x,
            y=y,
            image=images[0])
        self.game = game

        size = (55, 47)   # dimensions of cat running sprite frame

#        self.rect = pygame.Rect(x, y, size)
        self.images = images
#        self.images_right = images
#        self.images_left = [games.transform.flip(image, True, False) for image in images]

        self.index = 0
        self.image = images[self.index]
        self.stretch = Game.stretch
        self.stand = Game.stand
        self.dx = 0
        self.dy = 0
        self.health = 25
        self.animation_time = 0.1
        self.current_time = 0
 #       self.velocity = pygame.math.Vector2(0, 0)
        self.animation_frames = 4
        self.current_frame = 0
        self.total_frames = 0
        self.face_right = False
        self.time_to_jump = 15
        self.jump = False
        self.jumping = 0
        self.sitting = True

    def cat_run_left(self):
        self.total_frames += 1

    def update(self):
        self.total_frames += 1

        if self.jump:
            if self.jumping < 25:
                self.y = self.y + (CatSprite.JUMP_ARC[self.jumping] * 4)
                if CatSprite.JUMP_ARC[self.jumping] in [0, -1, 1]:
                    if self.face_right:
                        self.image = Game.run_right[1]
                    if not self.face_right:
                        self.image = Game.stretch[0]
                else:
                    self.image = Game.stretch[4]
                if games.keyboard.is_pressed(games.K_d):
                    self.face_right = True
                    self.image = Game.run_right[1]
                    self.x += 3
                if games.keyboard.is_pressed(games.K_a):
                    self.face_right = False
                    self.image = Game.stretch[0]
                    self.x -= 3
                self.jumping += 1
            else:
                self.jump = False

        elif games.keyboard.is_pressed(games.K_SPACE):
            self.jump = True
            self.jumping = 0
            CatSprite.meow.play()

        elif games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_d) \
            or games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_s):
            self.sitting = False
            if games.keyboard.is_pressed(games.K_a):
                self.face_right = False
                self.x -= 3
            if games.keyboard.is_pressed(games.K_d):
                self.face_right = True
                self.x += 3
            if games.keyboard.is_pressed(games.K_w):
                self.y -= 2
            if games.keyboard.is_pressed(games.K_s):
                self.y += 2

            self.current_frame += 1
            self.animation_frames = 4
            if self.current_frame >= self.animation_frames:
                self.current_frame = 0
                self.index = (self.index + 1) % self.animation_frames
                if not self.face_right:
                    self.image = self.images[self.index]
                if self.face_right:
                    self.image = Game.run_right[self.index]

        # elif games.keyboard.is_pressed(games.K_d):
        #     self.face_right = True
        #     self.current_frame += 1
        #     self.animation_frames = 4
        #     if self.current_frame >= self.animation_frames:
        #         self.current_frame = 0
        #         self.index = (self.index + 1) % len(self.images)
        #         self.image = Game.run_right[self.index]
        #     self.x += 3
        #
        # elif games.keyboard.is_pressed(games.K_w):
        #     self.current_frame += 1
        #     self.animation_frames = 4
        #     if self.current_frame >= self.animation_frames:
        #         self.current_frame = 0
        #         self.index = (self.index + 1) % len(self.images)
        #         self.image = Game.run_right[self.index]
        #   #  new_stretch = CatStretch(x=self.x, y=self.y)
        #   #  games.screen.add(new_stretch)
        #     self.y -= 2
        #
        # elif games.keyboard.is_pressed(games.K_s):
        #     self.y += 2

        else:
            self.current_frame += 1
            if not self.face_right:
                self.image = CatSprite.sit
            if self.face_right:
                self.image = CatSprite.sit_right

            # self.animation_frames = 10
            # if self.current_frame >= self.animation_frames:
            #     self.current_frame = 0
            #     self.index = (self.index + 1) % len(self.images)
            #     self.image = self.stand[self.index]

        """ Wrap sprite around screen. """
        if self.top < games.screen.height * 3/5 and not self.jump:
            self.top = games.screen.height * 3/5

        if self.bottom > games.screen.height - 20:
            self.bottom = games.screen.height - 20

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Destroy self. """
        self.destroy()

    # def update_time_dependent(self, dt):
    #     """
    #     Updates the image of Sprite approximately every 0.1 second.
    #
    #     Args:
    #         dt: Time elapsed between each frame.
    #     """
    #     if self.velocity.x > 0:  # Use the right images if sprite is moving right.
    #         self.images = self.images_right
    #     elif self.velocity.x < 0:
    #         self.images = self.images_left
    #
    #     self.current_time += dt
    #     if self.current_time >= self.animation_time:
    #         self.current_time = 0
    #         self.index = (self.index + 1) % len(self.images)
    #         self.image = self.images[self.index]
    #
    #     self.rect.move_ip(*self.velocity)
    #
    # def update_frame_dependent(self):
    #     """
    #     Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).
    #     """
    #     if self.velocity.x > 0:  # Use the right images if sprite is moving right.
    #         self.images = self.images_right
    #     elif self.velocity.x < 0:
    #         self.images = self.images_left
    #
    #     self.current_frame += 1
    #     if self.current_frame >= self.animation_frames:
    #         self.current_frame = 0
    #         self.index = (self.index + 1) % len(self.images)
    #         self.image = self.images[self.index]
    #
    #     self.rect.move_ip(*self.velocity)
    #
    # def update(self, dt):
    #     """This is the method that's being called when 'all_sprites.update(dt)' is called."""
    #     # Switch between the two update methods by commenting/uncommenting.
    #     self.update_time_dependent(dt)
    #     # self.update_frame_dependent()


class Game(object):
    """ Cat sprite game """
    images = load_images(path='./img/sliced_sprites/cat')
    stretch = load_images(path='./img/sliced_sprites/stretching_cat')
    stand = load_images(path='./img/sliced_sprites/standing_cat')
    run_right = load_images(path='./img/sliced_sprites/cat_running_right')


    def __init__(self):
        self.level = 0
        self.cat = CatSprite(game=self,
                             x = 500,
                             y = games.screen.height - 100,
                             images=Game.images)
        games.screen.add(self.cat)

    def play(self):
        """ start game play """
        games.music.load("audio/BlackCatWhiteCatK.mp3")
        games.music.play(-1)

        """ load background image"""
        background_image = games.load_image("img/alley.jpg")
        background_image = games.scale_image(background_image, 1.25)
        games.screen.background = background_image

        games.screen.mainloop()


def main():
    cat_dash = Game()
    cat_dash.play()


main()
