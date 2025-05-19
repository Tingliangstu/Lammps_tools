#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

# 检查是否提供了足够的参数
if len(sys.argv) != 3:
    print("请提供两个元素作为参数，例如：script.py W Hf")
    sys.exit(1)

# 直接从命令行参数获取值
elememt_1 = sys.argv[1]
elememt_2 = sys.argv[2]

print(f"第一个元素: {elememt_1}")
print(f"第二个元素: {elememt_2}")


import  csv   #import  csv lib
import math 

print('Applicable only to metal units in lammps.')
print('From Ting Liang s matlab program')
print('python script by Jingzhong Fang')

Data=[]

import csv
with open('LJ_data.csv')as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        Data.append(row)

## Enter two elements that you want to get LJ interactions
# elememt_1 = 'W'
# elememt_2 = 'Hf'
## Need to pay attention to the capitalization of letters

for irow in Data:
    if(irow['Species_i'] == elememt_1):
        elememt_1_distance =  float(irow['sigma'])
        elememt_1_energy = float(irow['epsilon'])
    if(irow['Species_j'] == elememt_2):
        elememt_2_distance =  float(irow['sigma'])
        elememt_2_energy = float(irow['epsilon'])    
## Calculate LJ parameters using mixing rules (Lorentz-Berthelot mixing rules) (For lammps script input)...
# In the UFF force field paper, the energy unit is kcal/mol, and the distance unit is angstrom (A)
# In the metal unit of lammps, the energy unit is ev, and the distance unit is angstrom (A).

Distance_constant = ((elememt_1_distance + elememt_2_distance)/2) / math.pow(2, 1/6)
# The unit is A (angstrom)

Energy_constant = math.sqrt(elememt_1_energy * elememt_2_energy) ## * 0.0433641 # already converted to ev
# Units converted from kcal/mol to ev (* 0.0433641 )

## Output result 

print("The distance_constant between %s and %s is %f (Angstrom)." %(elememt_1, elememt_2, Distance_constant))
# The unit is A (angstrom)
print('The energy_constant between %s and %s is %f (eV).'%(elememt_1, elememt_2, Energy_constant))
# The unit is ev

print('You can use these parameters as lammps input')
# Maybe other extensions are possible
print("end")