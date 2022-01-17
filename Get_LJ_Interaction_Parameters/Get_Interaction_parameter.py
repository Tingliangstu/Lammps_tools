#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  csv   #import  csv lib
import math 

print('Applicable only to metal units in lammps.')
print('By Ting Liang')

Data=[]

import csv
with open('LJ_data4py.csv')as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        Data.append(row)

## Enter two elements that you want to get LJ interactions
elememt_1 = 'W'
elememt_2 = 'Nb'
## Need to pay attention to the capitalization of letters

for irow in Data:
    if(irow['element'] == elememt_1):
        elememt_1_distance =  float(irow['distance'])
        elememt_1_energy = float(irow['energy'])
    if(irow['element'] == elememt_2):
        elememt_2_distance =  float(irow['distance'])
        elememt_2_energy = float(irow['energy'])    
## Calculate LJ parameters using mixing rules (Lorentz-Berthelot mixing rules) (For lammps script input)...
# In the UFF force field paper, the energy unit is kcal/mol, and the distance unit is angstrom (A)
# In the metal unit of lammps, the energy unit is ev, and the distance unit is angstrom (A).

Distance_constant = ((elememt_1_distance + elememt_2_distance)/2) / math.pow(2, 1/6)
# The unit is A (angstrom)

Energy_constant = math.sqrt(elememt_1_energy * elememt_2_energy) * 0.0433641
# Units converted from kcal/mol to ev (* 0.0433641 )

## Output result 

print("The distance_constant between %s and %s is %f (Angstrom)." %(elememt_1, elememt_2, Distance_constant))
# The unit is A (angstrom)
print('The energy_constant between %s and %s is %f (eV).'%(elememt_1, elememt_2, Energy_constant))
# The unit is ev

print('You can use these parameters as lammps input')
# Maybe other extensions are possible
print("end")