import requests
from bs4 import BeautifulSoup


def parse_list(url):
    soup = BeautifulSoup(requests.get(url).text)
    for anchor in soup.select('.product-content h2 a'):
        lens_name = anchor['href'][:-5]
        print(lens_name)


def main():
    url = 'https://www.lenstip.com/index.html?test=obiektywu&producent=&model=&typ=0&moc=25&sort=&szukaj=Search&szukaj=Search&przetest=1'
    parse_list(url)


if __name__ == '__main__':
    main()