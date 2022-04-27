class NotEqualLen(Exception):
    pass
def NotEqualLen(q,w):
    if len(q)!=len(w):
        raise NotEqualLen('Количество катетов не равно!')

class nonposit(Exception):
    def nonposit(e):
        if e<=0:
            raise nonposit('Катет не может быть отрицательным или равным нулю!')
try:
    a = list(map(int,input('Введите последовательно значения катетов треугольников через запятую:').split(',')))
except ValueError:
    print ('Введено не число')

f =[]
s =[]
c =[]

for id,i in enumerate (a, start=1):
    nonposit(i)
    c.append(id)
    if id%2 == 0:
        f.append(i)
    else:
        s.append(i)

NotEqualLen(f,s)

gipot = [(((x**2)+(y**2))**0.5) for x,y in zip (f,s)]
square = [((x*y)/2) for x,y in zip (f,s)]

for count,x,y,sq,g in zip (c,f,s,square,gipot):                     
        print (f'Треугольник {count} с катетами {y} и {x} имеет площадь {sq} и гипотенузу {round(g,2)}')