##################################################################################
# Day 1: Sonar Sweep
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Desafio 1 do Advent of Code;
# Count the number of times a depth measurement increases from the previous measurement.
# (There is no measurement before the first measurement.)
##################################################################################

# Libraries, working directory and inputs
import pandas as pd
import os

os.getcwd()
os.chdir('E:\\Github\\adventofcode2021')

data = pd.read_csv('input.txt', names = {'depth':1})

# Solution: Part 1
data.assign(depth1 = lambda dataframe: dataframe['depth'].shift(-1)
            ).assign(flag_inc = lambda dataframe: dataframe['depth'] < dataframe['depth1']
                     ).loc[:,'flag_inc'].sum()

# Solution: Part 2
data.assign(depth1 = lambda dataframe: dataframe['depth'].shift(1),
            depth2 = lambda dataframe: dataframe['depth'].shift(2)
            ).dropna(
                ).assign(
                    sliding3      = lambda dataframe: dataframe['depth']+dataframe['depth1']+dataframe['depth2']
                ).assign(
                    sliding3shift = lambda dataframe: dataframe['sliding3'].shift(-1)).assign(
                    flag_inc      = lambda dataframe: dataframe['sliding3'] < dataframe['sliding3shift']
                    ).loc[:,'flag_inc'].sum()
                    
