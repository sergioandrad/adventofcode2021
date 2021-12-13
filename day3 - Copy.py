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
import os
    
os.getcwd()
os.chdir('E:\\Github\\adventofcode2021')
    
bingoOrder = pd.read_csv('inputDay4.txt',names=dict(zip(list(range(0,100)),list(range(0,100)))),nrows=1, sep =','
                         ).transpose(
                             ).rename(columns={0:'input'})
    
# Solution: Part 1 

num_lines = sum(1 for line in open('inputDay4.txt'))


dict(zip(['c'+str(i) for i in range(6)],[i for i in range(6)]))

inputs = pd.read_csv('inputDay4.txt',names = {'input':0}, skiprows=1, dtype={'input':'string'})

boards = list()
for i in range(83):
    L = 0 + i*6
    U = 1 + 5 + i*6
    boards.append([(lambda x: x.replace('  ',' ').lstrip().rstrip().split(' '))(x) for x in inputs.iloc[L:U,0]])
    
arrayBoards = np.array(boards)

def checkBingo(x, bingo): 
    if x == str(bingo):
        return 'X'
    else:
        return x
        
checkBingoV = np.vectorize(checkBingo)
checkBingoV(arrayBoards[0,:,:],25)

arrayBoards.shape[0]

for x in range(100):
    for i in range(arrayBoards.shape[0]):
        checkBingo(arrayBoards[i,:,:],bingoOrder[i,0])
    

                   
                
# Solution: Part 2               
