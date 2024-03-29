from settings import *
import pygame

class Player:
    """Player class consists of functions for managing the player"""
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self) -> tuple[int, int]:
        """returns player position

        Returns:
            tuple[int, int]: x and y coordinates of player
        """
        return self.x, self.y

    def movement(self) -> None:
        """react to wasd and arrows button press and change user position or direction"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= player_speed
        if keys[pygame.K_s]:
            self.y += player_speed
        if keys[pygame.K_a]:
            self.x -= player_speed
        if keys[pygame.K_d]:
            self.x += player_speed
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02