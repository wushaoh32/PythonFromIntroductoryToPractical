class Settings:
    """存储《游戏》中的所有类"""

    def __init__(self):
        """初始化游戏的所有设置。"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        #外星人设置
        self.fleet_drop_speed = 10

        #加快游戏节奏的速度
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    #初始化随游戏进行而变化的设置
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

    #提高速度的设置
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
