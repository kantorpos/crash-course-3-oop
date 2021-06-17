from urllib import response

import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print('Success !', response)
        #print('Content ', response.text)
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil Pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print('Woops, ada kesalahan request', response.status_code)
except Exception as e:
    print('There is an error', e)
print('Program ended !')