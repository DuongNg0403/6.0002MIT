import random
import math
#############################DICE ROLLING###########################
def rollDice():
    return random.choice([1,2,3,4,5,6])

def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDice())
        if result == goal:
            total+= 1
    print('Actual probability of', txt, '=', 1/(6**len(goal)))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability of', txt, '=',estProbability) 

#runSim('111', 1000, '111') 
########################BIRTHDAY SIMULATION#######################
def sameDate(numPeople, numSame):
    possibleDates =  range(366)
    birthDays = [0]*366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthDays[birthDate] += 1
    return max(birthDays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits+= 1
    return numHits/numTrials


def combination(n, k):
    numerator =math.factorial(n)
    denom = math.factorial(k)*math.factorial(n-k)
    return numerator/denom

for numPeople in [10,20,40,100]:
    print('For', numPeople,'est. prob. of a shared birthday is',birthdayProb(numPeople, 2, 10000)) 
    numer = math.factorial(366)
    denom = math.factorial(366-numPeople)*(366**numPeople)
    print('Actual prob. for N = 100 =',1 - numer/denom) 