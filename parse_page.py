import requests
from bs4 import BeautifulSoup
import shutil
import os
import unicodedata
import re

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def build_url(path):
    return 'http://www.lenstip.com/' + path


def download(url, path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)   

# https://www.lenstip.com/617.4-Lens_review-Sony_FE_70-200_mm_f_2.8_GM_OSS_II_Image_resolution.html
def parse_page(lens_code, lens_name):

    data_dir = 'data'
    lens_name = slugify(lens_name)

    lens_dir = os.path.join(data_dir, lens_name)

    if os.path.exists(lens_dir):
        return

    os.makedirs(lens_dir, exist_ok=True)

    url = f'https://www.lenstip.com/{lens_code}.4-Lens_review-{lens_name}.html'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')


    for img in soup.select('.shortcode-content img'):
        path = img['src'].split('/')[-1]
        download('http://www.lenstip.com/' + img['src'], os.path.join(lens_dir, path))
    