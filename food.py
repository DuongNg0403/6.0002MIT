class Food():
   
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def trueValue(self):
        return self.value/self.calories

    def __repr__(self):
        return "{} : < {}, {} >".format(self.name, self.value, self.calories)

    def __str__(self):
        return "{} : < {}, {} >".format(self.name, self.value, self.calories)
    

