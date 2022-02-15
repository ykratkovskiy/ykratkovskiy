def concat (*args:str,**kwargs)->str:
    if True in kwargs.values():
        result = ("".join([i for i in args[::-1]]))
    else:
        result = ("".join([i for i in args]))
    return (result) 
a = list(map(str,input('Введите слова через запятую: ').split(',')))
b = bool(input('''Введите значение параметра reversed: Нажмите любую клавишу и затем "Enter" если "True".
Нажмите только "Enter" если "False") ''' ,))
def inspect(f):
    def inner (*args, **kwargs):
        res = f(*args, **kwargs)
        print (f'Args:{args}')
        print (f'Kwargs:{kwargs}')
        print (f'retvalue {res}')
        return res
    return inner
concat = inspect(concat)
concat (*a, reversed=b)