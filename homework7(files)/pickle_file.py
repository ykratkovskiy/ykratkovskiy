import pickle

class Point:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'Это точка с координатами {self.x} и {self.y}' 



x = '9'
y = '6'

with open ('pickle_x_y','wb') as coordinates:
    pickle.dump(x,coordinates)
    pickle.dump(y,coordinates)


with open ('pickle_x_y','rb') as coordinates:
    x1_1 = pickle.load (coordinates)
    y1_1 = pickle.load (coordinates)
    

pt1 = Point(x1_1,y1_1)
print (str(pt1))