import yaml

data = {
'age': 47,
'name': 'Peter',
'children': 
[
{
'age': 3,
'name': 'Alice'
},
{'age':7,
'name': 'John'}
],
'married': True,
'city': None}

with open ('data.yaml','w') as file:
    yaml.dump(data,file)

with open ('data.yaml') as file:
    data1 = yaml.safe_load(file)
print(data1)

child = data1.get('age')
print (child)