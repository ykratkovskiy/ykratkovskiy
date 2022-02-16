import os
from pathlib import Path

path = '.\directory'
list_of_files = sorted(os.listdir(path))

for file in list_of_files:
    fold1 = (file.split('-')[0])
    fold2 = (file.split('-')[1])
    fl = (file.split('-')[2])
    Path(f'directory/{fold1}/{fold2}/').mkdir(parents=True,exist_ok=True)
    path1 = f'.\directory\\{file}'
    path2 = f'.\directory\\{fold1}\\{fold2}\\{fl}'
    os.replace(path1,path2)
    