##################################################################################
# Day 1: Sonar Sweep
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Desafio 1 do Advent of Code;
# Count the number of times a depth measurement increases from the previous measurement.
# (There is no measurement before the first measurement.)
##################################################################################


import pandas as pd
import os

os.getcwd()
os.chdir('E:\\Github\\adventofcode2021')

data = pd.read_csv('input.txt', names = {'depth':1})

pd.merge(data,data.shift(-1), left_index=True, right_index=True, how="inner").assign(
    flag_inc = lambda dataframe: dataframe['depth_x'] < dataframe['depth_y']).loc[:,'flag_inc'].sum()


