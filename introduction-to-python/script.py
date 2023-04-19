"""
This module provides the script for the course Introduction to Python.

Reference: https://www.datacamp.com/courses/intro-to-python-for-data-science

Dependencies:
- pandas

This script uses flake8 & pylint to ensure that the code follows best practices
and is free from common mistakes and errors.
"""

# Import the math package
import math
# Import radians function of math package
from math import radians

# Import the numpy package as np
import numpy as np
# Import the pandas package as pd
import pandas as pd

# Example, do not modify!
print(5 / 8)

# Put code below here
print(7 + 10)

# Division
print(5 / 8)

# Addition
print(7 + 10)

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# Calculate two to the power of five
print(2 ** 5)

# Create a variable SAVINGS
SAVINGS = 100

# Print out SAVINGS
print(SAVINGS)

# Create a variable SAVINGS
SAVINGS = 100

# Create a variable GROWTH_MULTIPLIER
GROWTH_MULTIPLIER = 1.1

# Calculate RESULT
RESULT = SAVINGS * GROWTH_MULTIPLIER ** 7

# Print out RESULT
print(RESULT)

# Create a variable DESC
DESC = 'compound interest'

# Create a variable PROFITABLE
PROFITABLE = True

SAVINGS = 100
GROWTH_MULTIPLIER = 1.1
DESC = 'compound interest'

# Assign product of SAVINGS and GROWTH_MULTIPLIER to YEAR1
YEAR1 = SAVINGS * GROWTH_MULTIPLIER

# Print the type of YEAR1
print(type(YEAR1))

# Assign sum of DESC and DESC to DOUBLEDESC
DOUBLEDESC = DESC + DESC

# Print out DOUBLEDESC
print(DOUBLEDESC)

# Definition of SAVINGS and RESULT
SAVINGS = 100
RESULT = 100 * 1.10 ** 7

# Fix the printout
print('I started with $' +
      str(SAVINGS) +
      ' and now have $' +
      str(RESULT) +
      '. Awesome!')

# Definition of PI_STRING
PI_STRING = '3.1415926'

# Convert PI_STRING into float: pi_float
pi_float = float(PI_STRING)

# Area variables (in square meters)
HALL = 11.25
KIT = 18.0
LIV = 20.0
BED = 10.75
BATH = 9.50

# Create list areas
areas = [HALL, KIT, LIV, BED, BATH]

# Print areas
print(areas)

# area variables (in square meters)
HALL = 11.25
KIT = 18.0
LIV = 20.0
BED = 10.75
BATH = 9.50

# Adapt list areas
areas = ['hallway', HALL,
         'kitchen', KIT,
         'living room', LIV,
         'bedroom', BED,
         'bathroom', BATH]

# Print areas
print(areas)

# area variables (in square meters)
HALL = 11.25
KIT = 18.0
LIV = 20.0
BED = 10.75
BATH = 9.50

# house information as list of lists
house = [['hallway', HALL],
         ['kitchen', KIT],
         ['living room', LIV],
         ['bedroom', BED],
         ['bathroom', BATH]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

# Create the areas list
areas = ['hallway', 11.25,
         'kitchen', 18.0,
         'living room', 20.0,
         'bedroom', 10.75,
         'bathroom', 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ['hallway', 11.25,
         'kitchen', 18.0,
         'living room', 20.0,
         'bedroom', 10.75,
         'bathroom', 9.50]

# Sum of kitchen and bedroom area: EAT_SLEEP_AREA
EAT_SLEEP_AREA = areas[3] + areas[-3]

# Print the variable EAT_SLEEP_AREA
print(EAT_SLEEP_AREA)

# Create the areas list
areas = ['hallway', 11.25,
         'kitchen', 18.0,
         'living room', 20.0,
         'bedroom', 10.75,
         'bathroom', 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Create the areas list
areas = ['hallway', 11.25,
         'kitchen', 18.0,
         'living room', 20.0,
         'bedroom', 10.75,
         'bathroom', 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]

# Create the areas list
areas = ['hallway', 11.25,
         'kitchen', 18.0,
         'living room', 20.0,
         'bedroom', 10.75,
         'bathroom', 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change 'living room' to 'chill zone'
areas[4] = 'chill zone'

# Create the areas list (updated version)
areas = ['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0,
         'bedroom', 10.75, 'bathroom', 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ['poolhouse', 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ['garage', 15.45]

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

# Create variables VAR1 and VAR2
VAR1 = [1, 2, 3, 4]
VAR2 = True

# Print out type of VAR1
print(type(VAR1))

# Print out length of VAR1
print(len(VAR1))

# Convert VAR2 to an integer: OUT2
OUT2 = int(VAR2)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in DESCending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

# string to experiment with: PLACE
PLACE = 'poolhouse'

# Use upper() on PLACE: PLACE_UP
PLACE_UP = PLACE.upper()

# Print out PLACE and PLACE_UP
print(PLACE)
print(PLACE_UP)

# Print out the number of o's in PLACE
print(PLACE.count('o'))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

# Definition of radius
R = 0.43

# Calculate C
C = 2 * R * math.pi

# Calculate A
A = math.pi * R ** 2

# Build printout
print('Circumference: ' + str(C))
print('Area: ' + str(A))

# Definition of radius
R = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
dist = R * radians(12)

# Print out dist
print(dist)

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# edited/added
mlb = pd.read_csv('baseball.csv')

# height_in is available as a regular list
height_in = mlb['Height'].tolist()

# height_in is available as a regular list

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

# edited/added
weight_lb = mlb['Weight'].tolist()

# height_in and weight_lb are available as regular lists

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)

# height_in and weight_lb are available as a regular lists

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# height_in and weight_lb are available as a regular lists

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# baseball is available as a regular list of lists

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

# edited/added
baseball = pd.read_csv('baseball.csv')[['Height', 'Weight']]

# baseball is available as a regular list of lists

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player
print(np_baseball[123, 0])

# edited/added
baseball = pd.read_csv('baseball.csv')[['Height', 'Weight', 'Age']]
n = len(baseball)
updated = np.array(pd.read_csv('update.csv', header=None))

# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

# np_baseball is available

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# np_baseball is available

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print('Average: ' + str(avg))

# Print median height. RePLACE 'None'
med = np.median(np_baseball[:, 0])
print('Median: ' + str(med))

# Print out the standard deviation on height. RePLACE 'None'
stddev = np.std(np_baseball[:, 0])
print('Standard Deviation: ' + str(stddev))

# Print out correlation between first and second column. RePLACE 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print('Correlation: ' + str(corr))

# edited/added
fifa = pd.read_csv('fifa.csv',
                   skipinitialspace=True,
                   usecols=['position', 'height'])
positions = list(fifa.position)
heights = list(fifa.height)

# heights and positions are available as lists

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. RePLACE 'None'
print('Median height of goalkeepers: ' + str(np.median(gk_heights)))

# Print out the median height of other players. RePLACE 'None'
print('Median height of other players: ' + str(np.median(other_heights)))
