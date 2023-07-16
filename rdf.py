import scipy as sp
import numpy as np
from matplotlib import pyplot as plt


def atom_vol(z, r, z_bot, z_top):
    volume = 4.0 / 3.0 * sp.pi * r ** 3

    if z + r > z_top:
        h = z + r - z_top
        volume -= sp.pi * h ** 2 * (r - h / 3.0)

    elif z - r < z_bot:
        h = z - r + z_bot
        volume -= sp.pi * h ** 2 * (r - h / 3.0)

    return volume


def distance(a, b):
    dx = abs(a[0] - b[0])
    x = min(dx, abs(A - dx))

    dy = abs(a[1] - b[1])
    y = min(dy, abs(B - dy))

    dz = abs(a[2] - b[2])
    z = min(dz, abs(C - dz))

    return sp.sqrt(x ** 2 + y ** 2 + z ** 2)


class Trajectory:
    def __init__(self, filename, skip, z_bot_interface, z_top_interface, interface_offset=4.0, resolution=200):
        """ 
        self             : pointer to current object
        filename         : path to the trajectory file 
        skip             : number of snapshots to be skipped between two configurations that are evaluated
                           (for example, if trajectory is 9000 steps long, and skip = 10, every tenth step
                           is evaluated, 900 steps in total; use skip = 1 to take every step of the MD)
        z_bot_interface  : average vertical coordinate for interface below water layer in Angstrom
        z_top_interface  : average vertical coordinate for interface above water layer in Angstrom
        interface_offset : distance between interface and region of water with bulk-like properties
        resolution       : number of points in the final radial distribution function """

        self.rdf = 0
        self.radii = 0
        self.volume_per_h2o = 0
        with open(filename, 'r') as f:
            data = f.readlines()

        self.z_top = z_top_interface - interface_offset
        self.z_bot = z_bot_interface + interface_offset

        self.n_atoms = int(data[0])
        self.n_steps_total = int(len(data) / self.n_atoms)

        self.atom_list = [line.split()[0] for line in data[1: self.n_atoms + 1]]

        self.skip = skip
        self.n_steps = self.n_steps_total / self.skip

        self.coordinates = np.zeros((self.n_steps, self.n_atoms, 3))

        for step in range(self.n_steps):
            coords = np.zeros((self.n_atoms, 3))

            i = step * self.skip * (self.n_atoms + 2)
            for j, line in enumerate(data[i + 2: i + self.n_atoms + 2]):
                coords[j, :] = [float(value) for value in line.split()[1:]]

            self.coordinates[step] = coords

        self.resolution = resolution
        self.compute_volume_per_h2o()

    def compute_volume_per_h2o(self):
        n_h2o = 0
        for step in range(self.n_steps):
            for i, atom in enumerate(self.coordinates[step]):
                if self.atom_list[i] == "O":
                    n_h2o += 1

        self.volume_per_h2o = A * B * (self.z_top - self.z_bot) * self.n_steps / n_h2o

    def compute_radial_distribution(self):
        """ no reason to go above half of the smallest lattice parameter as mirror images start 
        to be double-counted """
        r_cutoff = min(A, B) / 2.0
        dr = r_cutoff / self.resolution
        volumes = np.zeros(self.resolution)

        self.radii = sp.linspace(0.0, self.resolution * dr, self.resolution)
        self.g_of_r = np.zeros(self.resolution)

        for step in range(self.n_steps):
            print('{:4d} : {:4d}'.format(step, self.n_steps))

            """ isolate all liquid water molecules based on the position of the oxygen atoms """
            data_oxygen = []
            for i, atom in enumerate(self.coordinates[step]):
                if self.atom_list[i] == "O":
                    if self.z_bot < atom[2] < self.z_top:
                        data_oxygen.append(atom)
            data_oxygen = sp.array(data_oxygen)

            """ loop over each pair of H2O molecules, calculate their distance, build a histogram 
            each pair is evaluated as two contributions to the distribution function """
            for i, oxygen1 in enumerate(data_oxygen):
                for j in range(self.resolution):
                    r1 = j * dr
                    r2 = r1 + dr
                    v1 = volume(oxygen1[2], r1, self.z_bot, self.z_top)
                    v2 = volume(oxygen1[2], r2, self.z_bot, self.z_top)
                    volumes[j] += v2 - v1

                for oxygen2 in data_oxygen[i:]:
                    dist = distance(oxygen1, oxygen2)
                    index = int(dist / dr)
                    if 0 < index < self.resolution:
                        self.g_of_r[index] += 2.0

        """ normalize by the volume of the spherical shell corresponding to each radius """
        for i, value in enumerate(self.g_of_r):
            self.g_of_r[i] = value * self.volume_per_h2o / volumes[i]

    def plot(self, filename=""):
        """ plots the radial distribution function
        if filename is specified, prints it to file as a pdf """

        if not self.g_of_r:
            print('compute the radial distribution function first\n')
            return

        plt.xlabel('r (Å)')
        plt.ylabel('g$_{O-O}$(r)')
        plt.plot(self.radii, self.g_of_r)

        if filename:
            plt.savefig('radial_distribution_function.pdf', dpi=300, bbox='tight', format='pdf')

        plt.show()


A = 32.382287464521355 - (-31.978589464547184)
B = 8.428445250056132 - (-15.706883250056134)
C = 10.768190250056133 - (-13.367138250056133)

bottom_interface = 23.0
top_interface = 40.0

H2O = Trajectory('wat_dump_CHOLi.xyz', 10, bottom_interface, top_interface)
H2O.compute_radial_distribution()
H2O.plot()
