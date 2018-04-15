import pygame, sys, random
from pygame.locals import *
import numpy as np
import time as ti
# 變數宣告
##背景顏色
BACKGROUNDCOLOR = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 40

VHNUMS = 10 #格數
CELLNUMS = VHNUMS*VHNUMS#總格數


#  退出
def terminate():
    pygame.quit()
    sys.exit()

#初始化板子
def initBoard():
    pygame.init()
    mainClock = pygame.time.Clock()


    # 加載圖片
    gameImage = pygame.image.load('apple.jpg')
    gameImage = pygame.transform.scale(gameImage, (800, 600))
    gameRect = gameImage.get_rect()


    # 設置遊戲視窗
    windowSurface = pygame.display.set_mode((gameRect.width, gameRect.height))
    pygame.display.set_caption('炸彈超人')

    #每隔寬度
    cellWidth = int(gameRect.width / VHNUMS)
    cellHeight = int(gameRect.height / VHNUMS)
    hasBoard = True

    #畫分隔線
    for i in range(VHNUMS+1):
        pygame.draw.line(windowSurface, BLACK, (i*cellWidth, 0), (i*cellWidth, gameRect.height))
    for i in range(VHNUMS+1):
        pygame.draw.line(windowSurface, BLACK, (0, i*cellHeight), (gameRect.width, i*cellHeight))


    windowSurface.fill(BLUE)

    for i in range(VHNUMS+1):
        pygame.draw.line(windowSurface, BLACK, (i*cellWidth, 0), (i*cellWidth, gameRect.height))
    for i in range(VHNUMS+1):
        pygame.draw.line(windowSurface, BLACK, (0, i*cellHeight), (gameRect.width, i*cellHeight))

    pygame.display.update()


#設定新腳色
class piece:
    x = 0 #位址
    y = 0 #位址
    player = 0 # 1為第一個玩家 2為第二個玩家
    life = True #存活
    picture = ""

    def __init__(self , x_position , y_position , player_side , life_TF ):
        self.x = x_position
        self.y = y_position
        self.player = player_side
        self.life = life_TF


#產生腳色
def init_players():
    #player1
    piece( a , 0 , 0 , A , True)

    #player2
    piece(b , 720 , 520 , B , True)

class obstacles
    passable = False
    locationx = -1
    locationy = -1
    AOE = -1
    owner = -1
    time = -1
    picked = False

    def initBomb(self , locationx , locationy , AOE , owner , time ):
        self.locationx = locationx
        self.locationy = locationy
        self.AOE = AOE
        self.owner = owner
        self.time = time
        bombTimer = pygame.time.get_ticks()
        waiting = True
        while waiting:
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            if seconds > 5 :
                bombAOE(self.owner , self.locationx , self.locationy , self.AOE)
                waiting = False


    def initBlocks( self , locationx , locationy ):
        self.locationx = locationx
        self.locationy = locationy

    def initItems(self , picked , locationx , locationy ):
        self.picked = False
        self.locationx = locationx
        self.locationy = locationy

def bombAOE(owner , locationx , locationy , AOE):



finish = False
# 遊戲主程式
while finish == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #player 1 up down left right
                #x_change = -5
            if event.key == pygame.K_a:
                #x_change = 5
            if event.key == pygame.K_s:
                #x_change = 5
            if event.key == pygame.K_d:
                #x_change = 5
            if event.key == pygame.K_i: #player 2 up down left right
                #x_change = -5
            if event.key == pygame.K_j:
                #x_change = 5
            if event.key == pygame.K_k:
                #x_change = 5
            if event.key == pygame.K_l:
                #x_change = 5
            if event.key == pygame.K_x:#player 1 drop bomb
                #x_change = 5
            if event.key == pygame.K_m:#player 2 drop bomb
                #x_change = 5
            #這邊我不知道怎麼做
        '''if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
'''
    mainClock.tick(FPS)

    ti.sleep(2)
