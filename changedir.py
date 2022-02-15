import os
from pathlib import Path
import shutil

path = '.\directory'
list_of_files = sorted(os.listdir(path))

year =[]
day = []
filename = []

for single_names in list_of_files:
    unp = single_names.split('-')
    year.append(unp[0])
    day.append(unp[1])
    filename.append(unp[2])

shutil.rmtree('.\directory')
for fold1,fold2,fl in zip (year,day,filename):
    Path(f'directory/{fold1}/{fold2}/').mkdir(parents=True,exist_ok=True)
    Path(f'directory/{fold1}/{fold2}/{fl}').touch()