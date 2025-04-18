#导入模块sys:退出游戏
import sys
#导入模块pygame：功能
import pygame
#导入settings类
from settings import Settings
#导入Ship类
from ship import Ship

from bullet import Bullet

from alien import Alien
#创建主类：管理游戏资源和行为的类
class AlienInvasion:
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
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #设置背景色
        self.bg_color = (230,230,230)

        #导入Ship类、、
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.bullets.update()
            

            print(len(self.bullets))
            
    def _check_events(self):
        """辅助方法的名称以单个下划线打头：其作用是为了隔离事件循环"""
        # 监视键盘和鼠标事件
        for event in pygame.event.get():#检测事件访问
            if event.type == pygame.QUIT:#检测到这个事件，调用sys退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    #向右移动飞船
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left =True
        #按Q退出
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """松开响应"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  

    def _update_bullets(self):
        """更新子弹的位置并消除子弹"""
        #更新子弹的位置
        self.bullets.update()
        #消除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    #检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    def _update_aliens(self):
        self._check_fleet_edges()
        self.alien.update()#更新位置

    def _create_fleet(self):
        """创建一个外星人群"""
        #创建一个外星人
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #计算屏幕可以容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien_height)-ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def  _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.alien.add(alien)

    #外星人到达边缘时采取相应措施
    def _check_fleet_edges(self):
        for aline in self.alien.sprites():
            if aline.check_edges():
                self._change_fleet_direction()
                break

    #将整群外星人下移并改变他们的方向
    def _change_fleet_direction(self):
        for aline in self.alien.sprites():
            aline.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #每次循环时都重绘屏幕,fill方法是用背景色充满屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() 
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.alien.draw(self.screen)
            #让最近绘制的屏幕可见
            pygame.display.flip()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullets  = Bullet(self)
            self.bullets.add(new_bullets)

if __name__ == '__main__':
    #创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()