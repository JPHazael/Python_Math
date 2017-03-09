from math import sqrt
import random
import numpy as np

print "Let's take the standard deviation of a list of 10 random numbers?"

my_randoms=[random.randrange(1,101,1) for _ in range (10)]

print my_randoms

print "The mean of this list is?"

mean = np.mean(my_randoms)

print mean

print "The differences from the mean are:"

difference = [(i - mean) for i in my_randoms]

print difference

print "The squares of the diferences are:"

squares = [i ** 2 for i in difference]

print squares


print "The variance for this list of numbers is:"

variance = np.mean(squares)

print variance

print "The standard deviation of this list is:"

print sqrt(variance)