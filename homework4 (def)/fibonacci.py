def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-2)+fibo(n-1)
q = int(input('Введите  искомый индекс ряда Фибоначчи: ',))
print (fibo(q))