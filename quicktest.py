import requests
from bs4 import BeautifulSoup

def main():

    url = "https://github.com/sulaiman-allen?tab=overview&from=2016-03-10"
    html = requests.get(url)
    html = html
    soup = BeautifulSoup(html.content, "lxml")
    print("results = ", soup.find_all('span', class_='text-gray m-0'))


if __name__ == '__main__':
    main()
