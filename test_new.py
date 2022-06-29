a = [1,2,3,4,5,7,8,8,7]
b = [4,5,6,7,8,4,3]

res = {item for item in a if item in b}

print (list(res))
