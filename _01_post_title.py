import requests
req =  requests.get('https://jsonplaceholder.typicode.com/posts')
posts = req.json()

for post in posts:
        print(f"Title: {post['title']}")