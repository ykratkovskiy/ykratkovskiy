import random
import time

num_of_teams = int (input("Введите количество команд, участвующих в игре "))
num_of_posts = int (input("Введите последний номер, отправленный в сообщении ")) 

if num_of_teams<20:
    q = 1
elif num_of_teams>20 and num_of_teams<50:
    q = 2
elif num_of_teams>50:
    q=3

for team in range (1,((num_of_teams+1)//q)):
    time.sleep(0.5)
    print (random.randint (1,num_of_posts))