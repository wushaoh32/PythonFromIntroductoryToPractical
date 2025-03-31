import pygame

class Ship:
    """管理飞船的类"""
    #引用self和指向当前AlienInvasion实例的引用
    #Ship能够访问AlienInvasion中定义的所有资源
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置。"""
        #将屏幕赋给Ship的一个属性
        self.screen = ai_game.screen
        #使用get_rect方法访问屏幕的属性rect
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形,把飞船和屏幕按照矩形进行处理
        #Yes,Yes成功了，这tm的居然必须用绝对路径，而且这jj的Python只能用斜杠(/),不能反斜杠
        self.image = pygame.image.load('C:/Users/admin/Desktop/PythonFromIntroductoryToPractical/aline_invasion/images/ship.bmp')
        #在Pygame中(0,0)位于屏幕左上角
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船。"""
        self.screen.blit(self.image,self.rect)