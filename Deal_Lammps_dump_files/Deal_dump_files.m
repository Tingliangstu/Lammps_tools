 %% Read dump file
 
 clc, clear, close all
 disp('A script to deal with the dump file of lammps.');
 tic;
 
 %% Set up some parameters related to the dump file
 
 % Inpute / Output file name
 in_file = 'dump.main';                                                                         % Dump file name
 save_file_name_1 = 'coordinate_all.mat';                                            % Output  file for coordinate data
 
 % Read the information of the simulation box in the dump file
 fileID = fopen(in_file, 'r');
 atoms = textscan(fileID, '%n', 1, 'HeaderLines', 3, 'Delimiter', '\t');      % Number of particles   (You should read the textscan command carefully)
 box = textscan(fileID, '%n %n', 3, 'HeaderLines', 2, 'Delimiter', '\t');    % Extract box information
 fclose(fileID);
 
 Total_atoms = atoms{1};                                                                     % Number of atoms 
 len_header = 9;                                                                                   % Skip comments          (may have to  change acording to your system )
 N = Total_atoms + len_header;                                                           % Length of block
 
 %%  Parameters from MD simulation
 
 Output_interval = 500000;                                                                  % Dump output interval (step)
 Total_running_steps = 4000000;                                                         % The total number of running steps of lammps during the production period
 Ns = Total_running_steps / Output_interval;                                       % Total number of dump point  (number of frames)
 
 % If you have more output (columns) in your dump file, you must modify this value
 
 dump_columns = 6;                                                                            % The number of columns in the dump file (Modify according to your own output)
 
 %% Deal with data
 
 coordinate_all = zeros(Total_atoms, dump_columns, Ns);
 fileID = fopen(in_file);
 form = '%n ';
 formatSpec = repmat(form, 1, dump_columns);                                 % Equivalent to the number of dump_columns = x
 
 for i = 1:Ns
     
      C = textscan(fileID, formatSpec, N, 'HeaderLines', len_header, 'Delimiter', '\t');
      
      for  j = 1 : dump_columns
          
            coordinate_all(:,j,i) = C{1, j};                                                       % Extract all the coordinate information (Including all frames)
                                                                                                              % Of course, it can also contain only the information you want (need to modify)
      end
end

fclose(fileID);

save(save_file_name_1, 'coordinate_all')                                                 % Maybe you need to output the data for backup

frame_traversal =  coordinate_all(:, :, 1);                                                 % For test 

%%  Box information

lx = box{1, 2}(1) - box{1, 1}(1);
ly = box{1, 2}(2) - box{1, 1}(2);
lz = box{1, 2}(3) - box{1, 1}(3);

Size = [lx, ly, lz];                                                                                       % Box size

%% Information display

disp ('The size of the simulation box is: ' );
disp ('   lx             ly              lz');
disp (Size);
disp ('Processing is complete and you can use these data!!!');

toc;