import click
from os import path

@click.group()
def cli():
    pass

@click.command()
def runner():
    
    #type name of original file with codes here!#
    file = '55 PrM Smetana 20%.txt'
    #############################################

    lst_of_codes = []
    num = int (input('Введите количество готовых ролей ',))
    for i in range (1,num+1):
        number_of_codes = int (input(f'Введите количество кодов в роле {i} ',))
        lst_of_codes.append(number_of_codes)


    full_name = path.basename(f'./{file}')
    name = path.splitext(full_name)[0]

    c=0
    original_file = open (full_name,'r')
    for i in range(len(lst_of_codes)):
        new_file = open(f'{name} rol {i+1}.txt', 'w')
        c=lst_of_codes[i]
        for j in range (1,c+1):
            new_file.write(original_file.readline())
    original_file.close()
    new_file.close()

cli.add_command(runner)
cli.main()