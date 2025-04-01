class Settings:
    """存储《游戏》中的所有类"""

    def __init__(self):
        """初始化游戏的所有设置。"""
        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船设置——每次移动1.5像素
        self.ship_speed = 1.5

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        