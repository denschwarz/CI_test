from math import sqrt, asin, sin, cos

gravity_constant = 6.67430*10**(-11)
astronomical_unit = 149597870700

mass_sun = 1.989*10**30
radius_sun = 696340000

def gravity_force(m1, m2, r):
    G = gravity_constant
    return m1*m2*G/(r**2)

def distance(pos1, pos2):
    (x1,y1) = pos1
    (x2,y2) = pos2
    return sqrt( (x1-x2)**2 + (y1-y2)**2 )