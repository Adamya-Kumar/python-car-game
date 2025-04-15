import  random

class Dice:
    def roll(self):
        self.genrateRandomValue()
        self.randomNum = (self.x,self.y)
        self.printRandomDiceValue()

    def genrateRandomValue(self):
       self.x=random.randint(1,6)
       self.y=random.randint(1,6)
      
    def printRandomDiceValue(self):
        print(self.randomNum)

dice1=Dice()
dice1.roll()
