import asyncio,aiohttp
import json

async def fetch(session, url,params={}):
    async with session.get(url,params=params) as response:
        return await response.json()

async def get_person(name):
    async with aiohttp.ClientSession() as session:
        params = {"api_key": "4d2712aacf92b2b1158e877b2194e607","query":name}
        person = await fetch(session, 'https://api.themoviedb.org/3/search/person',params)
        if person:
            return person["results"][0]
        else:
            return None

async def main():
    async with aiohttp.ClientSession() as session:
        p = await get_person("Keanu Reeves")
        params = {"api_key": "4d2712aacf92b2b1158e877b2194e607"}
        keanus = await fetch(session, f"https://api.themoviedb.org/3/person/{p['id']}/movie_credits",params)

        print("movies by keanus\n")
        i = 1
        for keanu in keanus['cast']:
            print(f"{i}. {keanu['title']}")
            i+=1

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())