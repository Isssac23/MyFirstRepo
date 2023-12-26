import requests

r =requests.get('https://pngimg.com/uploads/bruce_lee/bruce_lee_PNG17.png')

with open('bruce.png', 'wb') as f:
    f.write(r.content)