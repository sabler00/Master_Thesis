import numpy as np 

# Define the dimensions of the water box
box_xmin = -0.615349
box_ymin = -0.355660
box_zmin = -496.646000
box_xmax = 23.996651
box_ymax = 20.957225
box_zmax = 503.354000

# Define the number of water molecules in each dimension
num_x = float((box_xmax - box_xmin) / 3.5)  # Assuming water molecules are separated by 3 Å
num_y = float((box_ymax - box_ymin) / 3.5)
num_z = float((box_zmax - box_zmin) / 3.5)

#x = box_xmax - box_xmin
#y = box_ymax - box_ymin
#z = box_zmax - box_zmin

#print(x, y, z)

# Create an XYZ file
with open("waterbox.xyz", "w") as xyz_file:
    xyz_file.write(f"{num_x * num_y * num_z}\n")
    xyz_file.write("Water box\n")

    for k in np.arange(box_zmin, box_zmax, 3.5):
        for j in np.arange(box_ymin, box_ymax, 3.5):
            for i in np.arange(box_xmin, box_xmax, 3.5):
                x = i 
                y = j 
                z = k 

                # Water molecule 1 (oxygen)
                xyz_file.write(f"O {x} {y} {z}\n")

                # Water molecule 2 (hydrogen)
                xyz_file.write(f"H {x + 1.290} {y + 0.860} {z}\n")

                # Water molecule 3 (hydrogen)
                xyz_file.write(f"H {x + 1.290} {y - 0.860} {z}\n")
