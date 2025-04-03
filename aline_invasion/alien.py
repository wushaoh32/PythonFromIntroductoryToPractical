import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """"表示单个外星人的类"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #加载外星人图像并设置rect属性
        self.image = pygame.image.load('C:/Users/admin/Desktop/PythonFromIntroductoryToPractical/aline_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的精度水平位置
        self.x = float(self.rect.x)
        