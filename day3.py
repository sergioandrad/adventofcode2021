##################################################################################
# Day 3: Binary Diagnostic
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Desafio 1 do Advent of Code;
# Extract the most and least common number for each digit position and 
# conver the binary to an int in order to find the answer, bin0*bin1.
##################################################################################
# Libraries, working directory and inputs
import pandas as pd
import os
    
os.getcwd()
os.chdir('E:\\Github\\adventofcode2021')
    
data = pd.read_csv('inputDay3.txt', names={'input':1}, dtype={'input':'string'})
    
# Solution: Part 1 
inputList = list()
for i in range(1000):
    inputList.append(
        list(map(int, [x for x in data.iloc[i,0]])))

def majorDigit(x,cut):
    if x >= cut:
        return 1
    else:
        return 0
    
binary0 = ''   
binary1 = ''  
digitsDf    = pd.DataFrame(inputList)
majorDigits = digitsDf.agg('sum').map(lambda x: majorDigit(x,500))
for i in range(12):
 binary0 += str(majorDigits.iloc[i])
 binary1 += str(1-majorDigits.iloc[i])

int(binary0,2)*int(binary1,2)


# Solution: Part 2

colIndex = list(range(12))
names    = ['d'+str(i) for i in range(12)]
digitsDf = digitsDf.rename(dict(zip(colIndex,names)),axis='columns')

mostCommon  = list()    
leastCommon = list()

filterDigitM = majorDigit(digitsDf.iloc[:,0].agg('sum'),500)
filterDigitL = 1-filterDigitM

mostCommon.append(filterDigitM)
filteredM = digitsDf.query('d0==@mostCommon[0]')
lenM = len(filteredM.index)

leastCommon.append(filterDigitL)
filteredL = digitsDf.query('d0==@leastCommon[0]')    
lenL = len(filteredL.index)

for i in range(11):
    print(i)
   # most common digits
   # selection step
    filterDigitM = majorDigit(filteredM.iloc[:,i+1].agg('sum'),lenM/2)
    mostCommon.append(filterDigitM)
   # filter step 
    filteredM    = filteredM.query('d'+str(i+1)+'==@filterDigitM')
    lenM = len(filteredM.index)
    if lenM==1: break
    print(filteredM)
    
for i in range(11):    
    print(i)
   # least common digits
    filterDigitL = 1-majorDigit(filteredL.iloc[:,i+1].agg('sum'),lenL/2)
    leastCommon.append(filterDigitL) 
    filteredL    = filteredL.query('d'+str(i+1)+'==@filterDigitL')
    lenL = len(filteredL.index)
    if lenL==1: break
    print(filteredL)

rate0=''
rate1=''
for i in range(12):
    rate0+= str(filteredM.iloc[0,i])
    rate1+= str(filteredL.iloc[0,i])

int(rate0,2)*int(rate1,2)
