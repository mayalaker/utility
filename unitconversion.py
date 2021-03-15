# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:35:41 2019

@author: Maya
"""

#Unit conversion program
#A library of functions that input a quantity 
#and returns that quantity in a different unit system

########################################################################
# List functions
########################################################################
def list_length():
    print("Inches to meters: in2m")
    print("Meters to inches: m2in")
    print("Meters to astronomical units: m2au")
    print("Astronomical units to meters: au2m")
    print("Meters to light years: m2ly")
    print("Light years to meters: ly2m")
    print("Astronomical units to light years: au2ly")
    print("Light years to astronomical units: ly2au")
    print("Solar radii to meters: sr2m")
    print("Meters to solar radii: m2sr")
    print("Earth radii to meters: er2m")
    print("Meters to Earth radii: m2er")
    print("Parsecs to light years: pc2ly")
    print("Light years to parsecs: ly2pc")
    print("Parsecs to meters: pc2m")
    print("Meters to parsecs: m2pc")
    print("Parsecs to astronomical units: pc2au")
    print("Astronomical units to parsecs: au2pc")
    return

def list_mass():
    print("Pounds to kilograms: lb2kg")  
    print("Kilograms to pounds: kg2lb")
    print("Solar mass to kilograms: sm2kg")
    print("Kilograms to solar mass: kg2sm")
    print("Earth mass to kilograms: em2kg")
    print("Kilograms to Earth mass: kg2em")
    print("Solar mass to Earth mass: sm2em")
    print("Earth mass to solar mass: em2sm")
    print("Newtons to pounds: n2lb")
    print("Pounds to Newtons: lb2n")
    print("Atomic mass units to kilograms: u2kg")
    print("Kilograms to atomic mass units: kg2u")
    print("Atomic mass units to MeV/c^2: u2mev")
    print("MeV/c^2 to atomic mass units: mev2u")
    return

def list_time():
    print("Seconds to minutes: s2min")
    print("Minutes to seconds: min2s")
    print("Seconds to hours: s2hr")
    print("Hours to seconds: hr2s")
    print("Seconds to days: s2day")
    print("Days to seconds: day2s")
    print("Seconds to years: s2yr")
    print("Years to seconds: yr2s")
    print("Days to years: day2yr")
    print("Years to days: yr2day")
    return

def list_temperature():
    print("Celcius to Kelvin: c2k")
    print("Kelvin to Celcius: k2c")
    print("Farenheit to Kelvin: f2k")    
    print("Kelvin to Farenheit: k2f")
    print("Farenheit to Celcius: f2c")
    print("Celcius to Farenheit: c2f")
    return

def list_angles():
    print("Degrees to radians: deg2rad")
    print("Radians to degrees: rad2deg")
    return

def list_energy():
    print("Electron volts to Joules: ev2j")
    print("Joules to electron volts: j2ev")
    print("Solar luminosity to Watts: sl2w")
    print("Watts to solar luminostiy: w2sl")
    return

def list_all():
    print("\nLength:")
    list_length()
    print("\nMass:")
    list_mass()
    print("\nTime:")
    list_time()
    print("\nTemperature:")
    list_temperature()
    print("\nAngle:")
    list_angles()
    print("\nEnergy:")
    list_energy()
    return

#######################################################################
# Length
#######################################################################

def in2m(x):
    return 0.0254 * x

def m2in(x):
    return 39.3701 * x

def m2au(x):
    return 6.68459e-12 * x

def au2m(x):
    return 1.496e+11 * x

def m2ly(x):
    return 1.057e-16 * x

def ly2m(x):
    return 9.461e+15 * x

def au2ly(x):
    return 1.58125e-5 * x

def ly2au(x):
    return 63241.1 * x

def sr2m(x):
    return 6.9550826e8 * x

def m2sr(x):
    return x / 6.9550826e8

def er2m(x):
    return x * 6.378136e6

def m2er(x):
    return x / 6.378136e6

def pc2ly(x):
    return x * 3.2615638

def ly2pc(x):
    return x / 3.2615638

def pc2m(x):
    return x * 3.0856776e16

def m2pc(x):
    return x / 3.0856776e16

def pc2au(x):
    return x * 206264.806

def au2pc(x):
    return x / 206264.806


#######################################################################
# Weight and Mass
#######################################################################

def lb2kg(x):
    return 0.453592 * x

def kg2lb(x):
    return 2.20462 * x

def sm2kg(x):
    return 1.9891e30 * x

def kg2sm(x):
    return x / 1.9891e30

def em2kg(x):
    return 5.9736e24 * x

def kg2em(x):
    return x / 5.9736e24

def sm2em(x):
    return (1.9891e30 / 5.9736e24) * x

def em2sm(x):
    return (5.9736e24 / 1.9891e30) * x

def n2lb(x):
    return x * 0.22480894

def lb2n(x):
    return x * 4.4482216

def u2kg(x):
    return x * 1.66053878283e-27

def kg2u(x):
    return x / 1.66053878283e-27

def u2mev(x):
    return x * 931.49402883

def mev2u(x):
    return x / 931.49402883


#######################################################################
# Time
#######################################################################

def s2min(x):
    return 0.0166667 * x

def min2s(x):
    return 60 * x

def s2hr(x):
    return 0.000277778 * x

def hr2s(x):
    return 3600 * x

def s2day(x):
    return 1.15741e-5 * x

def day2s(x):
    return 86400 * x

def s2yr(x):
    return 3.17098e-8 * x

def yr2s(x):
    return 3.154e+7 * x

def day2yr(x):
    return 0.00273973 * x

def yr2day(x):
    return 365 * x

######################################################################
# Temperature
######################################################################

def c2k(x):
    return 273.15 + x

def k2c(x):
    return x - 273.15

def f2k(x):
    return (x + 459.67) * (5/9)

def k2f(x):
    return (x * (9/5)) - 459.67

def f2c(x):
    return (x - 32) * (5/9)

def c2f(x):
    return (x * (9/5)) + 32

#######################################################################
# Angles
#######################################################################

def deg2rad(x):
    return 0.0174533 * x

def rad2deg(x):
    return 57.2958 * x

#######################################################################
# Energy
#######################################################################

def ev2j(x):
    return x * 1.602176487e-19

def j2ev(x):
    return x / 1.602176487e-19
    
def sl2w(x):
    return x * 3.8395e26

def w2sl(x):
    return x / 3.8395e26
    
    
    
    
########################################################################
# Constants
########################################################################

    
    
    
    
    
    
    
    
    