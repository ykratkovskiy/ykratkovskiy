import re
import pathlib
from unicodedata import name


file = '85 PrM tvorog 1% Rol 250_vse.csv'

name = re.split(r'vse', file)[0]
ext = re.split(r'vse', file)[1]
rol_number2 = re.findall(r'[\d\d]+_+', name)
rol_number1 = ''.join(rol_number2)
rol_number = re.split(r'_+',rol_number1)[0]
name_for_rep = re.split(r'%', name)[0]

print ('name =',name)
print ('extension =',ext)
print ('rol_mumber =',rol_number)
print ('name for rep =',name_for_rep)