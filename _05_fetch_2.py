import json,requests

req = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = req.json()
req = requests.get('https://jsonplaceholder.typicode.com/users')
users = req.json()

for post in posts:
    user = list(filter(lambda user: user['id'] == post['id'], users))
    if len(user) > 0 : 
        post['user'] =  user[0]
    print(json.dumps(post))