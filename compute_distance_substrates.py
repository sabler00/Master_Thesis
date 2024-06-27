import numpy as np
import os
import pandas as pd
from statistics import mean

def extract_and_average_last_column(lines, atom_indices):
    averages = []
    step_size = 1480
    header_lines = 3
    num_steps = len(lines) // (step_size + header_lines)

    for step in range(num_steps):
        start = step * (step_size + header_lines)
        end = start + step_size + header_lines
        step_lines = lines[start:end]
        
        step_values = []
        for index in atom_indices:
            line_index = index + header_lines

            columns = step_lines[line_index].split()[1:]
            if len(columns) == 3: 
                    last_column_value = float(columns[-1])
                    step_values.append(last_column_value)
                
        average_value = sum(step_values) / len(step_values)
        averages.append(average_value)


    return averages


""" for step in range(num_steps):
    step_frame = df[:,step*] """


file_path = '/home/sal/qmcf_examples/graphite_qmmm_setup/graphite-md-02.xyz'


df = pd.read_csv(file_path, delim_whitespace=True, header = None, skiprows= 1)

df = df.drop(df[df.iloc[:, 0] == 'X'].index)
df = df.drop(df[df.iloc[:, 0] == '1481'].index)
#df = df.drop(to_drop)
#print(df[df.iloc[:,0] == 1481])
#print(df[df.iloc[:, 0] == '1481'])


df = df.reset_index(drop = True)
#df = df.drop()
print(df)


""" atom_indices = range(1153, 1481)
averages = extract_and_average_last_column(lines, atom_indices)
print(averages)
 """