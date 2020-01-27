###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cowDict = {}
    
    f = open(filename, "r")
    line = f.readline()
    while line:
        
        line = line.replace("\n","")
        splittedLine = line.split(',')
        
        #print(splittedLine)
        #print(splittedLine[0])
        #print(splittedLine[1])
        cowDict[splittedLine[0]] = int(splittedLine[1])
        line = f.readline()
    f.close()
    return cowDict
    



    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    allTrip = []
    currentTrip = []
    cowCopy = {k:v for k,v in sorted(cows.items(),key = lambda x: x[1], reverse=True)}#important
    #print(cowCopy)
    while len(cowCopy) != 0:
        currentTrip=[list(cowCopy.items())[0][0]]#dict.items() is iterable but not indexible so convert it to list
        avail =limit - list(cowCopy.items())[0][1]
        cowCopy.pop(currentTrip[0])
        for n in cowCopy.copy():
            if cowCopy[n] <=avail:
                currentTrip.append(n)
                avail-= cowCopy[n]
                cowCopy.pop(n)
            else:
                continue
        allTrip.append(currentTrip)                
    #print(allTrip)
    return allTrip  ################  O(n^2)
    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    bestTrip = []
    cow_set = cows.keys()
    leastTrip = 0
    for cowTrip in get_partitions(cow_set):
        
        for trip in cowTrip:
            weightSum = 0
            for cow in trip:
                weightSum+= cows[cow]
            if weightSum > limit:
                break
        if len(cowTrip)<=leastTrip:
            bestTrip = cowTrip
            leastTrip = len(bestTrip)

    return bestTrip
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


############ TESTING ##############
cowDict = load_cows("C:\\Users\\MikeN\Python\\6.0002MIT\\PS1\\ps1_cow_data.txt")
greedy_cow_transport(cowDict, 10)
#print(cowDict)