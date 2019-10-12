from math import *

def decibel(value,unit):
    value_dB=10*log(value/unit, 10)
    return value_dB

def val(value_dB,unit):
    value=unit*10**(value_dB/10)
    return value

#Constants
Re = 6371*1000                      #[m]
k = 1.38e-23                        #[J/K]
c = 3e8                             #[m/s]
mu_earth= 3.986e14                  #[m^3/s^2]
AU = 149597870700                   #[m]
mu_mars = 4.282837e13               #[m^3/s^2]
mu_venus = 3.24859e14               #[m^3/s^2]
mu_europa = 3.2034543e12            #[m^3/s^2]
mu_moon = 4.9048695e12              #[m^3/s^2]
Rmars = 3389.5*1000                 #[m]
Reuropa = 1560.8*1000               #[m]
Rmoon = 1737.1*1000                 #[m]
Rvenus = 6051.8*1000                #[m]
min_dist_moon_earth = 363104000     #[m]
dist_mars_sun = 1.524               #[AU]
dist_venus_sun = 0.7                #[AU]
dist_europa_sun = 5.2               #[AU]
