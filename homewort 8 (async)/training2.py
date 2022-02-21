import requests

lst_of_users =[]
lst_of_id = []
lst_of_todos = []
lst_of_posts = []
lst_of_albums = []
lst_of_allposts =[]

req_users = requests.get('https://jsonplaceholder.typicode.com/users')
users_data = req_users.json()

users_data = req_users.json()
for i in users_data:
    lst_of_users.append(i['name'])

for i in range (0,3):
    # req_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}/todos')
    req_posts = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}/posts')
    # req_albums = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}/albums')
    posts_data = req_posts.json()
    for i in posts_data:
        lst_of_posts.append(i['id'])
    
    
# for name,posts in zip(lst_of_users,lst_of_posts):
#     print (f'User:{lst_of_users}, posts: {lst_of_posts}')