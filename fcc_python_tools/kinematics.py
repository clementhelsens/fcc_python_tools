import awkward1 as ak
import numpy as np

#Momentum
def calc_p(array, container):
    return np.sqrt(array[container,'p4.px']**2 + array[container,'p4.py']**2 + array[container,'p4.pz']**2)

#Transverse momentum
def calc_pt(array, container):
    return np.sqrt(array[container,'p4.px']**2 + array[container,'p4.py']**2)

#Pseudorapidity
def calc_eta(array, container):
    return np.arcsinh(array[container,'p4.pz'] / calc_pt(array, container))

#Phi
def calc_phi(array, container):
    return np.arccos(array[container,'p4.px'] / calc_pt(array, container))

#Invariant mass of 2 particles
def mass_2body(left, right, left_mass, right_mass):
    left_energy = np.sqrt(left['p4.p']**2 + left_mass**2)
    right_energy = np.sqrt(right['p4.p']**2 + right_mass**2)
    return np.sqrt(((left_energy + right_energy)**2 -
            (left['p4.px'] + right['p4.px'])**2 -
            (left['p4.py'] + right['p4.py'])**2 -
            (left['p4.pz'] + right['p4.pz'])**2))

# Cosine of angle between two particles
def cos_angle(left, right):
    left_px_mag = left['p4.px'] / left['p4.p']
    left_py_mag = left['p4.py'] / left['p4.p']
    left_pz_mag = left['p4.pz'] / left['p4.p']

    right_px_mag = right['p4.px'] / right['p4.p']
    right_py_mag = right['p4.py'] / right['p4.p']
    right_pz_mag = right['p4.pz'] / right['p4.p']

    return left_px_mag*right_px_mag + left_py_mag*right_py_mag + left_pz_mag*right_pz_mag
