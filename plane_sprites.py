# coding= utf-8
import random
import pygame
SCREEN_SIZE = pygame.Rect(0, 0, 480, 700)
CLOCK_FPS = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(PlaneSprite):
    def __init__(self, is_alt=False):
        super().__init__("E:/飞机大战/demo/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_SIZE.height:
            self.rect.y = -self.rect.height


class Enemy(PlaneSprite):
    def __init__(self):
        super().__init__("./demo/enemy.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_SIZE.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_SIZE.height:
            # print("需要删除敌人")
            self.kill()

    def __del__(self):
        print("敌机over了%s" % self.rect)


class Hero(PlaneSprite):
    def __init__(self):
        super().__init__("./demo/hero.png", 0)
        self.rect.centerx = SCREEN_SIZE.centerx
        self.rect.bottom = SCREEN_SIZE.bottom - 50
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_SIZE.right:
            self.rect.right = SCREEN_SIZE.right

    def fire(self):
        # print("发射子弹")
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(PlaneSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./demo/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("销毁子弹")

