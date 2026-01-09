# T-xy Diagram Generator for Binary Solutions (Personal Project)
A Python program that produces the T-xy diagram of a binary mixture of two chosen liquid species. Computes **Bubble-Point** and **Dew-Point** curves using numerical root-finding.

## Background & Scientific Principles
A **T-xy diagram** displays the mole composition (in both liquid and vapour phase) of a binary mixture (two species) at different temperatures and a constant pressure. The key principles applied in my code are the **Ideal Gas Law**, **Raoult's Law**, and the **Antoine Equation**. These three principles effectively describe the relation between several properties of liquids and their respective vapours in a system at phase equilibrium (pressure, temperature, mole fraction). 

## Features
1. Takes two inputs of liquid species from a list of various different liquids (the first species selected, whose mole composition is in the horizontal axis of the diagram, should conventionally be the more volatile species)
2. Takes a pressure input (in mmHg)
3. Calculates bubble-point and dew-point temperatures (in <sup>o</sup>C) at each liquid and vapour mole composition respecitvely
4. Generates T-xy graphs for chosen binary mixtures and pressures

## Logic & Applied Equations
Antoine constants are uniquely assigned based on the chosen liquid species. 

Two equations are set up in order to compute bubble-point and dew-point temperatures numerically using **fsolve** in **SciPy**. Both equations are derived from **Raoult's Law** and the **Antoine Equation**. 

### Equation for numerically computing temperature at each liquid mole composition (bubble-point curve):
![Bubble Point](https://latex.codecogs.com/png.latex?\dpi{120}x_1\,10^{A_1-\frac{B_1}{T+C_1}}+x_2\,10^{A_2-\frac{B_2}{T+C_2}}-P_{total}=0)

### Equation for numerically computing temperature at each vapour mole composition (dew-point curve): 
![Dew Point](https://latex.codecogs.com/png.latex?\dpi{120}y_1\,\frac{P_{total}}{10^{A_1-\frac{B_1}{T+C_1}}}+y_2\,\frac{P_{total}}{10^{A_2-\frac{B_2}{T+C_2}}}-1=0)

## Examples of Usage

## Assumptions & Limitations

## Future Work 
