class Tree:
    def __init__(self,name):
        self.height = 0
        self.age = 0
        self.name = name

    @property
    def grow(self):
        self.age+=1
        self.height = self.age*2
        return f'{self.name} is {self.age} yrs old, {self.name} height is {self.height} m'
    
    @property
    def cut_dowm(self):
        print (f'{self.name} has cut down... (:')

maple = Tree('Maple')
oak = Tree ('Oak')

       
class FruitTree(Tree):
    def __init__(self,name,_country):
        super().__init__(name)
        self._country = _country
    @property
    def fruits_harvest(self):
        self.fruit = self.age*5
        return f'{self.name} harvest from {self._country} - {self.fruit} kg'

orange = FruitTree('Orange','Marocco')
lemon = FruitTree ('Lemon', 'India')
mango = FruitTree ('Mango','Brazil')

print (mango.grow)
print (mango.grow)
print (mango.fruits_harvest)
mango.cut_dowm