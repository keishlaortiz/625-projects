import math
import random
import sys
import copy

"""
Generates a random successor by swapping two random cities
"""
def randomSuccessor(cities):
    i = random.randint(0,len(cities)-1)
    j = random.randint(0,len(cities)-1)

    while i == j:
        i = random.randint(0,len(cities)-1)
        j = random.randint(0,len(cities)-1)

    newTour = copy.deepcopy(cities)

    newTour[i], newTour[j] = newTour[j], newTour[i]

    return newTour

"""
Calculates total distance 
"""
def totalDistance(cities):
    dist = 0
    for i in xrange(len(cities)-1):
        dist += distance(cities[i],cities[i+1])

    dist += distance(cities[-1],cities[0])
    
    return round(dist,2)
"""
Calculates distance in miles
"""
def distance(c1,c2):
    rLat1 = degreeToRadian(c1.latitude)
    rLat2 = degreeToRadian(c2.latitude)

    rLon1 = degreeToRadian(c1.longitude)
    rLon2 = degreeToRadian(c2.longitude)

    dlon = rLon2 - rLon1
    dlat = rLat2 - rLat1
    
    a = pow(math.sin(dlat/2),2)+math.cos(rLat1)*math.cos(rLat2)*pow(math.sin(dlon/2),2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a)) * 3961
    return c

"""
Conversion from degree to radian
"""
def degreeToRadian(degree):

    return degree*3.14159/180.0
