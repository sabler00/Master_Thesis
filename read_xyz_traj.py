import os
import sys
import numpy as np
from ase.io import read
from ase import Atoms
from statistics import mean



mytraj = sys.argv[1]

traj = read(mytraj, ":")

z1 = []
z2 = []
z3 = []
z4 = []
z5 = []
z6 = []
z7 = []
z8 = []
z9 = []
z10 = []
z11 = []
z12 = []
z13 = []
z14 = []
z15 = []
z16 = []


for idx, frames in enumerate(traj):
    for i in range(0, 399, 8):
        z1.append(  mean ( [ z[2] for z in frames.positions[i+4:i+8]    ] ) ) # average z coordinates of layer 
        z2.append(  mean ( [ z[2] for z in frames.positions[i:i+4]  ] ) ) # average z coordinates of layer 
    for i in range(400, 799, 8):
        z3.append(  mean ( [ z[2] for z in frames.positions[i+4:i+8]  ] ) ) # average z coordinates of layer 
        z4.append(  mean ( [ z[2] for z in frames.positions[i:i+4] ] ) ) # average z coordinates of layer 
    for i in range (800, 1199, 8): 
        z5.append(mean([z[2] for z in frames.positions[i+4:i+8]]))
        z6.append(mean([z[2] for z in frames.positions[i:i+4]]))
    for i in range (1200, 1599, 8): 
        z7.append(mean([z[2] for z in frames.positions[i+4:i+8]]))
        z8.append(mean([z[2] for z in frames.positions[i:i+4]]))
    for i in range(1600, 1999, 8):
        z9.append(  mean ( [ z[2] for z in frames.positions[i+4:i+8]    ] ) ) # average z coordinates of layer 
        z10.append(  mean ( [ z[2] for z in frames.positions[i:i+4]  ] ) ) # average z coordinates of layer 
    for i in range(2000, 2399, 8):
        z11.append(  mean ( [ z[2] for z in frames.positions[i+4:i+8]  ] ) ) # average z coordinates of layer 
        z12.append(  mean ( [ z[2] for z in frames.positions[i:i+4] ] ) ) # average z coordinates of layer 
    for i in range (2400, 2799, 8): 
        z13.append(mean([z[2] for z in frames.positions[i+4:i+8]]))
        z14.append(mean([z[2] for z in frames.positions[i:i+4]]))
    for i in range (2800, 3199, 8): 
        z15.append(mean([z[2] for z in frames.positions[i+4:i+8]]))
        z16.append(mean([z[2] for z in frames.positions[i:i+4]]))

z_averages = []

for i in range(1, 17):
    var_name = "z" + str(i)
    current_var = globals()[var_name]
    z_averages.append(sum(current_var)/len(current_var))



interlayer_distance = []
z_averages.sort()

for i in range(len(z_averages)-1):
    interlayer_distance.append(z_averages[i+1] - z_averages[i])
print(interlayer_distance)











