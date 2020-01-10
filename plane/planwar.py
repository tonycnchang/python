# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time
import random
num =1

class HeroPlan():
    def __init__(self,screen_temp,enemy_bullet_list_temp):
        self.x = 200
        self.y = 534
        self.screen = screen_temp
        self.image = pygame.image.load('plan.png').convert_alpha()
        self.bullet_list=[]
        self.bullet_list_del=[]
        self.enemy_bullet_list = enemy_bullet_list_temp
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)


    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def move_up(self):
        self.y-=5
    def move_down(self):
        self.y+=5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

    def dead(self):
        for enemybullet in self.enemy_bullet_list:
            if self.x<enemybullet.x<self.x+50 and self.y<enemybullet.y <self.y+50:
                
                return True
            else:
                return False
class EnemyPlan():
    def __init__(self,screen_temp):
        self.x = random.randint(50,350)
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load('enemy.png').convert_alpha()
        self.direction = 'right'
        self.enemybullet_list=[]
    def display(self):
        if self.judge():
            self.screen.blit(self.image,(self.x,self.y))
            for enemybullet in self.enemybullet_list:
                enemybullet.display()
                enemybullet.move()
                if enemybullet.judge():
                    self.enemybullet_list.remove(enemybullet)

    def move(self):
        self.y += 5
        if self.direction=='right':
            self.x+=5
        elif self.direction=='left':
            self.x-=5
        
        if self.x>=400:
            self.direction = 'left'
        elif self.x<=0:
            self.direction = 'right'
    def judge(self):
        if self.y<50:
            return True
        else:
            return False
            self.__init__()

    def fire(self):
        #random_num = random.randint(1,100)
        #if random_num == 10 or random_num == 20:
            self.enemybullet_list.append(EnemyBullet(self.screen,self.x,self.y))
        
class Bullet():
    def __init__(self,screen_temp,x,y):
        self.x = x+35
        self.y = y-15
        self.screen = screen_temp
        self.image = pygame.image.load('bullet.png').convert_alpha()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=5
    def judge(self):
        if self.y<400:
            return True
        else:
            return False

class EnemyBullet():
    def __init__(self,screen_temp,x,y):
        self.x = x+35
        self.y = y+70
        self.screen = screen_temp
        self.image = pygame.image.load('bullet1.png').convert_alpha()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y+=30
    def judge(self):
        if self.y>600:
            return True
        else:
            return False
        
def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()               
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.move_down()
            elif event.key == K_SPACE:
                hero_temp.fire()    
def main():
    screen = pygame.display.set_mode((500,600),0,32)
    pygame.display.set_caption('飞机大战')
    back_ground_image = 'space.png'
    #HeroPlane_image = 'plan.png'
    #HeroPlan = pygame.image.load(HeroPlane_image).convert_alpha()
    BackGround = pygame.image.load(back_ground_image).convert_alpha()
    
    enemy_plane1 = EnemyPlan(screen)
    enemy_bullet_list = enemy_plane1.enemybullet_list
    hero_plane1 = HeroPlan(screen,enemy_bullet_list)
    while True:
        global num
        screen.blit(BackGround,(0,0))
        hero_plane1.display()
        
        enemy_plane1.display()
        enemy_plane1.move()
        if hero_plane1.dead():
            pygame.quit()
            exit()
        if num == 5:
            enemy_plane1.fire()
        if enemy_plane1.judge() == False:
            enemy_plane1.__init__(screen)
        pygame.display.update()
        key_control(hero_plane1)
        
        time.sleep(0.5)
        num += 1
        if num >5:
            num=1
        print(num)
        
if __name__ == "__main__":
    main()
