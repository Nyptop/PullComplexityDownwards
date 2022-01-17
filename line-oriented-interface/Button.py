# try to make this general purpose
# what would a specialised design look like?

#

# gotta check, when is the mouse in the correct position?
# add a method for handling clicks, to keep it general purpose, must specify a function?
# add a draw method, blit to screen

# for interface, we provide the screen, x, y and text, making the interface as simple as possible

# could live code an improvement, make interface smaller, more general purpose

# put mouse.get_pos() in here?

# example of pulling complexity downwards, automatically calculate button size

import pygame

class Button:
    def __init__(self, screen, x, y, width, height, text):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colour = (170, 170, 170)

    def handle_click(self, action, *args):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x in range(self.x, self.x + self.width) and mouse_y in range(self.y, self.y + self.height):
            return action(*args)

    def show(self):
        pygame.draw.rect(self.screen,self.colour,[self.x, self.y, self.width, self.height])
