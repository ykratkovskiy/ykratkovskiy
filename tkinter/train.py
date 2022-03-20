import re
import pathlib

file = '87 PrM kefir 3,2 1L rol_166_vse.csv'
name = file.split('_vse')[0]
ext = pathlib.Path(file).suffix
name_for_rep = name.split('_')[0]
# print (name)
# print (ext)
print (name_for_rep)

rol_number = re.findall(r'_\d+',name)
print (rol_number)