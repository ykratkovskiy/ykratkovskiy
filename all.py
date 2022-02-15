import click
from datetime import datetime
import random
from random import randint
import enum
from loguru import logger

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


cli.add_command(newyear)
cli.add_command(toy)
cli.main()