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
lst_of_id_posts = []


req_users = requests.get('https://jsonplaceholder.typicode.com/users')
users_data = req_users.json()

for i in users_data:
    lst_of_id.append(i['id'])

req_comments = requests.get('https://jsonplaceholder.typicode.com/comments')
comments_data = req_comments.json()

for i in comments_data:
    lst_of_id_posts.append(i['postId'])
lst_of_id_posts = list(dict.fromkeys(lst_of_id_posts))
# print (lst_of_id_posts)


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


async def main1():
    for i in lst_of_id:
        await asyncio.gather(
        users(f'https://jsonplaceholder.typicode.com/users/{i}'),
        posts(f'https://jsonplaceholder.typicode.com/users/{i}/posts'),
        todos(f'https://jsonplaceholder.typicode.com/users/{i}/todos'),
        albums(f'https://jsonplaceholder.typicode.com/users/{i}/albums'),
        )
    
async def main2():
    for j in lst_of_id_posts:
        await asyncio.gather(
        comments(f'https://jsonplaceholder.typicode.com/posts/{j}/comments')
        )



if __name__=='__main__':
    start_time = time.time()
    # asyncio.run(main1()) 
    asyncio.run(main2()) 
    print (lst_of_comments)
    
    # for post,comment in zip (lst_of_posts,lst_of_comments):
    #     print (f'"posts":{post},"comments":{comment}')
    print ('timing = ',time.time()-start_time)