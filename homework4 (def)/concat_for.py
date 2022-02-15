def inspect(f):
    def inner (*args, **kwargs):
        res = f(*args, **kwargs)
        print (f'''Args: {args}
        Kwargs: {kwargs}'
        retvalue:  {res}''')
        return res
    return inner
@inspect
def concat (*args:str,reversed:bool)->str:
    result=''
    if reversed==True:
        for i in args[::-1]:
            result +=i
    else:
        for i in (args):
            result +=i
    return (result) 
concat ('First',' ','second',' ','third',reversed=True)