from importlib.metadata import files
import click
from datetime import datetime
import random
from random import randint
import enum
from loguru import logger
import os
from pathlib import Path


logger.add('debug.log', format='{time}{level}{message}', level = 'DEBUG')


NY_date = datetime(2023,1,1)

class Colors(enum.Enum):
    yellow = 1
    green = 2
    white = 3 
    blue = 4
    red = 5
    orange = 6
    purple = 7
    pink = 9

class Toys(enum.Enum):
    bear = 1
    ball = 2 
    santa = 3
    angel = 4
    tree = 5 
    star = 6
    candy = 7
    snowflake = 8


@click.group()
def cli():
    pass


@click.command()
@click.option('--hours', is_flag=True, help='если нужны еще и часы до Нового года')

def newyear(hours):
    delta = NY_date - datetime.now()
    if hours:
        logger.success('Успешное выполнение newyear+hours')
        return (print (f'До нового года осталось {delta.days} дней и {round(delta.seconds/3600,1)} часов'))
    else:
        logger.success('Успешное выполнение newyear')
        return (print (f'До нового года осталось {delta.days} дней'))

@click.command()
def toy()-> str:
    logger.success('Успешное выполнение toy')
    color_list = (random.choice(list(Colors)))
    toy_list = (random.choice(list(Toys)))
    print (f'{color_list.name} {toy_list.name}')


@click.command()
def mkdir():
    Path('directory').mkdir(exist_ok=True)
    for i in range(10):
        Path(f'directory/'
        f'{randint(2020, 2022)}-'
        f'{randint(1,12)}-'
        f'{randint(1, 31)}.txt'
        ).touch()


@click.command()
def changedir():
    path = '.\directory'
    list_of_files = sorted(os.listdir(path))

    for file in list_of_files:
        fold1 = (file.split('-')[0])
        fold2 = (file.split('-')[1])
        fl = (file.split('-')[2])
        Path(f'directory/{fold1}/{fold2}/ ').mkdir(parents=True,exist_ok=True)
        path1 = f'.\directory/{file}'
        path2 = f'.\directory/{fold1}/{fold2}/{fl}'
        os.replace(path1,path2)


cli.add_command(newyear)
cli.add_command(toy)
cli.add_command(mkdir)
cli.add_command(changedir)
cli.main()