"""
This module provides the script for the course Intermediate Python:
https://www.datacamp.com/courses/intermediate-python

Dependencies:
- matplotlib
- pandas

This script uses pylint to ensure that the code follows best practices
and is free from common mistakes and errors.
"""

# Import matplotlib.pyplot as plt
import numpy as np

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Import pandas as pd
import pandas as pd

# edited/added
year=list(range(1950,2100+1))
pop=list(np.loadtxt('pop1.txt', dtype=float))

# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# edited/added
gdp_cap=list(np.loadtxt('gdp_cap.txt', dtype=float))
life_exp=list(np.loadtxt('life_exp.txt', dtype=float))

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

# edited/added
pop=list(np.loadtxt('pop2.txt', dtype=float))

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clear plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clear plot again
plt.show()
plt.clf()

# edited/added
life_exp1950=list(np.loadtxt('life_exp1950.txt', dtype=float))

# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
XLAB = 'GDP per Capita [in USD]'
YLAB = 'Life Expectancy [in years]'
TITLE = 'World Development in 2007'

# Add axis labels
plt.xlabel(XLAB)
plt.ylabel(YLAB)

# Add title
plt.title(TITLE)

# After customizing, display the plot
plt.show()

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

# edited/added
col=list(np.loadtxt('col.txt', dtype=str))

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del europe['australia']

# Print europe
print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83 }

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.iloc[5, 2])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

# Comparison of booleans
print(True is False)  # pylint: disable=R0133

# Comparison of integers
print(-5 * 15 != 75)

# Comparison of strings
print("pyscript" == "PyScript")  # pylint: disable=R0133

# Compare a boolean with a numeric
print(True == 1)  # pylint: disable=R0133, R0124, C0121

# Comparison of integers
X = -3 * 6
print(X >= -10)

# Comparison of strings
Y = "test"
print("test" <= Y)

# Comparison of booleans
print(True > False)  # pylint: disable=R0133

# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

# Define variables
MY_KITCHEN = 18.0
YOUR_KITCHEN = 14.0

# MY_KITCHEN bigger than 10 and smaller than 18?
print(10 < MY_KITCHEN < 18)

# MY_KITCHEN smaller than 14 or bigger than 17?
print(MY_KITCHEN < 14 or MY_KITCHEN > 17)

# Double MY_KITCHEN smaller than triple YOUR_KITCHEN?
print(MY_KITCHEN * 2 < YOUR_KITCHEN * 3)

# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# Define variables
ROOM = "kit"
AREA = 14.0

# if statement for ROOM
if ROOM == "kit" :
    print("looking around in the kitchen.")

# if statement for AREA
if AREA > 15 :
    print("big place!")

# Define variables
ROOM = "kit"
AREA = 14.0

# if-else construct for ROOM
if ROOM == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for AREA :
if AREA > 15 :
    print("big place!")
else :
    print("pretty small.")

# Define variables
ROOM = "bed"
AREA = 14.0

# if-elif-else construct for ROOM
if ROOM == "kit" :
    print("looking around in the kitchen.")
elif ROOM == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for AREA
if AREA > 15 :
    print("big place!")
elif AREA > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)

# Initialize OFFSET
OFFSET = 8

# Code the while loop
while OFFSET != 0 :
    print("correcting...")
    OFFSET = OFFSET - 1
    print(OFFSET)

# Initialize OFFSET
OFFSET = -6

# Code the while loop
while OFFSET != 0 :
    print("correcting...")
    if OFFSET > 0 :
        OFFSET = OFFSET - 1
    else :
        OFFSET = OFFSET + 1
    print(OFFSET)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for AREA in areas :
    print(AREA)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, AREA in enumerate(areas) :
    print("ROOM " + str(index) + ": " + str(AREA))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Adapt the printout
for index, AREA in enumerate(areas) :
    print("ROOM " + str(index + 1) + ": " + str(AREA))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for x in house :
    print("the " + x[0] + " is " + str(x[1]) + " sqm")

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

# Iterate over europe
for key, value in europe.items() :
    print("the capital of " + str(key) + " is " + str(value))

# edited/added
mlb = pd.read_csv('baseball.csv')
np_height = np.array(mlb['Height'])
np_weight = np.array(mlb['Weight'])
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
np_baseball = np.array(baseball)

# For loop over np_height
for x in np_height[:5]: # edited/added
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(x)

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Set seed
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# NumPy is imported, seed is set

# Starting STEP
STEP = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    STEP = STEP - 1
elif dice <= 5 :
    STEP = STEP + 1
else :
    STEP = STEP + np.random.randint(1,7)

# Print out dice and STEP
print(dice)
print(STEP)

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set STEP: last element in random_walk
    STEP = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next STEP
    if dice <= 2:
        STEP = STEP - 1
    elif dice <= 5:
        STEP = STEP + 1
    else:
        STEP = STEP + np.random.randint(1,7)

    # append next_STEP to random_walk
    random_walk.append(STEP)

# Print random_walk
print(random_walk)

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    STEP = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure STEP can't go below 0
        STEP = max(0, STEP - 1)
    elif dice <= 5:
        STEP = STEP + 1
    else:
        STEP = STEP + np.random.randint(1,7)

    random_walk.append(STEP)

print(random_walk)

# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    STEP = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        STEP = max(0, STEP - 1)
    elif dice <= 5:
        STEP = STEP + 1
    else:
        STEP = STEP + np.random.randint(1,7)

    random_walk.append(STEP)

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        STEP = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            STEP = max(0, STEP - 1)
        elif dice <= 5:
            STEP = STEP + 1
        else:
            STEP = STEP + np.random.randint(1,7)
        random_walk.append(STEP)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        STEP = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            STEP = max(0, STEP - 1)
        elif dice <= 5:
            STEP = STEP + 1
        else:
            STEP = STEP + np.random.randint(1,7)
        random_walk.append(STEP)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        STEP = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            STEP = max(0, STEP - 1)
        elif dice <= 5:
            STEP = STEP + 1
        else:
            STEP = STEP + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            STEP = 0

        random_walk.append(STEP)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        STEP = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            STEP = max(0, STEP - 1)
        elif dice <= 5:
            STEP = STEP + 1
        else:
            STEP = STEP + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            STEP = 0
        random_walk.append(STEP)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
