##################################################################################
# Day 3: Binary Diagnostic
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Desafio 1 do Advent of Code;
# Extract the most and least common number for each digit position and 
# conver the binary to an int in order to find the answer, bin0*bin1.
##################################################################################
# Libraries, working directory and inputs
import pandas as pd
import numpy as np
import copy as cp
import os
    
os.getcwd()
os.chdir('E:\\Github\\adventofcode2021')
    
bingoOrder = pd.read_csv('inputDay4.txt',names=dict(zip(list(range(0,100)),list(range(0,100)))),nrows=1, sep =','
                         ).transpose(
                             ).rename(columns={0:'input'})
    
num_lines = sum(1 for line in open('inputDay4.txt'))
inputs    = pd.read_csv('inputDay4.txt',names = {'input':0}, skiprows=1, dtype={'input':'string'})

# Cleaning and assembling bingo boards
boards = list()
for i in range(83):
    L = 0 + i*5
    U = 5 + i*5
    boards.append([(lambda x: x.replace('  ',' ').lstrip().rstrip().split(' '))(x) for x in inputs.iloc[L:U,0]])
    
arrayBoards = np.array(boards)

# Marking draws and checking which one wins first
def checkBingo(x, bingo): 
    if x == str(bingo):
        return 'X'
    else:
        return x
        
checkBingoV = np.vectorize(checkBingo)
arrayBoardsCopy = cp.deepcopy(arrayBoards)

def checkMarks(x): 
    if x == 'X':
        return 0
    else:
        return int(x)
checkMarksV = np.vectorize(checkMarks)    
        
listPass    = list() # stores boards that already won
listNumbers = list() # stores winning number for each board
for x in range(100):
    print(x)
    for i in range(arrayBoards.shape[0]):
        if i in listPass:
            continue
        else:
            arrayBoards[i,:,:] = checkBingoV(arrayBoards[i,:,:], str(bingoOrder.iloc[x,0]))
            print(i)
            print(arrayBoards[i,:,:])
            for k in range(5):
                if np.all(arrayBoards[i,k,:] == ['X', 'X', 'X', 'X', 'X']) or np.all(arrayBoards[i,:,k] == ['X', 'X', 'X', 'X', 'X']):
                    listPass.append(i)
                    listNumbers.append(bingoOrder.iloc[x,0])
   
# Solution: Part 1
bestBoard = listPass[0]
firstWinNumber = listNumbers[0]
firstWinNumber*(checkMarksV(arrayBoards[bestBoard,:,:]).sum())

# Solution: Part 2  
worstBoard = listPass[-1]
lastWinNumber = listNumbers[-1]
lastWinNumber*(checkMarksV(arrayBoards[worstBoard,:,:]).sum())


# old code for part 1
# breaknow = 0
# for x in range(100):
#     print(x)
#     for i in range(arrayBoards.shape[0]):
#         arrayBoards[i,:,:] = checkBingoV(arrayBoards[i,:,:], str(bingoOrder.iloc[x,0]))
#         print(i)
#         print(arrayBoards[i,:,:])
#         for k in range(5):
#             if np.all(arrayBoards[i,k,:] == ['X', 'X', 'X', 'X', 'X']) or np.all(arrayBoards[i,:,k] == ['X', 'X', 'X', 'X', 'X']):
#                 breaknow = 1
#                 bestBoard = i
#                 lastNumberCalled = x
#     if breaknow == 1: 
#             break          

