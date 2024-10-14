import pygame

def load_sprite(game, sprite, size):
    return pygame.transform.scale(game.assets[sprite], (size))