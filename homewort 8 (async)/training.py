import asyncio
import time
import httpx
import requests

lst_of_id = []
lst_of_users = []
lst_of_posts = []
lst_of_todos = []
lst_of_albums = []
lst_of_comments = []
lst_of_photos = []

req_users = requests.get('https://jsonplaceholder.typicode.com/users')
users_data = req_users.json()

for i in users_data:
    lst_of_id.append(i['id'])



async def users(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        lst_of_users.append(resp.text)


async def posts(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        lst_of_posts.append(resp.text)
    

async def todos(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        lst_of_todos.append(resp.text)


async def albums(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        lst_of_albums.append(resp.text)


async def comments(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        lst_of_comments.append(resp.text)


async def photos(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        lst_of_photos.append(resp.text)



async def main():
    for i in (lst_of_id):
        # await users(f'https://jsonplaceholder.typicode.com/users/{i}'),
        # await posts(f'https://jsonplaceholder.typicode.com/users/{i}/posts'),
        # await comments(f'https://jsonplaceholder.typicode.com/posts/{i}/comments'),
        # await albums(f'https://jsonplaceholder.typicode.com/users/{i}/albums'),
        # await photos(f'https://jsonplaceholder.typicode.com/albums/{i}/photos'),
        # await todos(f'https://jsonplaceholder.typicode.com/users/{i}/todos')
            
        await asyncio.gather(
        users(f'https://jsonplaceholder.typicode.com/users/{i}'),
        posts(f'https://jsonplaceholder.typicode.com/users/{i}/posts'),
        # comments(f'https://jsonplaceholder.typicode.com/posts/{i}/comments'),
        albums(f'https://jsonplaceholder.typicode.com/users/{i}/albums'),
        # photos(f'https://jsonplaceholder.typicode.com/albums/{i}/photos'),
        todos(f'https://jsonplaceholder.typicode.com/users/{i}/todos')
        )
        
    

if __name__=='__main__':
    start_time = time.time()
    asyncio.run(main()) 
    
    for user,post,todo,album in zip (lst_of_users,lst_of_posts,lst_of_todos,lst_of_albums):
         print (f'"User":{user},"albums":{album},"todos":{todo},"posts":{post}')
    print ('timing = ',time.time()-start_time)
