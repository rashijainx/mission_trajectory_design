import math
import numpy

from get_planet_data import Planet


planet = Planet.from_yaml("planet_data.yaml", "Earth")

r_unit = (1.6772, -1.6772, 2.3719)
r_1 = planet.scale_vec_by_radius(r_unit)  # km
v_1 = (3.1574, 2.4987, 0.4658)  # already km/s

r_1_mag = numpy.linalg.norm(r_1)
v_1_mag = numpy.linalg.norm(v_1) 

## Objective: 
## a, e, i, omega, w, thetaS

## a
## Equation 1: energy = -v^2/2 - mu/r
## Equation 2: energy = -mu/(2*a)
energy = (v_1_mag**2 / 2) - (planet.mu_km3s2 / r_1_mag)
a = -planet.mu_km3s2/(2 * energy)

## e 
## Equation 1: h = cross (r, v)
## Equation 2: p = h^2 / mu 
## Equation 3: p = a * (1 - e^2)

h = numpy.cross(r_1, v_1)
h_mag = numpy.linalg.norm(h) 
p = h_mag**2/planet.mu_km3s2 
e = math.sqrt(1 - p/a)

