#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
The assumed commands used for dumping the velocities from LAMMPS is as follows:
dump  vels  all  custom  10  dump.gr  id  type  vx  vy  vz  
dump_modify vels sort id
'''
           
import  numpy  as  np
import  linecache
import  os

def read_lammps_velocity(dump_file):

      # using 'linecache' get the line information  in lammps
      line_number_1 = 4                                      # Total atoms
      line_number_2 = 9                                      # ITEM: ATOMS id type vx vy vz (in my case)
      
      atoms_number = int(linecache.getline(dump_file, line_number_1).strip())       # Get total numbers in your system
      Judging_characters = linecache.getline(dump_file, line_number_2).strip()      # Get the information in line 9
      
      ''' Use linecache function to directly read the number of atoms in the fourth line of the file '''
     
      print ("The number of atoms in your system is %s\n" % atoms_number)
    
      add_flag = False

      velocity_all = []
    
      with open(dump_file) as f:                          
        
          for line in f:
                if "ITEM:" in line and Judging_characters not in line:
                    add_flag = False
                    continue            
                    
                elif Judging_characters in line:
                    add_flag = True
                    continue
                
                if add_flag:
                    if line.strip():
                    	
                        entries = line.strip().split()
                        
                        '''Just extract the velocity information. Of course,  it can also contain only the information you want (need to modify)'''
                        velocity_atom = [float(t) for t in entries[2:5]]
                        velocity_all.append(velocity_atom) 
                        
      return np.array(velocity_all, dtype = float),  atoms_number
    

if __name__ == '__main__':
     
     Deal_file = input("Please enter a file name to process (dump.) and press the Enter key: ")
     
     if not os.path.isfile(Deal_file):
          
          raise ValueError("\nSorry, the file " + Deal_file + " does not exist or not in this folder.")
          
     else:

          print ('\nProcessing file is starting, please wait !!!\n') 
           
     velocity, atoms_number = read_lammps_velocity(Deal_file)

     n_frame = int (np.size(velocity, 0) / atoms_number) - 1
          
     print('The frame number of the output velocity file is %s.\n' % n_frame )
          
     save_files = input ('Please enter the name of the file you want to output: ')

     np.savetxt(save_files, velocity)

     print('\nProcessing is complete and you can use these data.\n')
