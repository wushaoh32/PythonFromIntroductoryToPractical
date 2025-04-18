import pygame

class Ship:
    """管理飞船的类"""
    #引用self和指向当前AlienInvasion实例的引用
    #Ship能够访问AlienInvasion中定义的所有资源
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置。"""
        #将屏幕赋给Ship的一个属性
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #使用get_rect方法访问屏幕的属性rect
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形,把飞船和屏幕按照矩形进行处理
        #Yes,Yes成功了，这tm的居然必须用绝对路径，而且这jj的Python只能用斜杠(/),不能反斜杠
        self.image = pygame.image.load('images/ship.bmp')
        #在Pygame中(0,0)位于屏幕左上角
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性x中存储小数值
        self.x = float(self.rect.x)      

        #移动标识
        self.moving_right = False
        self.moving_left = False

    def update(self):
        "根据移动标志调整飞船的位置"
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船。"""
        self.screen.blit(self.image,self.rect)
