"""
Write a program to solve a classic puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
"""

def solve(numheads, numlegs):
    for rab in range(numheads + 1):
        chicken = numheads - rab  # Calculate chickens based on rabbits
        if 2 * chicken + 4 * rab == numlegs:  # Check if the legs match
            return chicken, rab

numheads = 35
numlegs = 94
print(solve(numheads, numlegs))