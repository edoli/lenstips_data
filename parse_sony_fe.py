import requests
from bs4 import BeautifulSoup

from parse_page import parse_page


def decode_link(link):
    lens_code_with_page, lens_name = link.split('-Lens_review-')
    lens_code = lens_code_with_page.split('.')[0]
    return lens_code, lens_name

def parse_list(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    for anchor in soup.select('.product-content h2 a'):
        lens_link = anchor['href'][:-5]
        lens_code, lens_name = decode_link(lens_link)
        parse_page(lens_code, lens_name)


def main():
    url = 'https://www.lenstip.com/index.html?test=obiektywu&producent=&model=&typ=0&moc=25&sort=&szukaj=Search&szukaj=Search&przetest=1'
    parse_list(url)


if __name__ == '__main__':
    main()