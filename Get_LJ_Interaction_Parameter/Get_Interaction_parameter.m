%% read UFF parameters

clc, clear, close all
disp('Applicable only to metal units in lammps.');
disp('By Ting Liang');

file1=fopen('LJ_data.csv');                                      % The data extracted by the python script has been artificially processed.

%% define some variables
formatSpec='%n %s %n %n %n %n %n %n';
N = 2;                                                                     % Number of rows read per read
len_header = 0;                                                       % Length of headerline

%% Open folder
M = textscan(file1, formatSpec, 'HeaderLines', len_header, 'Delimiter', ',');
fclose(file1);

%% Extract the LJ data
element = M{2};
distance = M{5};                                                       % The unit is A (angstrom)
energy = M{6};                                                         % The unit is kcal/mol

%% Enter two elements that you want to get LJ interactions

elememt_1 = 'B';
elememt_2 = 'P';                                                       % Need to pay attention to the capitalization of letters

%% Gets the distance and energy data of the two elements
[rows, ~] = size(element);  

% For elememt_1
for  i = 1 : rows
       if  (strcmpi(element{i, 1}, elememt_1)) 
           
            elememt_1_distance =  distance(i);
            elememt_1_energy = energy(i);
            
       end
end

% For elememt_2
for  k = 1 : rows
       if (strcmpi(element{k, 1}, elememt_2)) 
           
            elememt_2_distance = distance(k);   
            elememt_2_energy =  energy(k);     
            
      end
end

%% Calculate LJ parameters using mixing rules (Lorentz-Berthelot mixing rules) (For lammps script input)...
% In the UFF force field paper, the energy unit is kcal/mol, and the distance unit is angstrom (A)
% In the metal unit of lammps, the energy unit is ev, and the distance unit is angstrom (A).

Distance_constant = ((elememt_1_distance + elememt_2_distance)/2) / power(2, 1/6);      % The unit is A (angstrom)

Energy_constant = sqrt(elememt_1_energy * elememt_2_energy) * 0.0433641;                  % Units converted from kcal/mol to ev (* 0.0433641 )

%% Output result 

disp(['The distance_constant between ', elememt_1, ' and ', elememt_2, ' is: ', num2str(Distance_constant), ' (Angstrom).']);                                             % The unit is A (angstrom)
disp(['The energy_constant between ', elememt_1, ' and ', elememt_2, ' is: ', num2str(Energy_constant), ' (ev).']);                                                              % The unit is ev

disp('You can use these parameters as lammps input');                                                                                   % Maybe other extensions are possible
