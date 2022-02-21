import asyncio
import keyword
import time
from unicodedata import name
import httpx

url_users = 'https://jsonplaceholder.typicode.com/users'
url_posts = 'https://jsonplaceholder.typicode.com/posts'
url_comments = 'https://jsonplaceholder.typicode.com/comments'
url_albums = 'https://jsonplaceholder.typicode.com/albums'
url_photos = 'https://jsonplaceholder.typicode.com/photos'
url_todos = 'https://jsonplaceholder.typicode.com/todos'


async def wait(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        print (resp)
    

async def main():
    start_time = time.time()
    await wait(url_users)
    # await wait(url_posts)
    # await asyncio.gather(wait(url_users),wait(url_posts))
    print ('timing = ',time.time()-start_time)


if __name__=='__main__':
    asyncio.run(main()) 