# file = open ('text.txt','w')
# file.write ('Homework 7: files - 1\n')
# file.close()

# file = open ('text.txt','a')
# for i in range (2,6):
#     file.write(f'Homework 7: files - {i}\n')
# file.close()


# file = open ('text.txt','a')
# file.writelines(
#     'First str\n'
#     'Second str\n'
# )
# file.close()

file = open ('text.txt','r')
print (file.read())
file.close()