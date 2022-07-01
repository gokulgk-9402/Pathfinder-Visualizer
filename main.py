from tkinter import messagebox, Tk
import pygame
import sys

import pygments

WIDTH = 700
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((10, 10, 10))

        pygame.display.flip()

main()