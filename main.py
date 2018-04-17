import pygame, sys, random
#from pygame.locals import *
import numpy as np
import time
import time as ti
# 變數宣告
##背景顏色
BACKGROUNDCOLOR = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 40
AOEA =3
AOEB = 3
VHNUMS = 10 #格數
CELLNUMS = VHNUMS*VHNUMS #總格數

finish = False;

gameImage = pygame.image.load('apple.jpg')
gameImage = pygame.transform.scale(gameImage, (800, 600))
gameRect = gameImage.get_rect()


# 設置遊戲視窗
windowSurface = pygame.display.set_mode((gameRect.width,gameRect.height))
pygame.init()
#  退出
def zxcv():
    pygame.quit()
    sys.exit()

#初始化板子
def initBoard():
    pygame.init()
    mainClock = pygame.time.Clock()


    # 加載圖片

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


    #windowSurface.fill(BLUE)

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


p1=piece( 0 , 0 , 'A' , True)
p2=piece( 720 , 540 , 'B' , True)

background=pygame.Surface((800,600))
#產生腳色
def players_picture_set():
    #player1
    background.fill([176,196,22])
    playerImage1 = pygame.image.load("man1.png")
    playerImage1 = pygame.transform.scale(playerImage1, (70, 50))
    background.blit(playerImage1,(p1.x,p1.y))
    #player2

    playerImage2 = pygame.image.load("man2.png")
    playerImage2 = pygame.transform.scale(playerImage2, (70, 50))
    background.blit(playerImage2,(p2.x,p2.y))
    windowSurface.blit(background,(0,0))
    pygame.display.update

def bombsPictureSet(locationx , locationy ):
    print("makepicture")
    bombImage = pygame.image.load("bomb.png")
    bombImage = pygame.transform.scale(bombImage , ( 70 , 50 ))
    background.blit(bombImage,(locationx,locationy))
    windowSurface.blit(background,(0,0))
    pygame.display.update


class obstacles:
    passable = False
    locationx = -1
    locationy = -1
    AOE = -1
    owner = -1
    time = -1
    picked = False


    def initBlocks( self , locationx , locationy ):
        self.locationx = locationx
        self.locationy = locationy

    def initItems(self , picked , locationx , locationy ):
        self.picked = False
        self.locationx = locationx
        self.locationy = locationy

    def initBomb( locationxO , locationyO , AOEO , ownerO  ):
        print("initbomb")
        locationx = locationxO
        locationy = locationyO
        bombsPictureSet(locationx ,locationy )
        AOE = AOEO
        owner = ownerO
        bombTimer = time.time()
        #bombTimer = pygame.time.get_ticks()
        waiting = True
        while waiting:
            curTime = time.time()
            seconds= curTime - bombTimer
            print(seconds) 
            if seconds >5 :
                duelOutcome = bombAOE(self.owner , self.locationx , self.locationy , self.AOE)
                if duelOutcome == 1 or duelOutcome == 2 or duelOutcome == 3:
                    finish = True
                elif duelOutcome == 4 :
                    finish = False
                waiting = False


    def bombAOE(owner, locationx , locationy ):
        print("bombAOE")
        whathappensnext ;
        if owner == 1:
            AOE = AOEA
        if owner == 2 :
            AOE =AOEB
        resultA , resultB =  bombDamage(locationx , locationy , AOE)

        if resultA == True:
            print("Bwin")
            whathappensnext = 1
        elif resultB == True:
            print("Awin")
            whathappensnext = 2
        elif resultA == True and resultB == True:
            print("DRAW")
            whathappensnext = 3
        elif resultA == False and resultB == False:
            print("safe")
            whathappensnext = 4
        return whathappensnext

    def bombDamage(locationx , locationy , AOE):
        print("bombAOE")
        p1Status , p2Status = False
        if locationx -( 80 * AOE) <= p1.x and locationx >= p1.x and locationy == p1.y: #left hit
            p1Status = True
        if locationx + (80 * AOE) >= p1.x and locationx <= p1.x and locationy == p1.y: #right hit
            p1Status = True
        if locationy - (60*AOE ) <= p1.y and locationy >= p1.y and locationx == p1.x: #top hit
            p1Status = True
        if locationy + (60 * AOE ) >= p1.y and locationy <= p1.y and locationx == p1.x: # bottom hit
            p1Status = True

        if locationx -( 80 * AOE) <= p2.x and locationx >= p2.x and locationy == p2.y: #left hit
            p2Status = True
        if locationx + (80 * AOE) >= p2.x and locationx <= p2.x and locationy == p2.y: #right hit
            p2Status = True
        if locationy - (60*AOE ) <= p2.y and locationy >= p2.y and locationx == p2.x :#top hit
            p2Status = True
        if locationy + (60 * AOE ) >= p2.y and locationy <= p2.y and locationx == p2.x: # bottom hit
            p2Status = True

        return p1Status , p2Status


players_picture_set()
# 遊戲主程式
while finish == False:
    obsta = obstacles()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #player 1 up down left right
                p1.y=p1.y-60
                print('w')
            if event.key == pygame.K_a:
                p1.x = p1.x -80
                print('a')
            if event.key == pygame.K_s:
                p1.y = p1.y +60
                print('s')
            if event.key == pygame.K_d:
                p1.x = p1.x +80
                print('d')
            if event.key == pygame.K_p:#end game
                finish = True
                print("end game")
                break
            if event.key == pygame.K_i: #player 2 up down left right
                p2.y = p2.y - 60
                print('i')
            if event.key == pygame.K_j:
                p2.x = p2.x - 80
                print('j')
            if event.key == pygame.K_k:
                p2.y = p2.y + 60
                print('k')
            if event.key == pygame.K_l:
                p2.x = p2.x + 80
                print('l')
#<<<<<<< HEAD
            if event.key == pygame.K_q:#player 1 drop bomb
                obstacles.initBomb(p1.x , p1.y , AOEA , 1 )
            if event.key == pygame.K_m:#player 2 drop bomb
                obstacles.initBomb(p2.x , p2.y , AOEB , 2 )
#=======
            #if event.key == pygame.K_q:#player 1 drop bomb

            #if event.key == pygame.K_m:#player 2 drop bomb

#>>>>>>> 619efc72fbaddd29881fd2499347206791e15ca8
        pygame.event.pump()

    initBoard()
    players_picture_set()
    pygame.display.update
            #這邊我不知道怎麼做

"""
mainClock.tick(FPS)

ti.sleep(2)"""
