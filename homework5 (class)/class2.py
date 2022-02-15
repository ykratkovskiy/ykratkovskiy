from abc import ABC
class Point:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'Это точка с координатами {self.x} и {self.y}'

class Line:
    def __init__(self,pt1,pt2):
        self.pt1 = pt1
        self.pt2 = pt2
       
    def length(self)-> float:
        return (((self.pt2.x-self.pt1.x)**2)+((self.pt2.y-self.pt1.y)**2))**0.5
        

class Shape(ABC):
    def __init__(self,sh):
        self.sh = sh


class Square(Line,Shape):
    def __init__(self,sh,pt1,pt2):
        Shape.__init__(self,sh)
        Line.__init__(self,pt1,pt2)
    
    @property
    def perim(self)-> float:
        if self.sh == 'square':
            return f'Периметр квадрата равен {(self.length()*4)}'
        else:
            raise Exception ('Форма не является квадратом')
    @property
    def area(self)->float:
        if self.sh == 'square':
            return f'Площадь квадрата равна {(self.length()**2)}'
        else:
            raise Exception ('Форма не является квадратом')


class Cube(Square):
    def __init__(self,sh,pt1,pt2):
        Square.__init__(self,sh,pt1,pt2)
        
    def volume(self)->float:
            return f'Объем куба равен {(self.length()**3)}'


class Rect(Shape):
    def __init__(self,sh,lin1,lin2):
        self.lin1 = Line.length(lin1)
        self.lin2 = Line.length(lin2)
        Shape.__init__(self,sh)
    
    @property
    def perim_sq (self)->float:
        if self.sh == 'rect':
            return f'Периметр прямоугольника равен {(self.lin1)*2+(self.lin2)*2}'
        else:
                raise Exception ('Форма не является прямоугольником')
    @property
    def area_sq (self)->float:
        if self.sh == 'rect':
            return f'Площадь прямоугольника равна {(self.lin1)*(self.lin2)}'
        else:
                raise Exception ('Форма не является прямоугольником')

        
point1 = Point (-20,20)
point2 = Point (20,20)
point3 = Point (-20,-20)
point4 = Point (20,-20)
print (str(point1))
print (str(point2))
print (str(point3))
print (str(point4))

line1 = Line (point1,point2)
line2 = Line (point3,point4)
line3 = Line (point1,point3)
line4 = Line (point2,point4)


print (f'Длина первой линии равна {line1.length()}')
print (f'Длина первой линии равна {line2.length()}')
print (f'Длина третьей линии равна {line3.length()}')
print (f'Длина четвертой линии равна {line4.length()}')

sq = Square('square',point1,point2)
print (sq.perim)
print (sq.area)

cub = Cube('square',point1,point2)
print (cub.volume())

rec = Rect ('rect',line3,line4)
print (rec.perim_sq)
print (rec.area_sq)