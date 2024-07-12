import pygame
from sys import *
import random

pygame.init()
pygame.display.init()
pygame.font.init()

font_selector = pygame.sysfont.get_fonts()

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
orange = (255,137,39)
white = (255,255,255)
black = (0,0,0)

screen_fill_color = (146,250,244)
size = (500,500)
width = size[0]
height = size[1]
title = 'mouse game'
screen = pygame.display.set_mode(size)
pygame.display.set_caption(title)
leftText = pygame.font.SysFont(None,32,True)
leftTextSurf_Left = leftText.render('Left',True,black)
leftTextSurf_Side = leftText.render('side',True,black)

midText = pygame.font.SysFont(font_selector[20],24,False)
midTextSurf_Middle = midText.render('Middle',True,white)
midTextSurf_Area = midText.render('area',True,white)

# rightText = pygame.font.SysFont(font_selector[50],80,True)
# rightTextSurf_Right = midText.render('Right',True,white)
# rightTextSurf_Side = midText.render('side',True,white)

def rotater(rectangle):
    return pygame.transform.rotate(rectangle,90)

def textRender(word: str, wordColor, font: int,font_size: int, bold: bool):
    textId = pygame.font.SysFont(font_selector[font],font_size,bold)
    w1 = textId.render(word,True,wordColor)
    return w1
# UserText = input('Type into the program:  ')

# testingText = textRender(UserText,white,80,50,True)

# rightTextSurf_Right = rotater(rightTextSurf_Right)


def randColor():
    randomColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return randomColor



# def stringSearch(string, search):
#     lengthOfString = len(string)
#     if string.find(search) >= 0 and string.find(search) <= lengthOfString:
#         stringPlus1 = string.find(search) + 1
#         return stringPlus1
run = False
crosshairSpread = int(input('\n\ninput crosshair size:  '))


if crosshairSpread >= 0 and type(crosshairSpread) == int: #case 1: valid crosshair size on try 1
        print('Crosshair size accepted... Open the game window, and enjoy the game!')
        run = True

while crosshairSpread < 0 or type(crosshairSpread) != int:  #case 2: invalid crosshair on try 1,2,3 etc
    crosshairSpread = int(input('Invalid crosshair size. Enter a value greater than or equal to 0:  '))
    if crosshairSpread >= 0:
        print('Crosshair size accepted... Open the game window, and enjoy the game!')
        run = True

with open('saveFile.txt','a') as SAVEFILE:
    SAVEFILE.write(str(crosshairSpread) + '\n')
 

# with open('alpha.txt','r') as ALPHABET:
#         file = ALPHABET.readline()
#         alphaList.append(file.split(' '))
#         for letters in file:
#             alphaList.append(letters)

# letterCaught = True
# while letterCaught:            
#     for items in alphaList[0]:
#         if crosshairSpread == items:
#             print('you typed a letter')
            

def mouseRectCircle(rect,color,mosColor,moSize):
    pygame.draw.rect(screen,color,rect,0) #areas on screen

    pygame.draw.circle(screen,mosColor,mosPos,2,-1) #crosshair control
    pygame.draw.circle(screen,mosColor,(mosPos[0]-moSize, mosPos[1]),2,-1)
    pygame.draw.circle(screen,mosColor,(mosPos[0]+moSize, mosPos[1]),2,-1)
    pygame.draw.circle(screen,mosColor,(mosPos[0], mosPos[1]-moSize),2,-1)
    pygame.draw.circle(screen,mosColor,(mosPos[0], mosPos[1]+moSize),2,-1)
    pygame.draw.line(screen,mosColor,(mosPos[0],mosPos[1]),(mosPos[0]-moSize,mosPos[1]))
    pygame.draw.line(screen,mosColor,(mosPos[0],mosPos[1]),(mosPos[0]+moSize,mosPos[1]))
    pygame.draw.line(screen,mosColor,(mosPos[0],mosPos[1]),(mosPos[0],mosPos[1]-moSize))
    pygame.draw.line(screen,mosColor,(mosPos[0],mosPos[1]),(mosPos[0],mosPos[1]+moSize))

    pygame.mouse.set_visible(False) #remove windows cursor
noFlashRandomColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
rectColor = (randColor())
X_rectPlant = [50, 0, 100]
Y_rectPlant = [0, 0, 0]
rectValue = [(X_rectPlant[0],Y_rectPlant[0],width/10,height), #MID BOX
             (X_rectPlant[1], Y_rectPlant[1], width/10,height), #LEFT BOX
             (X_rectPlant[2], Y_rectPlant[2], width - X_rectPlant[2],height)] #RIGHT BOX

clock = pygame.time.Clock()
mosPos = 0



while run:
    screen.fill(screen_fill_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # screen.blit(testingText,(0,0))
        
    mosPos = pygame.mouse.get_pos()
    mosClick = pygame.mouse.get_pressed()[0] == True
    btw_50u100 = mosPos[0] <= 100 and mosPos[0] > 50
    less_50 = mosPos[0] <= 50 
    great_100 = mosPos[0] > 100
    if btw_50u100:
        if mosClick:
            mouseRectCircle(rectValue[0],green,white, crosshairSpread+5)
            screen.blit(midTextSurf_Middle,(X_rectPlant[0],Y_rectPlant[0]))
            screen.blit(midTextSurf_Area,(X_rectPlant[0],Y_rectPlant[0]+40))
        else:
            mouseRectCircle(rectValue[0],blue,red, crosshairSpread)
        
            
    if less_50:
        if mosClick:
            mouseRectCircle(rectValue[1],orange,white,crosshairSpread + 5)
            screen.blit(leftTextSurf_Left,(0,0))
            screen.blit(leftTextSurf_Side,(0,40))
        else:
            mouseRectCircle(rectValue[1],white,red, crosshairSpread)
    if great_100:
        if mosClick:
            mouseRectCircle(rectValue[2],red,blue,crosshairSpread+10)
            screen.blit(rotater(textRender('Right',white,80,20,True)),(200,0))
            screen.blit(textRender('Side',white,80,20,True),(250,0))
            
        else:
            mouseRectCircle(rectValue[2],noFlashRandomColor,red,crosshairSpread)
    
    pygame.display.update()
    clock.tick(60)

print('done')