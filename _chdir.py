import os
from pathlib import Path

path = '.\directory'
list_of_files = sorted(os.listdir(path))
print (list_of_files)

year =[]
day = []
filename = []

for single_names in list_of_files:
    unp = single_names.split('-')
    year.append(unp[0])
    day.append(unp[1])
    filename.append(unp[2])

print (filename)     

    # shutil.rmtree('.\directory')

for num, original in enumerate(os.listdir('.\directory')):
    print (num,original)
    os.rename(original, filename[num])


# for num, filename in enumerate ((filename),1):
#     print (num,filename)
    
    
    # print (original)
           

# Path('directory2').mkdir(exist_ok=True)
# for original,fold1, fold2, fl in zip(list_of_files,year,day,filename):
#     os.rename(f'{original}', f'{filename}')
    
    
    # Path(f'directory2/{fold1}').mkdir(exist_ok=True)
    # Path(f'directory2/{fold1}/{fold2}').mkdir(exist_ok=True)
    
    # Path(f'./directory/{orig}').move(f'/directory2/{fold1}/{fold2}/{fl}')
    
    # Path(f'directory2/{fold1}/{fold2}/{fl}').mkdir(exist_ok=True)