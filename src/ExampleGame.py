
# File: ExampleGame.py

from Scene import Scene
from Thing import Thing
import pygame
from pygame.locals import *


def main():
    # Create scene
    scene = Scene()
    scene.set_size(800, 500)

    #  Create obstacle sprite
    sprite1 = Thing(scene, "../assets/enemy.png", 100, 400)
    sprite1.set_dx(0)
    sprite1.set_dy(-0.2)
    sprite1.set_bounds_action(sprite1.BOUNCE)
    sprite1.scale((40, 40))

    sprite2 = Thing(scene, "../assets/enemy.png", 200, 0)
    sprite2.set_dx(0)
    sprite2.set_dy(0.3)
    sprite2.set_bounds_action(sprite2.BOUNCE)
    sprite2.scale((50, 50))

    sprite3 = Thing(scene, "../assets/enemy.png", 300, 400)
    sprite3.set_dx(0)
    sprite3.set_dy(-0.2)
    sprite3.set_bounds_action(sprite3.BOUNCE)
    sprite3.scale((60, 60))

    sprite4 = Thing(scene, "../assets/enemy.png", 400, 0)
    sprite4.set_dx(0)
    sprite4.set_dy(0.3)
    sprite4.set_bounds_action(sprite4.BOUNCE)
    sprite4.scale((70, 70))

    sprite5 = Thing(scene, "../assets/enemy.png", 500, 400)
    sprite5.set_dx(0)
    sprite5.set_dy(-0.3)
    sprite5.set_bounds_action(sprite5.BOUNCE)
    sprite5.scale((80, 80))

    sprite6 = Thing(scene, "../assets/enemy.png", 600, 0)
    sprite6.set_dx(0)
    sprite6.set_dy(0.2)
    sprite6.set_bounds_action(sprite6.BOUNCE)
    sprite6.scale((90, 90))

    # Player that can be moved around
    player = Player(scene, "../assets/player.png", 50, 200)
    player.set_bounds_action(player.BOUNCE)

    # if Thing.check_collisions(player):
    #     pass

    # Start the game loop
    scene.start()


class Player(Thing):

    def __init__(self, scene, image_file, initial_x, initial_y):
        Thing.__init__(self, scene, image_file, initial_x, initial_y)

    # def check_collisions(self):
    #     """Check for collisions with other sprites"""
    #     for sprite in self.scene.sprites:
    #         if sprite != self and self.collides_with(sprite):
    #             self.handle_collision(sprite)    

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == pygame.K_UP:
                self.set_dy(-0.5)
            if event.type == KEYUP and event.key == pygame.K_UP:
                self.set_dy(0)
            if event.type == KEYDOWN and event.key == pygame.K_DOWN:
                self.set_dy(0.5)
            if event.type == KEYUP and event.key == pygame.K_DOWN:
                self.set_dy(0)
            if event.type == KEYDOWN and event.key == pygame.K_RIGHT:
                self.set_dx(0.5)
            if event.type == KEYUP and event.key == pygame.K_RIGHT:
                self.set_dx(0)
            if event.type == KEYDOWN and event.key == pygame.K_LEFT:
                self.set_dx(-0.5)
            if event.type == KEYUP and event.key == pygame.K_LEFT:
                self.set_dx(0)


if __name__ == '__main__':
    while main():
        pass
