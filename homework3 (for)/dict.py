import collections
persons = [
    {'name':'Veronika',
    'age':'32',
    'gender':'female'},
    {'name':'Peter',
    'age':'21',
    'gender':'male'},
    {'name':'John',
    'age':'26',
    'gender':'male'},
    {'name':'Ann',
    'age':'27',
    'gender':'female'},
    {'name':'Ann',
    'age':'27',
    'gender':'female'},
    {'name':'Ann',
    'age':'56',
    'gender':'female'},
    {'name':'Franck',
    'age':'48',
    'gender':'male'},
    {'name':'Andrew',
    'age':'33',
    'gender':'male'},
    {'name':'Andrew',
    'age':'35',
    'gender':'male'},
    {'name':'Mark',
    'age':'41',
    'gender':'male'},
    {'name':'Natalie',
    'age':'35',
    'gender':'female'},
    {'name':'Fred',
    'age':'35',
    'gender':'male'},
    {'name':'Nick',
    'age':'22',
    'gender':'male'},
    {'name':'Victoria',
    'age':'29',
    'gender':'female'},
    {'name':'Ferdinand',
    'age':'61',
    'gender':'male'},
    {'name':'Lucy',
    'age':'34',
    'gender':'female'},
    {'name':'Christie',
    'age':'34',
    'gender':'female'},
    {'name':'Ann',
    'age':'17',
    'gender':'female'},
    {'name':'Rose',
    'age':'32',
    'gender':'female'},
    {'name':'Marta',
    'age':'32',
    'gender':'female'},
    {'name':'Veronika',
    'age':'41',
    'gender':'female'},
    {'name':'Harry',
    'age':'24',
    'gender':'male'},
    {'name':'Faruh',
    'age':'27',
    'gender':'male'},
     {'name':'Jane',
    'age':'41',
    'gender':'female'},
    {'name':'Fillip',
    'age':'17',
    'gender':'male'},
    {'name':'Andrew',
    'age':'15',
    'gender':'male'}]
men = 0
women = 0
overall = 0
above18 = 0
for i in (persons):
    overall +=1
    if i['gender']=='male':
        men+=1
    if i['gender']=='female':
        women+=1
    if i['age']>='18':
        above18+=1
print (f'В списке всего {overall} человек. Из них {men} мужчин и {women} женщин. Совершеннолентних - {above18} человек.')
names = [i['name'] for i in persons]
print (f'Список всех имен: {names}')
ages = [i['age'] for i in persons]
set_of_ages = set(ages)
lst_of_ages_to_sort = list(set_of_ages)
srt_lst_of_ages = sorted(lst_of_ages_to_sort)
print (f'Отсортированный список возрастов без повторений: {srt_lst_of_ages}')
men_above35_fromF = [i['name'] for i in persons if i['age']>'35' and i['gender'] == 'male' and 'F' in i['name']]
print (f'Список мужчин старше 35-ти с именем на "F" : {men_above35_fromF}')
Counter = collections.Counter(names)
print (f'Три самых встречающихся имени: {Counter.most_common(3)}')