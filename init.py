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
