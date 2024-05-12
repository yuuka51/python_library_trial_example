import requests

res = requests.get('https://pyladies.com/locations/')

with open('pyladies_locations.html', 'wb') as fout:
    fout.write(res.content)