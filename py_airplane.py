#!/usr/bin/python
# coding: utf-8

import pygame
from sys import exit
from pygame.locals import *
import random


# screen size

CREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# bullet

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed

# player plane

class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []  # save airplane image
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]),convert_alpha())
        self.rect = player_rect[0]  # initial rectangle
        self.rect.topleft = init_pos  # initial topleft of rectangle
        self.speed = 8  # initial speed
        self.bullets = pygame.sprite.Group()  # initial bullet group
        self.img_index = 0  # airplane image index
        self.is_hit = False  # be hit or not

    # shoot

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

    # move up

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    # move down

    def moveDown(self):
        if self.rect.top >=  SCREEN_HEIGHT - self.rect.heigh:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    # move left

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    # move right

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH -self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

# anemy plane

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 2
        self.down_index = 0

    # enemy move

    def move(self):
        self.rect.top += self.speed

# init pygame

pygame.init()

# screen

screen = pygame.display.set_mode((SCREEN.WIDTH, SCREEN_HEIGHT))

# caption

pygame.display.set_caption('airplane')

# background

background = pygame.image.load('resources/image/background.png').convert()

# game over image
game_over = pygame.image.oad('resources/image/gameover.png')

# plane and bullet

plane_img = pygame.image.load('resources/image/shoot.png')

# player plane status image

player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)

# bullet

bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

# enemy plane status image

enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = []
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

enemies1 = pygame.sprite.Group()

# enemy down

enemies_down = pygame.sprite.Group()

# init shoot frequency and enemy frequency

shoot_frequency = 0
enemy_frequency = 0

# player down

player_down_index = 16

# init score

score = 0

# clock

clock = pygame.time.Clock()

# judge running

running = True

# main

while running:
    clock.tick(60)

    # judge if player is hit and create bullet

   if not player.is_hit:
        if shoot_frequency % 15 == 0:
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    # create enemy

    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frenquency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0

    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    for enemy in enemies1:
        enemy.move()
        # collition
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            break
        if enemy.rect.top < 0:
            enemies1.remove(enemy)

    # enemy down process

    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    screen.fill(0)
    screen.blit(background, (0, 0))

    if not player.is_hit:
        screen.blit(player.image[player.img_index], player.rect)
        player.img_index = shoot_frequency / 8
    else:
        player.img_index = player_down_index / 8
        screen.blit(player.image[player.img_index], player.rect)
        layer_down_index += 1
        if player_down_index > 47:
            running = False

    # enemy is hit

    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            pass
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            score += 1000
            continue
        creen.blit(enemy_down.down_imgs[enemy_down.down_index / 2],
                enemy_down.rect)
        enemy_down.down_index += 1

    player.bullets.draw(screen)

    enemies1.draw(screen)

    # score

    score_font = pygame.font.Font(None, 36)
    score_text = score_font,render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)

    # update display

    pygame.display.update()

    # quit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key_pressed = pygame.key.get_pressed()

    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()

# gameover process

font = pygame.font.Font(None, 48)
text = font.render('Score: ' + str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)

# quit process

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
