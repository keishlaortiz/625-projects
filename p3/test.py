from parser import *
from utils import *
"""
Tested at server compute.cs.tamu.edu (faster execution)
"""
"""
Prints the names of the cities in the tour
"""
def print_cities(cities):
    for i in xrange(len(cities)):
        if i != 0 and i % 9 == 0:
            print ""
        print cities[i].name,

    print "\n"
"""
Temperature Schedule: Linear schedule
parameter:
 1. k - the iteration value
"""
def TempSchedule(k):
    return temp * (ITERATIONS+1 - k) / (ITERATIONS+1)

"""
Simulated Annealing function
parameter:
1. tour - the initial state
"""
def SA(tour):
    current_length = totalDistance(tour)
    print "initial state, tour length={0} miles".format(current_length)
    print_cities(tour)

    for k in xrange(1,ITERATIONS+1):
        possible_successor = randomSuccessor(tour)
        new_length = totalDistance(possible_successor)
        delta = new_length - current_length
        newTemp = TempSchedule(k)
        p = math.exp(-delta/newTemp)
        print "iter={0} len={1} newlen={2} delta={3} temp={4} p<{5}".format(k,current_length,new_length,delta,newTemp,p)
        data.write(str(k)+" "+str(current_length)+"\n")
        if delta < 0 or random.random() < p:
            tour = possible_successor
            current_length = new_length
            print "update! len={0}".format(current_length)
            print_cities(tour)

    return (tour,current_length)

pFile = Parser("texas-cities.dat.txt")

cities = pFile.parseFile() #the default initial state

option = str(sys.argv[1]).lower()
ITERATIONS = int(sys.argv[2])
temp = float(sys.argv[3])

#d for default initial state and r for random initial state
sys.stdout = open("output.txt","w")
data = open("data.txt","w")
if option == 'r':
    random.shuffle(cities)
    
result = SA(cities)
print ""
print "Solution with {0} iterations, initial temperature {1} and tour length of {2} miles".format(ITERATIONS,temp,result[1])
print ""
print_cities(result[0])


data.close()

