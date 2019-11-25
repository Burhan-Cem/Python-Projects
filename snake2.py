import random
import numpy as np
import move_interface
#from move_interface import MoveInterface.Direction as Dir
from time import sleep
from graphics import *

gameOn = True 

################################################# Functions  ################################################# 

def initBoard(dim):
    board = [[0 for x in range(dim)] for y in range(dim)]
    return board

def initSnake(dim):
    snakeHead = [dim//2, dim//2]
    tail = [snakeHead[0], snakeHead[1]+1]
    snake = []
    snake.append(snakeHead)
    snake.append(tail)
    print(snake)
    return snake

def newFood(dim,snake):
    global food
    foodOnSnake = True
    while foodOnSnake:
        food = [random.randrange(dim), random.randrange(dim)]
        for tile in snake:
            if tile == food:
                print("food placed on snake")
                break
            else: foodOnSnake = False
    return food

def updateBoard(snake, dim):
    board = np.zeros((dim,dim))
    for s in snake:
        board[s[0], s[1]] = 1           #Snake head and tail
    board[snake[0][0], snake[0][1]] = 2 #Snake head
    board[food[0],food[1]] = 3          #Food
    return board



def updateSnake(snake, dim, direction):
    global food
    print(direction)
    if direction == move_interface.Direction.NORTH:
        dirnx = 0; dirny = 1
    elif direction == Direction.SOUTH:
        dirnx = 0; dirny = -1
    elif direction == Direction.EAST:
        dirnx = 1; dirny = 0
    elif direction == Direction.WEST:
        dirnx = -1; dirny = 0
    
    snake.insert(0, [snake[0][0]+dirnx, snake[0][1]+dirny])
    if food == snake[0]:
        newFood(dim, snake)
    else:
        snake.pop()
    return snake

def loseCondition(snake, dim):
    if snake[0] in snake[1:len(snake)-1]:
        return True
    elif min(snake[0])<0 or max(snake[0])>=dim:
        return True
    else:
        return False
    
def go(board):
    print(board)

def initWindow(dim, boxDim):
    winDim = dim*boxDim
    win = GraphWin('Snake2', winDim, winDim)
    for i in range(dim):
        Line(Point(i*boxDim,0), Point(i*boxDim, winDim)).draw(win) # vertical lines
        Line(Point(0, i*boxDim), Point(winDim, i*boxDim)).draw(win) # horizontal lines
    return win

def drawBoard(board, boxDim, win):
    dim = len(board)
    winDim = dim*boxDim 
    for row in range(dim):
        for col in range(dim):
            tile = board[row][col]
            rect = Rectangle(Point(col*boxDim, row*boxDim), Point((col+1)*boxDim, (row+1)*boxDim))
            if tile == 3: # Food
                rect.setFill('red')
                rect.draw(win)
            elif tile == 2: # SnakeHead
                rect.setFill('black')
                rect.draw(win)
            elif tile == 1: # SnakeTail
                rect.setFill('green')
                rect.draw(win)
            else: # WhiteSpace
                rect.setFill('white')
                rect.draw(win)
    return win

################################################# Main  ################################################# 
def main():
    # Definitions
    dim = 10
    gameOn = True
    board = np.zeros((dim,dim))
    snake= []

    # Init Move Interface
    moveInterface = move_interface.KeyboardInterface() # Keyboard input

    # Init display window
    boxDim = 25
    win = initWindow(dim, boxDim)
    
    # Init snake, food, board
    snake = initSnake(dim)
    newFood(dim, snake)
    updateBoard(snake, dim)
#    go(board)

    
    # Main loop
    while(gameOn):
        snake = updateSnake(snake, dim, moveInterface.nextDirection())
        if loseCondition(snake, dim):
            score = len(snake)-1
            print('Game Over! \nYour score: {0}'.format(score))   
            break
        board = updateBoard(snake, dim)
        go(board)
        win = drawBoard(board, boxDim, win)
        sleep(0.3)        
main()
