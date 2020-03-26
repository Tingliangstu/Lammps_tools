# Deal_Lammps_dump_files

**A small script for processing lammps dump files, including matlab and python versions**

The lammps dump file used in this tool looks like this:
```
ITEM: TIMESTEP
3000000
ITEM: NUMBER OF ATOMS
4650
ITEM: BOX BOUNDS pp pp pp
-6.2150000000000005e-01 6.1497498999999998e+01
-7.0029999999999997e-03 2.1549299700000000e+02
-3.2999999999999998e+00 6.7000000000000002e+00
ITEM: ATOMS id type x y z f_Totaltemperatom 
102 2 1.2624 7.86677 1.68123 298.989 
106 2 3.73959 7.87872 1.75115 299.745 
110 2 6.21105 7.8436 1.69641 295.124 
114 2 8.69724 7.84617 1.6999 296.704 
......
```
## Features
- [x] Can read lammps dump file containing multiple frames
- [x] Can handle very large files quickly (For matlab version)
- [x] Easy to use and modify

## Usage
----
1. For matlab version

   You need to modify several parameters in `Deal_dump_files.m` according to your case:
   
   **Output_interval**: Interval steps for output dump file in lammps
   
   **Total_running_steps**: The total number of running steps of lammps during the production period
   
   **dump_columns**: The number of columns in the dump file (Modify according to your own output)
   ``` matlab
    run Deal_dump_files.m file
   ```
   **Tips**: The use of the `textscan` command is key in the matlab version.
2. For python version 
   ``` python 
    python Deal_dump_files.py
   ```
   **You can modify python version after running and use it freely**
----
## Example
* For matlab version

  In the example, the `dump.main` file was processed. And the lammps command is as follows:
   ```
   variable            output_interval        equal         500000
   dump                1     all     custom   ${output_interval}    dump.main   id   type   x   y   z   f_Totaltemperatom 
   dump_modify         1     sort    id          #Sort each atom order
  
   run                   4000000                 # Total_running_steps
   ```

## TODO

C++ version 

## Contact

Please contact me if you have any questions or suggestions.

Email: liangting.zj@gmail.com
