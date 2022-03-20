import pygame
import random
# draw a map

pygame.init()
Length = 600
Width = 600
BoxLength = 20
BoxWidth = 20
Row = int(Length / BoxLength)-1
Col = int(Width / BoxWidth)-1
direct = "left"
BodyLength = 3
Tick = 15
# setting the size of window
window = pygame.display.set_mode((Length, Width))

# class box
class box:
    row = 0
    col = 0
    color = (255, 255, 255)

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


# create a snake head
snakeHead = box(row=int(Row / 2), col=int(Col / 2), color=(255, 0, 0))

# create a food-box
food = box(row=random.randint(0, Row-1), col=random.randint(0, Col-1), color=(0, 255, 0))

# create the snake's body
snakeBody = [(box(row=snakeHead.row, col=snakeHead.col+1, color=(255, 50, 50))),
             (box(row=snakeHead.row, col=snakeHead.col+2, color=(255, 50, 50))),
             (box(row=snakeHead.row, col=snakeHead.col+3, color=(255, 50, 50)))]

import pygame
import sys
import random
from pygame import QUIT




# draw the food and head
def draw_Box(box, window):
    left = box.col * BoxLength
    top = box.row * BoxWidth
    width = BoxWidth
    height = BoxLength
    color = box.color

    pygame.draw.rect(window, color, ((left, top), (width, height)))

# move the snake
def move(direct, box):
    if direct == "left":
        box.col -= 1
    elif direct == "right":
        box.col += 1
    elif direct == "up":
        box.row -= 1
    elif direct == "down":
        box.row += 1
    elif direct == "nodirection":
        isCreate = True
        i = 0
        while isCreate:
            box.row =random.randint(0, Row)
            box.col =random.randint(0, Col)
            if box.row != snakeBody[i].row and box.col != snakeBody[i].col:
                isCreate = False
            i += 1


# drew a game map on the screen
def play():
    # global variable
    global direct
    global BodyLength
    gamePlaying = "playing"

    # setting the title of the window
    pygame.display.set_caption("happy snake  1.0")

    # setting the background color of gameMap
    bgColor = (255, 255, 255)


    # let the map stay on your screen
    clock = pygame.time.Clock()

    while True:

        # fill the color to the map
        window.fill(bgColor)

        # draw the gameMap
        pygame.draw.rect(window, bgColor, (0, 0, Width, Length))

        #setting the snakeTail
        snakeTail = box(row=0, col=0, color=(255, 50, 50))
        snakeTail.row = snakeBody[BodyLength - 1].row
        snakeTail.col = snakeBody[BodyLength - 1].col

        # draw snake's head and food box
        draw_Box(snakeHead, window)
        # draw snake's body
        for bodyBox in snakeBody:
            draw_Box(bodyBox, window)
            if snakeHead.row == snakeBody[0].row and snakeHead.col == snakeBody[0].col:
                print("yes")


        # move
        bodyLength = BodyLength - 1
        while bodyLength > 0 :
            snakeBody[bodyLength].row = snakeBody[bodyLength - 1].row
            snakeBody[bodyLength].col = snakeBody[bodyLength - 1].col
            bodyLength -= 1

        snakeBody[0].row = snakeHead.row
        snakeBody[0].col = snakeHead.col

        move(direct, snakeHead)

        # eat

        # eat action
        if snakeHead.row == food.row and snakeHead.col == food.col:
            snakeBody.append(snakeTail)
            BodyLength += 1
            # if the food have been eaten

            move("nodirection", food)

        draw_Box(food, window)

        # crash action
        if snakeHead.row < 0 or snakeHead.col < 0 or snakeHead.row >= Row or snakeHead.col >= Col:
            gamePlaying = "over"
        # set tick
        clock.tick(Tick)

        # exit
        for event in pygame.event.get():
            if event.type == QUIT or gamePlaying == "over":
                print("exit the game")
                # quit pygame
                pygame.quit()
                # exit sys
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == 1073741906 or event.key == 119) and direct != "down":
                    direct = "up"
                elif (event.key == 1073741905 or event.key == 115) and direct != "up":
                    direct = "down"
                elif (event.key == 1073741904 or event.key == 97) and direct != "right":
                    direct = "left"
                elif (event.key == 1073741903 or event.key == 100) and direct != "left":
                    direct = "right"

        # update the screen
        pygame.display.update()

play()