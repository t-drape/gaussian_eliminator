"""
Author: TJ Drape
Date: August 8th, 2025
Purpose: Implement Gaussian Elimination for linear equations in Python
"""
import numpy as np

# Now, assume equations are given in echelon form
# Scale to n equations
def gaussian_eliminator(*args) -> list:
    """ Performs Gaussian Elimination on the input linear system """
    system = np.array(list(args))
    # Echelon Form
    system = align_system(system)

    num_variables = len(system[0])
    for current_variable in range(0, num_variables):
        new_system = reduce_system(current_variable, system.copy())
        if not(np.array_equal(new_system, system)):
            system = new_system
            system = align_system(system.copy())
            print(system)
    return system


def reduce_system(current_variable, system):
    """ Perform algebra to reduce the equations in the system, returns a reduced system of equations """
    index = current_variable
    for equation in system[current_variable:]:
        if index != current_variable and equation[current_variable] != 0:
            factor = -(system[index][current_variable] / system[current_variable][current_variable])
            print(f"Row {current_variable+1} * {factor} + Row {index+1}")
            system[index] = np.add(system[index], (system[current_variable] * factor))
        index += 1
    return system
    

def align_system(input_system):
    """ Returns a given system of equations in echelon form """
    current_row = 0
    next_row = 1
    length = len(input_system)

    while next_row < length:
        current_equation = input_system[current_row][0:-1]
        next_equation = input_system[next_row][0:-1]
        for elt, other in np.nditer([current_equation, next_equation]):
            if elt == 0 and other != 0:
                nr = input_system[next_row].copy()
                input_system[next_row], input_system[current_row] = input_system[current_row], nr
                align_system(input_system) # Restarts the process, in case an equation needs to "bubble up" even further
        next_row += 1
        current_row += 1
    return input_system


# Add any number of equations and variables, last place in the array is for the value of the equation
x = np.array([1, 2, 3, 4, 3])
y = np.array([-1, -4, 3, 8, -6])
z = np.array([1, 4, 6, 12, 3])
my_system = np.array([x, y, z])
gaussian_eliminator(x,y,z)
