# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 19:33:08 2026

@author: stone
"""

"""
constants data for temp in C and pressure in mmHg
https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781118135341.app1
"""

from numpy import *
from scipy.optimize import fsolve
from matplotlib.pyplot import * 

firstSubstance = input("Name first substance: ").lower()
secondSubstance = input("Name second substance: ").lower()
sysPressure = float(input("Pressure in mmHg: "))

def antoinePressure(substance, tempC):
    if substance == "toluene":
        A, B, C = 6.95334, 1343.943, 219.377
    
    elif substance == "benzene":
        A, B, C = 6.90565, 1211.033, 220.79

    elif substance == "n-heptane":
        A, B, C = 6.9024, 1268.115, 216.9

    elif substance == "n-hexane":
        A, B, C = 6.87776, 1171.53, 224.366
    
    elif substance == "ethanol":
        A, B, C = 8.20417, 1642.89, 230.30

    elif substance == "water":
        A, B, C = 7.94917, 1657.462, 227.02
    
    else:
        raise ValueError("Invalid substance")
        
    return 10 ** (A - B/(tempC + C))

def bubPointTemp(x1, substance1, substance2, mmHgPressure):
    def bubPointEqu(tempC):
        x2 = 1 - x1
        return x1*antoinePressure(substance1, tempC) + x2*antoinePressure(substance2, tempC) - mmHgPressure
    return float(fsolve(bubPointEqu, 100)[0])

def dewPointTemp(y1, substance1, substance2, mmHgPressure):
    def dewPointEqu(tempC):
        y2 = 1 - y1
        return y1*mmHgPressure/antoinePressure(substance1, tempC) + y2*mmHgPressure/antoinePressure(substance2, tempC) - 1
    return float(fsolve(dewPointEqu, 100)[0])

xDomain = linspace(0,1,100)
yDomain = linspace(0,1,100)
bubTempList = []
dewTempList = []
for i in xDomain:
    temp = bubPointTemp(i, firstSubstance, secondSubstance, sysPressure)
    
    bubTempList.append(temp)

for i in yDomain:
    temp = dewPointTemp(i, firstSubstance, secondSubstance, sysPressure)
    
    dewTempList.append(temp)

plot(xDomain, bubTempList, "b-", label="Bubble-Point Curve")
plot(yDomain, dewTempList, "r-", label="Dew-Point Curve")
xlabel("Mol Fraction of Substance 1 (x,y)")
ylabel("Temperature(C)")
legend()
title("T-xy Diagram")
show()



