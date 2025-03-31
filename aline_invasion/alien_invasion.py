#导入模块sys:退出游戏
import sys
#导入模块pygame：功能
import pygame
#导入settings类
from settings import Settings
#导入Ship类
from ship import Ship
#创建主类
class AlienInvasion:
    """管理游戏资源和行为的类"""
    #定义方法init
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        #方法中调用函数：初始化背景位置
        pygame.init()
        #导入类
        self.settings = Settings()
        #创建一个显示窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width , self.settings.screen_height)) #方法里面包含元组，赋值给属性self.screen
        pygame.display.set_caption("Aline Invasion")

        #设置背景色
        self.bg_color = (230,230,230)

        #导入Ship类
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():#检测事件访问
                if event.type == pygame.QUIT:#检测到这个事件，调用sys退出游戏
                    sys.exit()

            #每次循环时都重绘屏幕,fill方法是用背景色充满屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            #让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()