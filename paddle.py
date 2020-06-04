import pygame

BLACK = (0, 0, 0)

#Bat = pygame.image.load('BaseBallBat.png')

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
#        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def Up(self, box):
        self.rect.y -= box
        if self.rect.y < 0:
            self.rect.y = 0

    def Down(self, box):
        self.rect.y += box
        if self.rect.y > 400:
            self.rect.y = 400

    def Left1(self, box):
        self.rect.x -= box
        if self.rect.x < 0:
            self.rect.x = 0

    def Right1(self, box):
        self.rect.x += box
        if self.rect.x > 175:
            self.rect.x = 175

    def Left2(self, box):
        self.rect.x -= box
        if self.rect.x < 525:
            self.rect.x = 525

    def Right2(self, box):
        self.rect.x += box
        if self.rect.x > 690:
            self.rect.x = 690

