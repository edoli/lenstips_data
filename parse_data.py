import os
import requests
import re
import shutil
from bs4 import BeautifulSoup

def download(url, path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)   

lenses = [
    'Nikon Nikkor AF-S Micro 60 mm f/2.8G ED',
    'Nikon Nikkor AF 35 mm f/2D',
    'Nikon Nikkor AF-S 50 mm f/1.8G',
    'Sony Carl Zeiss Sonnar T* FE 55 mm f/1.8 ZA',
    'Samyang 50 mm f/1.4 AS UMC',
    'Samyang AF 50 mm f/1.4 FE',
    'Canon EF 50 mm f/1.8 STM',
    'Canon EF 16-35 mm f/2.8L II USM',
    'Carl Zeiss Otus 55 mm f/1.4 ZE/ZF.2'
]

pat = re.compile(r'\?q\=([^&]+)')

for lens in lenses:
    folder_name = lens[:18].strip()
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    res = requests.get('https://www.google.com/search?q=lenstip+%s+review' % (lens.replace(' ', '+')))
    
    soup = BeautifulSoup(res.text, 'lxml')

    results = soup.select('.r a')

    href = results[0]['href']

    m = re.search(pat, href)

    url = m.group(1)



    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml')

    m = re.search(r'href="([^\"]+Chromatic_aberration.html)"', res.text)

    suburl = m.group(1)

    data_page = requests.get('http://www.lenstip.com/' + suburl)


    soup = BeautifulSoup(data_page.text, 'lxml')

    imgs = soup.select('.shortcode-content img')

    i = 0
    for img in imgs:
        download('http://www.lenstip.com/' + img['src'], '%s/%d.jpg' % (folder_name, i))
        i += 1

