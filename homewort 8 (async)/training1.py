import requests
import json
lst_of_users =[]
lst_of_id = []
lst_of_todos = []

lst_of_albums = []
lst_allposts = []
lst_allcomments=[]
lst_allalbums=[]

req_users = requests.get('https://jsonplaceholder.typicode.com/users')
req_todos = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')
req_posts = requests.get('https://jsonplaceholder.typicode.com/users/1/posts')
req_albums = requests.get('https://jsonplaceholder.typicode.com/users/1/albums')


users_data = req_users.json()
for i in users_data:
    lst_of_users.append(i['name'])

    
for i in range (1,len(lst_of_users)+1):
    req_posts = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}/posts')
    lst_of_posts=[]
    posts_data = req_posts.json()
    for i in posts_data:
        lst_of_posts.append(i['id'])
    lst_allposts.append(lst_of_posts)


for i in range (1,len(lst_of_users)+1):
    req_albums = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}/albums')
    lst_of_albums=[]
    albums_data = req_albums.json()
    for i in albums_data:
        lst_of_albums.append(i['title'])
    lst_allalbums.append(lst_of_albums)




# for i in range (1,101):
#     req_comment = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}/comments')
#     lst_of_comment=[]
#     comment_data = req_comment.json()
#     for i in comment_data:
#         lst_of_comment.append(i['id'])
#     lst_allcomments.append(lst_of_comment)



for user,post,album in zip(lst_of_users,lst_allposts,lst_allalbums):
    my_dict = dict({'User':f'{user}', 'posts':f'{post}', 'albums':f'{album}'})
    json_object = json.dumps(my_dict) 
    with open('users_dict', 'a') as f:
        json.dump(my_dict, f)

