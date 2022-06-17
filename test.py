import random
import time

num_of_teams = int (input("Введите количество команд, участвующих в игре "))
num_of_posts = int (input("Введите последний номер, отправленный в сообщении ")) 
print ('Поехали!')
time.sleep(0.5)

for team in range (0,(num_of_teams+1)):
    time.sleep(0.3)
    print (random.randint (1,num_of_posts))
    if team == (num_of_teams-1):
        time.sleep(0.3)
        print ('И номер победителя!..')
        time.sleep(0.5)
        print ('...')
        time.sleep(0.5)
        print ('..')
        time.sleep(0.5)
        print ('.')
        time.sleep(0.3)