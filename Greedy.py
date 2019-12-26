from food import Food
'''
    Choosing what to eat at a meal such that doesn't exceed a certain
    amount of calories
'''

def buildMenu(names, values, calories):
    """names, values, calories lists of same length.
        name a list of strings
        values and calories lists of numbers
        returns list of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunc):
    """Assumes items a list, maxCost >= 0,
keyFunction maps elements of items to numbers"""
    itemCopy = sorted(items, key = keyFunc, reverse = True)
    result = []
    totalVal, totalCost = 0.0, 0.0
    for i in range (len(itemCopy)):
        if(totalCost + itemCopy[i].getCost())<= maxCost:
            result.append(itemCopy[i])
            totalCost+= itemCopy[i].getCost()
            totalVal += itemCopy[i].getValue()

    return (result,totalVal)


def testGreedy(items, constraint, keyFunc):
    (taken, val) = greedy(items, constraint, keyFunc)
    print("Total value of item taken: {}".format(val))
    for item in taken:
        print(item)


def testGreedys(foods, maxUnits):
    print("Use greedy by value to allocate {} calories".format(maxUnits))
    testGreedy(foods, maxUnits, Food.getValue)
    print("\n Use greedy by cost to allocate {} calories".format(maxUnits))
    testGreedy(foods, maxUnits, lambda x: 1/ Food.getCost(x))
    print("\n Use greedy by density to allocate {} calories".format(maxUnits))
    testGreedy(foods, maxUnits, Food.trueValue)

names =  ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)