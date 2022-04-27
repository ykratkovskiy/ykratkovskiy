a = 'Кошка'

# def rev_cap(string):
#     string.lower()
#     return (string[::-1]).capitalize()

# print (rev_cap(a))

rev = ''
for i in a:
    rev = i + rev

print (rev)
