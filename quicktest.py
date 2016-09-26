import requests
from bs4 import BeautifulSoup

def main():

    url = "https://github.com/sulaiman-allen?tab=overview&from=2016-03-10"
    html = requests.get(url)
    html = html
    soup = BeautifulSoup(html.content, "lxml")
    results = soup.find_all('span', class_='text-gray m-0')

    for result in results:
        print("result = ", result.string)
        print("type of result = ", type(result.string))
        if "had no activity during this period" in str(result.string.encode("utf-8")):
            print("true")
        else:
            print("false")



if __name__ == '__main__':
    main()
