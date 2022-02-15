import json

class Point:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'Это точка с координатами {self.x} и {self.y}' 


x_y = {'x':151,
       'y':350}

with open ('json_x_y','w') as coordinates:
    json.dump(x_y,coordinates)
    

with open ('json_x_y','r') as coordinates:
    x_y1 = json.load (coordinates)
    

x1 = x_y1.get('x')  
x2 = x_y1.get('y')  


pt1 = Point(x1,x2)
print (str(pt1))
