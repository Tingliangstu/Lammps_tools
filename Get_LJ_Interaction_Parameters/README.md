# Get_LJ_Interaction_parameter  

A small program for obtaining LJ (Lennard-Jones) interactions between different elements from the UFF force field (a universal force developed by Rappe et al).

These parameters are very useful for constructing a two-dimensional (2D) vertical heterostructure composed of a van der Waals force interaction.
And they are also very useful for building multi-layer 2D materials.

As used by these two references:
1. Liang T, Zhou M, Zhang P, et al., [Int. J. Heat Mass Transf. 151, 119395 (2020)](https://www.sciencedirect.com/science/article/pii/S0017931019350446)
2. Liang T, Zhang P, Yuan P, et al., [Phys. Chem. Chem. Phys. 20, 21151-21162 (2018)](https://pubs.rsc.org/en/content/articlelanding/2018/CP/C8CP02831A#!divAbstract)

## How to Use (Generally used for lammps input)

You want to get the LJ interaction parameters of different elements, just put the LJ_data.csv and Get_Interaction_parameter.m files in the same folder, and run the .m file.
The specific calculation process of these parameters can be viewed in the [Formula.pdf](https://github.com/Tingliangstu/Lammps_tools/blob/master/Get_LJ_Interaction_Parameters/Formula.pdf) file.

Please contact me if you have any questions or suggestions.

Email: liangting.zj@gmail.com

## News

The Python version of this script is done by [Dr. Jingzhong Fang](https://github.com/fangjzh).

One can use it through this [link](https://github.com/fangjzh/Lammps_tools/blob/master/Get_LJ_Interaction_Parameters/Get_Interaction_parameter.py).

