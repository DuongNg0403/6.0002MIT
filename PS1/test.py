import random
def test():
    stepChoices = [(0.0,1.1), (0.0,-.9), (1,0), (-1,0)]
    return random.choice(stepChoices)
xDist, yDist=test()
print(xDist)
print(yDist)