##################################################################################
# Day 3: Dive!
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Desafio 1 do Advent of Code;
# Using the inputs calculate the final depth and position of the submarine.
##################################################################################

# Libraries, working directory and inputs
import pandas as pd
import os

os.getcwd()
os.chdir('E:\\Github\\adventofcode2021')

data = pd.read_csv('inputDay2.txt', names={'input':1})

# Solution: Part 1
data

data.assign(command = data['input'].map(lambda x: x.split(sep=' ')[0]),
            size    = data['input'].map(lambda x: int(x.split(sep=' ')[1]))
            ).drop('input',axis=1
                   ).groupby(by='command'
                             ).agg({'size':sum}).transpose(
                                 ).assign(result = lambda df: (df['down']-df['up'])*df['forward'])

# Solution: Part 2
inputs = data['input'].map(lambda x: x.split(' '))

depth = int(0)
aim   = int(0) 
hori  = int(0)
for i in range(1000):
    current_command = inputs[i][0]
    size            = int(inputs[i][1])
    if  current_command == 'forward':
        hori  += size
        depth += (aim*size)
    else : 
        if current_command == 'up':
            aim   -= size
        else : 
            aim   += size
    print([current_command,size,depth,aim,hori])
    
hori*depth
