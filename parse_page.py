import requests
from bs4 import BeautifulSoup

# https://www.lenstip.com/617.4-Lens_review-Sony_FE_70-200_mm_f_2.8_GM_OSS_II_Image_resolution.html
def parse_page(lens_name):
    url = 'https://www.lenstip.com/{lens_name}_Image_resolution.html'
    soup = BeautifulSoup(requests.get(url).text)
    for img in soup.select('.shortcode-content img'):
        print(img['src'])
    